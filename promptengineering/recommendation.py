from fastai.collab import *
from fastai.tabular.all import *
import pandas



####### VARIABLES

EMB_SIZE = 50
lr = 5e-3
epochs = 5
input_range = (0,5.5)

all_users_agg = [
    # John Doe
    # Enjoys tech events and social gatherings.
    [3, 50, 4], [3, 45, 3], [3, 47, 5], [3, 49, 2], [3, 55, 1],

    # Alice Jones
    # Avid music lover and interested in a variety of creative events.
    [5, 38, 5], [5, 41, 4], [5, 57, 3], [5, 58, 2], [5, 62, 1],

    # Bob Johnson
    # Focuses on professional development and tech-related meetups.
    [6, 44, 5], [6, 51, 4], [6, 72, 3], [6, 76, 2], [6, 77, 1],

    # Sue Doe
    # Enthusiastic about professional meetups and wellness events.
    [7, 47, 5], [7, 45, 4], [7, 48, 3], [7, 50, 2], [7, 54, 1],

    # Bob Davis
    # Enjoys social and wellness events with a creative edge.
    [8, 43, 5], [8, 67, 4], [8, 58, 3], [8, 57, 2], [8, 61, 1],

    # Alice Smith
    # Interested in tech meetups and social events.
    [9, 45, 5], [9, 44, 4], [9, 51, 3], [9, 72, 2], [9, 77, 1],

    # Mary Williams
    # Prefers social and career-oriented events.
    [10, 50, 5], [10, 45, 4], [10, 49, 3], [10, 55, 2], [10, 54, 1],

    # Mike Johnson
    # Focused on tech events and practical discussions.
    [11, 44, 5], [11, 51, 4], [11, 76, 3], [11, 48, 2], [11, 77, 1],

    # Sue Johnson
    # Enjoys a mix of social gatherings and tech events.
    [12, 50, 5], [12, 47, 4], [12, 45, 3], [12, 49, 2], [12, 54, 1],

    # John Bean
    # Likes tech meetups and creative workshops.
    [13, 47, 5], [13, 44, 4], [13, 49, 3], [13, 55, 2], [13, 60, 1],

    # Bob Doe
    # Interested in business strategies and tech innovations.
    [14, 61, 5], [14, 44, 4], [14, 51, 3], [14, 70, 2], [14, 56, 1],

    # Jane Davis
    # Enthusiastic about professional and social events.
    [15, 47, 5], [15, 45, 4], [15, 49, 3], [15, 55, 2], [15, 60, 1],

    # Mike Doe
    # Engages in tech discussions and creative workshops.
    [16, 44, 5], [16, 51, 4], [16, 76, 3], [16, 58, 2], [16, 84, 1]
]

####### IMPORT DATA HERE

# NEED A DATA FRAME like:

#     user item	rating	
# 0	196	  242	3	
# 1	186	  302	3	
# 2	22	  377	1	
# 3	244	  51	2	
# 4	166	  346	1
df = pandas.DataFrame(all_users_agg)
df.columns = ['user', 'item', 'rating']

# df = DATAFRAME()

# ASSUME THAT WE HAVE A DATAFRAME OF M*N x 3 (user, item, rating), assign a rating of 3 if user is interested in tags of the event, and 5 if the user has been to the event

dls = CollabDataLoaders.from_df(df, item_name='item', bs=64) # item column name must be item

n_users = len(dls.classes['user'])
n_items = len(dls.classes['item'])



####### MODEL #######

# We are using the DotProductBias model from fast.ai (simple but it should work well enough, can improve later)
class DotProductBias(Module):
    def __init__(self, n_users, n_items, n_factors, y_range=input_range):
        self.user_factors = Embedding(n_users, n_factors)
        self.user_bias = Embedding(n_users, 1)
        
        self.item_factors = Embedding(n_items, n_factors)
        self.item_bias = Embedding(n_items, 1)
        self.y_range = y_range
        
    def forward(self, x):
        users = self.user_factors(x[:,0])
        items = self.item_factors(x[:,1])
        res = (users * items).sum(dim=1, keepdim=True)
        res += self.user_bias(x[:,0]) + self.item_bias(x[:,1])
        return sigmoid_range(res, *self.y_range)
    
   



####### TRAINING #######

model = DotProductBias(n_users, n_items, EMB_SIZE)
learn = Learner(dls, model, loss_func=MSELossFlat())
learn.fit_one_cycle(epochs, lr)



####### PREDICTION #######


user_emb = model.user_factors.weight.detach().cpu().numpy()
user_bias = model.user_bias.weight.detach().cpu().numpy()

item_emb = model.item_factors.weight.detach().cpu().numpy()
item_bias = model.item_bias.weight.detach().cpu().numpy()
    
    
def predict(prediction_embedding, prediction_bias, item_emb, item_bias, n_recommendations, y_range=input_range):
    """ Requires the input of a prediction embedding and prediction bias
        
        Outputs:
        - array of size n_recommendations containing the index of top predicted events
        
        
        For an existing user (id = idx) please input:
        - user_emb[idx] as the prediction_embedding
        - user_bias[idx] as the prediction_bias
    """
    recommentation_list = []
    for i in range(len(item_emb)):
        item_embedding = item_emb[i]
        item_bias_prediction = item_bias[i]
        
        # Making predictions for each event in the form (i, predictions)
        res = np.dot(prediction_embedding, item_embedding)
        res += prediction_bias 
        res += item_bias_prediction
        recommentation_list.append((i,sigmoid_range(torch.from_numpy(res), *y_range)))
        
    # sort into a list and get only the n_recommendations
    recommentation_list = sorted(recommentation_list, key=lambda x: x[1], reverse=True)[:n_recommendations]

    # getting only the keys
    recommentation_list = dict(recommentation_list)
    recommentation_list = sorted(recommentation_list, key=recommentation_list.get, reverse=True)
    return recommentation_list


    
#### SAMPLE USAGE ##############

user_idx = 0
predictions = predict(user_emb[user_idx], user_bias[user_idx], item_emb, item_bias, 10)

print(predictions)
