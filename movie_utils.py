import random
import sqlite3

'''Movie_history = "MovieList.json"
User_history = "UserHistory.json"'''
def build_database():
    conn = sqlite3.connect('MovieMatch.db')
    cur = conn.cursor()
    
    # Create MOVIE_HISTORY table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS MOVIE_HISTORY(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre TEXT NOT NULL,
            movie_title TEXT NOT NULL
        )'''
    )
    
    # Create USER_HISTORY table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS USER_HISTORY(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            type TEXT NOT NULL, --"suggested" or "added"
            genre TEXT,
            movie TEXT
        )'''
    )
    
    conn.commit()
    return conn, cur


'''def initialize_movies():
    cur.execute("SELECT COUNT(*) FROM MOVIE_HISTORY")
    if cur.fetchone()[0] == 0:
        for genre, titles in movies.items():
            for title in titles:
                cur.execute("INSERT INTO MOVIE_HISTORY (genre, movie_title) VALUES (?, ?)", (genre, title))
        conn.commit()'''






def get_all_movies(cur):
    cur.execute("SELECT genre, movie_title FROM MOVIE_HISTORY")
    movie_dict = {}
    for genre, movie_title in cur.fetchall():
        movie_dict.setdefault(genre, []).append(movie_title)
    return [movie_dict]

'''movies = {
    "Action": ["John Wick","Mad Max: Fury Road", "The Dark Knight", "Die Hard", "Gladiator"],
     "Comedy": ["Superbad","Step Brothers", "The Hangover", "Dumb and Dumber", "Monty Python and the Holy Grail"],
     "Drama" : ["The Shawshank Redemption", "Forrest Gump", "Fight Club", "The Godfather", "Parasite"],
     "Sci-Fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049", "Ex Machina"],
     "Horror": ["Get Out", "A Nightmare on Elm Street", "The Shining", "Hereditary", "It Follows"],
     "Thriller": ["Se7en", "Gone Girl", "Prisoners", "Zodiac", "No Country for Old Men"],
     "Animation": ["Spirited Away", "Toy Story", "Finding Nemo", "The Lion King", "Inside Out"]
     }'''

    
'''def SaveMovieHistory(Movie_history, movie):
    with open(Movie_history, "w") as file:
        json.dump(movie,file, indent=4)'''
        
        
def load_user_history(name, cur):
    cur.execute("SELECT type, genre, movie FROM USER_HISTORY WHERE username = ?", (name,))
    data = {"suggested_movie": [], "added_movie": []}
    for row in cur.fetchall():
        data[f"{row[0]}_movie"].append({"genre": row[1], "movie": row[2]})
    return data
        
def save_user_history(username, activity_type, genre, movie, conn, cur):
    cur.execute("INSERT INTO USER_HISTORY (username, type, genre, movie) VALUES (?, ?, ?, ?)",
                (username, activity_type, genre, movie))
    conn.commit()
    
        
'''def LoadMovieHistory(Movie_history):
    if os.path.exists(Movie_history):
        with open(Movie_history, "r") as file:
            return json.load(file)
    return [movies]'''

'''def SaveUserHistory(User_history,user_data):
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
        print(f"Welcome back {name}!, The last movie suggested to you was: {last_movie}. \n")'''
        
'''def RandomizeMovie(movie):
    random_movies = random.choice(movie)
    genre, movie = random.choice(list(random_movies.items()))
    selected_movie = random.choice(movie)
    return genre, selected_movie'''

def randomize_movie(cur):
    cur.execute("SELECT genre, movie_title FROM MOVIE_HISTORY")
    all_movies = cur.fetchall()
    if all_movies:
        return random.choice(all_movies)
    return None, None
    

def UserAddMovie(name, conn, cur):
    movie_request = input(f"{name}, would you like to add a movie? (yes/no)- ")
    if movie_request.strip().lower() == "yes":
        genre_check = input("please enter the genre you want to add a movie to: ").strip().title()
        
        cur.execute("SELECT DISTINCT genre FROM MOVIE_HISTORY")
        exist_genres = {row[0] for row in cur.fetchall()}
        
        if genre_check not in exist_genres:
            print(f"Sorry {name}, Looks like the genre --{genre_check}-- does not exist in our database.")
            print("Here are the available genres: ")
            print(", ".join(sorted(exist_genres)))
            return None, None
        
        new_movie = input("Enter the movie name: ").strip().title()
        
        cur.execute("SELECT 1 FROM MOVIE_HISTORY WHERE genre = ?  AND movie_title = ?", (genre_check, new_movie))
        if cur.fetchone():
            print(f"{new_movie} already exist in {genre_check} genre.")
            return None, None
        
        else:
            cur.execute("INSERT INTO MOVIE_HISTORY (genre, movie_title) VALUES (?, ?)", (genre_check, new_movie))
            conn.commit()
            print(f"{new_movie} has been added to {genre_check} genre.")
            return genre_check, new_movie
    return None, None

        
'''
        if genre_check.strip().title() in movie[0]:
            print(f"{name}, you have selected the {genre_check} genre. \n")
            print(f"{name}, Just to let you know, be curious of spelling and capitalization, for the movie you are adding. \n")
            new_movie = input(f"Enter the name of the movie you want to add in {genre_check}, {name}: ").title()
            
         #checking for duplicates
            if new_movie in movie[0][genre_check.title()]:  
                print(f"{name}, Looks like {new_movie} is already in the {genre_check.title()} genre. Try again. \n")
                return None, None
            else:
                movie[0][genre_check.title()].append(new_movie)
                print(f"{new_movie} has been added to the {genre_check.title()} genre. \n")
                return genre_check, new_movie
                
        else:
            print("Sorry, Looks like we do not have the genre you are looking for. \n")
        
    return None, None
'''  