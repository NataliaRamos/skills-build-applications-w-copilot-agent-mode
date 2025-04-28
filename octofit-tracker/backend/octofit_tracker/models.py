from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

# Activity model
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# Leaderboard model
class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

# Workout model
class Workout(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
