def userEntity(item) -> dict: #THIS FUNCTION RETURN A DICTIONARY
    return {
        "id": str(item["_id"]), #ID OF THE TYPE MONGO _ID
        "name": item["name"], 
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity] #LIST OF USERS IN THE MONGO ATLAS