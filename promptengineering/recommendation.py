from fastai.collab import *
from fastai.tabular.all import *

####### VARIABLES

EMB_SIZE = 50
lr = 5e-3
epochs = 5
input_range = (0,5.5)

####### IMPORT DATA HERE

# NEED A DATA FRAME like:

#     user item	rating	
# 0	196	  242	3	
# 1	186	  302	3	
# 2	22	  377	1	
# 3	244	  51	2	
# 4	166	  346	1


df = DATAFRAME()

# ASSUME THAT WE HAVE A DATAFRAME OF M*N x 3 (user, item, rating), assign a rating of 3 if user is interested in tags of the event, and 5 if the user has been to the event

dls = CollabDataLoaders.from_df(ratings, item_name='item', bs=64) # item column name must be item

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


user_emb = model.user_factors.weight.detach().numpy()
user_bias = model.user_bias.weight.detach().numpy()

item_emb = model.item_factors.weight.detach().numpy()
item_bias = model.item_bias.weight.detach().numpy()
    
    
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
