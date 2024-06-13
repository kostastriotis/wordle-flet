import json

#Sxolia
#To leaderboard ws entity einai ena leksiko, deka stoixeiwn, opoy kathe key einai to placement kai kathe value ena list 
#dyo stoixeiwn, tou onomatos tou paikth (name) kai tou score tou (score)
#to leaderboard prepei na ginei load apo to arxeio sto opoio theloume na xrhsimopoihsoume to leksiko

#Aporia: Ti ginetai an syndethoun panw apo ena atoma kai theloun na apothhkeusoun leksiko?

def leaderboard_placement(leaderboard,name ,score ):
    
    ''' Place current player in leaderboard if eligable.
    
        Parameters
        ----------
        leaderboard: dict
                    The leaderboard dictionary with which the inputed data in compared .
        name: str
                    The string containing the players name.
        score: int
                    The score of the current player.
        
        Description
        -----------
        This function scans through the provided leaderboard dictionary comparing the players score with the dictionary's and calls the function move_lower to place them in the correct spot if needed.
        
    '''
    if name =='':
        name="Guest"
    
    for iterator in leaderboard:
        if iterator == '1':
            if score>leaderboard[iterator][1]:
                #Move down
                move_lower(leaderboard,int(iterator))
                leaderboard[iterator] = [name,score]
                print("Placement checked(*)")
                return
        else:
            if (leaderboard[iterator][1]<score<leaderboard[str(int(iterator)-1)][1]) or (leaderboard[iterator][1]<score==leaderboard[str(int(iterator)-1)][1]) :
                #Move down
                move_lower(leaderboard,int(iterator))
                leaderboard[iterator] = [name,score]
                print("Placement checked(*)")
                return
                
def move_lower(leaderboard, entry_place):
    '''
    Move leaderboard rankings one place down.
    
    Parameters
    ----------
    leaderboard: dict
                The leaderboard dictionary that will have its rankings pushed down.
    entry_place: int
                The position in the leaderboard from which the rankings will be pushed down.
                
    Description
    -----------
    Provided the position from which the rankings will be pushed, this function moves every ranking one lower until it reaches the entry_place ranking to prepare for the insertion of a new ranking. The last ranking is lost.
    '''
    for iterator in range(9, entry_place-1,-1):
        leaderboard[str(iterator+1)] = leaderboard[str(iterator)]

def populate_leaderboard_dict():
    '''
    Loads a leaderboard dictionary from leaderboard.json file.
    '''
    leaderboard_file = open("leaderboard.json")
    leaderboard = json.load(leaderboard_file)
    leaderboard_file.close()
    print("Leaderboard loaded(*)")
    return leaderboard

def save_leaderboard(leaderboard):
    '''
    Saves a leaderboard dictionary to a json file. 
    '''
    with open("leaderboard.json","w") as outfile:
        json.dump(leaderboard, outfile)
    print("Save successfull(*)")
    outfile.close()
