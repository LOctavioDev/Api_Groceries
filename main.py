from fastapi import FastAPI

app = FastAPI()

users = [
    {
        'id': 1,
        'age': '20',
        'name': 'Octavio',
        'last_name': 'DEV'
    },
    {
        'id': 2,
        'age': '19',
        'name': 'Octa',
        'last_name': 'LM'
    }
]

@app.get('/')
def message():
    return 'Hello worlds'
    
@app.get('/users')
def get_users():
    return users
    
@app.get('/user/{id}')
def get_user(id):
    for user in users:
        if user['id'] == int(id):
            return user
        
    return "user not found"