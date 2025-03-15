import random
import sys
import os
import json

def Movie_history(Movie_history):
    Movie_history = "MovieList.json"
def User_history(User_history):
    User_history = "UserHistory.json"


# Dictionary inside a list
movies = [
    {"Action": ["John Wick","Mad Max: Fury Road", "The Dark Knight", "Die Hard", "Gladiator"],
     "Comedy": ["Superbad","Step Brothers", "The Hangover", "Dumb and Dumber", "Monty Python and the Holy Grail"],
     "Drama" : ["The Shawshank Redemption", "Forrest Gump", "Fight Club", "The Godfather", "Parasite"],
     "Sci-Fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049", "Ex Machina"],
     "Horror": ["Get Out", "A Nightmare on Elm Street", "The Shining", "Hereditary", "It Follows"],
     "Thriller": ["Se7en", "Gone Girl", "Prisoners", "Zodiac", "No Country for Old Men"],
     "Animation": ["Spirited Away", "Toy Story", "Finding Nemo", "The Lion King", "Inside Out"]
     }
]

if os.path.exists(Movie_history):
    # Load existing movie data from the JSON file
    with open(Movie_history, "r") as file:
        movie = json.load(file)
else:
    movie = movies
# Saves the hardcoded movie data to the JSON file if it doesn't exist.

# Load user data from the JSON file if it exists
if os.path.exists(User_history):
    with open(User_history, "r") as userfile:
        user_data = json.load(userfile)
else:
    user_data = {}
print("-------------------------------")
name = input("Enter your name: ").capitalize()



# Check if the user is new or returning
if name not in user_data:
    user_data[name] ={
        "suggested_movie": [],
        "added_movie" : []
    }
    print(f"Hello {name}, Welcome to MovieMatch!, Here is a movie suggestion for you.")
else:
    last_movie = user_data[name]["suggested_movie"][-1]["movie"]
    print(f"Welcome back {name}!, The last movie suggested to you was: {last_movie}.")


random_movies = random.choice(movie)
genre, movie_list = random.choice(list(random_movies.items()))
selected_movie = random.choice(movie_list)

user_data[name]["suggested_movie"].append({
    "movie": selected_movie,
    "genre": genre
})

print("-------------------------------")

movie_request = input(f"{name}, would you like to add a movie? (yes/no)- ")

print("-------------------------------")

if movie_request.lower() == "yes":
    genre_check = input("please enter the genre you want to add a movie to: ")
    
    if genre_check.title() in movie[0]:
        print(f"{name}, you have selected the {genre_check.title()} genre.")
        print(f"{name}, Just to let you know, be curious of spelling and capitalization, for the movie you are adding.")
        new_movie = input(f"Enter the name of the movie you want to add in {genre_check}, {name}: ").title()
         #checking for duplicates
        if new_movie in movie[0][genre_check.title()]:  
            print(f"{name}, Looks like {new_movie} is already in the {genre_check.title()} genre. Try again.")
            print("Exiting the program...")
            sys.exit(0)
        else:
            movie[0][genre_check.title()].append(new_movie)
            print(f"{new_movie} has been added to the {genre_check.title()} genre.")
        
        user_data[name]["added_movie"].append({
    "movie": new_movie,
    "genre": genre_check.title()
})
        
        with open(Movie_history, "w") as file:
            json.dump(movie,file, indent=4)
            
        print(f"{name}, your movie suggestion is: {selected_movie}, in this genre: {genre}. Hope you enjoy it!.")
        
    else:
        print("Sorry, that genre is not available.")
        
        
elif movie_request.lower() == "no":
    print(f"{name}, your movie suggestion is: {selected_movie}, in this genre: {genre}. Hope you enjoy it!")
    
else:
    print(f"{name}, Looks like you entered an invalid option. Please try again. " )
    print("Exiting the program...")
    sys.exit(0)

with open(User_history, "w") as userfile:
    json.dump(user_data, userfile, indent=4)

print("-------------------------------")

print(f"Thank you {name}, for using MovieMatch!. Hope you enjoy your movie " +
      "suggestion and your history has been been saved. Hope to see you again.")