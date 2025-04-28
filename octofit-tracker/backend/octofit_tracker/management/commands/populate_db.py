from django.core.management.base import BaseCommand
from octofit_tracker.test_data import get_test_data
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from mongoengine.errors import NotUniqueError

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        test_data = get_test_data()

        # Populate users
        for user_data in test_data['users']:
            try:
                User(**user_data).save()
            except NotUniqueError:
                self.stdout.write(self.style.WARNING(f"User {user_data['email']} already exists."))

        # Populate teams
        for team_data in test_data['teams']:
            Team(**team_data).save()

        # Populate activities
        for activity_data in test_data['activities']:
            user = User.objects.get(username=activity_data['user'])  # Ensure user exists before creating activity
            Activity(user=user, description=activity_data['description']).save()

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            team = Team.objects.get(name=leaderboard_data['team'])
            Leaderboard(team=team, points=leaderboard_data['points']).save()

        # Populate workouts
        for workout_data in test_data['workouts']:
            Workout(**workout_data).save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
