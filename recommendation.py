# Simple Recommendation System

# Dictionary of users and their favorite movies
user_preferences = {
    "Kuswanth": ["Leo", "Jailer", "KGF"],
    "Rahul": ["KGF", "Salaar", "Pushpa"],
    "Anu": ["Leo", "Pushpa", "Vikram"],
    "Sai": ["Jailer", "Vikram", "Salaar"]
}

# Function to recommend movies
def recommend_movies(user_name):
    if user_name not in user_preferences:
        print("User not found!")
        return

    user_movies = user_preferences[user_name]
    recommendations = []

    # Compare with other users
    for other_user, movies in user_preferences.items():

        if other_user != user_name:

            # Check common movies
            common = set(user_movies).intersection(set(movies))

            # If users have similar taste
            if common:

                for movie in movies:
                    if movie not in user_movies and movie not in recommendations:
                        recommendations.append(movie)

    # Display recommendations
    print("\nRecommended Movies for", user_name, ":")

    if recommendations:
        for movie in recommendations:
            print("-", movie)
    else:
        print("No recommendations available.")

# Main Program
print("Users:", list(user_preferences.keys()))

name = input("\nEnter user name: ")

recommend_movies(name)