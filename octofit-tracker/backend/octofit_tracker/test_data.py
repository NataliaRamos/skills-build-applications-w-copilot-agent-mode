# Test data for populating the octofit_db database

def get_test_data():
    return {
        "users": [
            {"username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"username": "jane_smith", "email": "jane@example.com", "password": "password123"}
        ],
        "teams": [
            {"name": "Team Alpha"},
            {"name": "Team Beta"}
        ],
        "activities": [
            {"user": "john_doe", "description": "Running"},
            {"user": "jane_smith", "description": "Cycling"}
        ],
        "leaderboard": [
            {"team": "Team Alpha", "points": 150},
            {"team": "Team Beta", "points": 120}
        ],
        "workouts": [
            {"name": "Yoga", "duration": 60, "calories_burned": 200},
            {"name": "HIIT", "duration": 30, "calories_burned": 300}
        ]
    }
