import db

# ----- Sample data ----- #





# ----------------------- #



def main():
    connection_string = db.return_connection_string()
    db.retrieveUsers()
    
    

if __name__ == "__main__":
    main()