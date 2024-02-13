def insert_unique_parents(response, mdb_collection):
    
    """
    Inserts the results of a reques that ARE NOT in the 
    given collection AND ARE NOT related to other object(childrens)

    response: --- : what to insert
    collection: ----: where to insert it
    """
    
    # 1. set conter for inserted objects
    inserted = 0
    
    # 3. Get the list of all elements alrready registered in the collection
    registered = [i['fsq_id'] for i in collection.find({}, {"_id":0,"fsq_id":1})]
    
    # 4. Iterate trough all elements of the response 
    for i in response["results"]:
        
        #Need to meet 2 conditions to be inserted:
        # It is not alrready registered:
        cond1 = i['fsq_id'] not in registered
        
        ## It's not a children of a parent:
        cond2 = "parent" not in list(i["related_places"].keys())
        
        # Check if the conditions are meet:
        if cond1 and cond2 == True:
            collection.insert_one(i)
            inserted += 1
            
    print(f'{inserted} items inserted into the collection')
               
    return