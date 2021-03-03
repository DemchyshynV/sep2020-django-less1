from django.db import models


# Create your models here.

class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
