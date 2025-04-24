import random
import sqlite3

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


def get_all_movies(cur):
    cur.execute("SELECT genre, movie_title FROM MOVIE_HISTORY")
    movie_dict = {}
    for genre, movie_title in cur.fetchall():
        movie_dict.setdefault(genre, []).append(movie_title)
    return [movie_dict]

                
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

'''def initialize_movies():
    cur.execute("SELECT COUNT(*) FROM MOVIE_HISTORY")
    if cur.fetchone()[0] == 0:
        for genre, titles in movies.items():
            for title in titles:
                cur.execute("INSERT INTO MOVIE_HISTORY (genre, movie_title) VALUES (?, ?)", (genre, title))
        conn.commit()'''
