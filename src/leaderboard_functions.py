import tinydb


    
def load_database():
    '''
    Loads the leaderboard database
    '''
    db = tinydb.TinyDB("db/ldb.json")
    if not db.all():
        #Make empty db
        db.truncate()
        for place in range(10,0,-1):
            # db.insert({"name":'',"score":0})
            db.insert({"rank":11-place,"name":"",'score':0})
        print("Database Created(*)")
    print("Database Loaded(*)")
    return db

def leaderboard_db_placement(l_db:tinydb.TinyDB ,name: str,score:int):
    
    ''' Place current player in leaderboard if eligable.
    
        Parameters
        ----------
        l_db: Tinydb
                    The leaderboard database holding the leaderboard data
        name: str
                    The string containing the players name.
        score: int
                    The score of the current player.
        
        Description
        -----------
        This function scans through the provided leaderboard database comparing the players score with the dictionaries' and if needed calls the function move_down_db and places them in the correct spot .
        
    '''
    
    if name=='':
        name ="Guest"
       
    l_Query = tinydb.Query()
    l_db = tinydb.TinyDB('db/ldb.json')
    for place in l_db:
        #place -->dictionary {"name":<name str>,"score":<score int>}
        if score>=place["score"]:
            move_down_db(l_db,place["rank"])
            l_db.update({"name":f"{name}","score":score},l_Query.rank == place["rank"])
            print("Entered in db(*)")
            return
    print("Entry ignored(*)")
            
def move_down_db(l_db : tinydb.TinyDB, rank : int):
    
    '''
    Move leaderboard rankings one place down.
    
    Parameters
    ----------
    leaderboard: Tinydb
                The leaderboard database that will have its rankings pushed down.
    rank: int
                The position in the leaderboard from which the rankings will be pushed down.
                
    Description
    -----------
    Provided the position from which the rankings will be pushed, this function moves every ranking one lower until it reaches the "rank" ranking to prepare for the insertion of a new ranking. The last ranking is lost.
    '''
    
    l_Query = tinydb.Query()
    for place in range(9,rank-1,-1):
        l_db.update({"name":l_db.all()[place-1]["name"],"score":l_db.all()[place-1]["score"]},l_Query.rank == place+1)
    print("Db lowered(*)")
