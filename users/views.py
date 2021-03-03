import os
import json
from django.shortcuts import render

from .models import User

# Create your views here.
names = []
db_path = os.path.join('users', 'db.json')


def home(request):
    # print(request)
    print(db_path)
    return render(request, 'users/home.html', {'names': names})


def users(request):
    # file = open(db_path, 'r')
    # data = json.load(file)
    # file.close()
    users_list = []
    try:
        with open(db_path, 'r') as file:
            users_list = [User(**item) for item in json.load(file)]
    except FileNotFoundError as err:
        print(err)
    finally:
        print('finish')
    return render(request, 'users/users.html', {'users': users_list})


# def create_user(request, id, name, age):
#     print(id)
#     print(name)
#     print(age)

def create_user(request, **kwargs):
    with open(db_path, 'w') as file:
        json.dump(kwargs, file)
    with open(db_path, 'r') as file:
        user = User(**json.load(file))
    return render(request, 'users/users.html', {'user': user})
