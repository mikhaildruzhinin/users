from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

fake_db = [
    {'id': 0, 'username': 'Alice'},
    {'id': 1, 'username': 'Bob'},
    {'id': 2, 'username': 'Carol'},
]


@app.post('/user/')
def create_user():
    '''Create a new user'''
    pass


@app.get('/users/')
def get_users():
    '''Get a list of users'''
    return fake_db


@app.get('/user/{user_id}')
def get_user(user_id: int):
    '''Get a specific user'''
    try:
        return list(filter(lambda user: user['id'] == user_id, fake_db))[0]
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.put('/user/{user_id}')
def edit_user():
    '''Edit user'''
    pass


@app.delete('/user/{user_id}')
def delete_user():
    '''Delete user'''
    pass