from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# admin.site.register(User)
# Removed Team model registration as it is not compatible with Django admin
# Removed Activity model registration as it is not compatible with Django admin
# Removed Leaderboard model registration as it is not compatible with Django admin
admin.site.register(Workout)
