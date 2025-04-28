from mongoengine import Document, StringField, EmailField, IntField, ListField, ReferenceField, DateTimeField

# User model
class User(Document):
    username = StringField(max_length=100)
    email = EmailField(unique=True)
    password = StringField(max_length=100)

# Team model
class Team(Document):
    name = StringField(max_length=100)
    members = ListField(ReferenceField(User))

# Activity model
class Activity(Document):
    user = ReferenceField(User)
    description = StringField()
    date = DateTimeField()

# Leaderboard model
class Leaderboard(Document):
    team = ReferenceField(Team)
    points = IntField()

# Workout model
class Workout(Document):
    name = StringField(max_length=100)
    duration = IntField()  # in minutes
    calories_burned = IntField()
