from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# admin.site.register(User)
# Removed Team model registration as it is not compatible with Django admin
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
