import random
import sys
import os
import json

Movie_history = "MovieList.json"
User_history = "UserHistory.json"

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
    
def SaveMovieHistory(Movie_history, movie):
    with open(Movie_history, "w") as file:
        json.dump(movie,file, indent=4)
        
def LoadMovieHistory(Movie_history):
    if os.path.exists(Movie_history):
        with open(Movie_history, "r") as file:
            return json.load(file)
    return []

def SaveUserHistory(User_history,user_data):
    with open(User_history, "w") as userfile:
        json.dump(user_data, userfile, indent=4)
        
def LoadUserHistory(User_history):
    if os.path.exists(User_history):
        with open(User_history, "r") as userfile:
            return json.load(userfile)
    return {}
        
def CheckUserHistory(name, user_data):
    if name not in user_data:
        user_data[name] ={
        "suggested_movie": [],
        "added_movie" : []
        }
        print(f"Hello {name}, Welcome to MovieMatch!, Here is a movie suggestion for you.")
    else:
        last_movie = user_data[name]["suggested_movie"][-1]["movie"]
        print(f"Welcome back {name}!, The last movie suggested to you was: {last_movie}.")
        
def RandomizeMovie(movie):
    random_movies = random.choice(movie)
    genre, movie = random.choice(list(random_movies.items()))
    selected_movie = random.choice(movie)
    return genre, selected_movie

def UserAddMovie(movie, name):
    movie_request = input(f"{name}, would you like to add a movie? (yes/no)- ")
    if movie_request.strip().lower() == "yes":
        genre_check = input("please enter the genre you want to add a movie to: ")
    
        if genre_check.title() in movie[0]:
            print(f"{name}, you have selected the {genre_check.title()} genre.")
            print(f"{name}, Just to let you know, be curious of spelling and capitalization, for the movie you are adding.")
            new_movie = input(f"Enter the name of the movie you want to add in {genre_check}, {name}: ").title()
         #checking for duplicates
            if new_movie in movie[0][genre_check.title()]:  
                print(f"{name}, Looks like {new_movie} is already in the {genre_check.title()} genre. Try again.")
            else:
                movie[0][genre_check.title()].append(new_movie)
                print(f"{new_movie} has been added to the {genre_check.title()} genre.")
                
        else:
            print("Looks like we do not have the genre you are looking for")
    return None, None
        

def main():
    movie_data = LoadMovieHistory(Movie_history)
    user_data = LoadUserHistory(User_history)
    name = input("Enter your name: ").strip().capitalize()
    CheckUserHistory(name, user_data)
    genre, selected_movie = RandomizeMovie(movie_data)
    
    user_data[name]["suggested_movie"].append({"movie": selected_movie, "genre": genre})
    
    print(f"{name}, your movie suggestion is: {selected_movie} in the {genre} genre.")
    
    genre_check, new_movie = UserAddMovie(movie_data, name)
    if new_movie:
        user_data[name]["added_movie"].append({"movie": new_movie, "genre": genre_check})
        SaveMovieHistory(Movie_history, movie_data)
    
    SaveUserHistory(User_history, user_data)
    
    print(f"Thank you {name} for using MovieMatch! Your history has been saved.")
    
