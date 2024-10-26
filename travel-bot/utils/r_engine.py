def get_recommendations(user_preferences):
    preferences = user_preferences.get('interests')
    budget = user_preferences.get('budget')
    # Mock data or API-based recommendations can go here
    recommendations = [
        {"destination": "Paris", "activity": "Museum Tour"},
        {"destination": "Tokyo", "activity": "Sushi Tasting"},
        {"destination": "Sydney", "activity": "Beach Day"}
    ]
    # Filter recommendations based on preferences
    return [rec for rec in recommendations if rec['destination'] in preferences]

