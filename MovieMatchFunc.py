from movie_utils import get_all_movies, randomize_movie, load_user_history, save_user_history, UserAddMovie, build_database

def main():
    
    conn, cur = build_database()
    '''initialize_movies()'''

    movie_data = get_all_movies(cur)
    
    name = input("Enter your name: ").strip().capitalize()
    
    user_data = load_user_history(name, cur)
    
    print("-"*30)
    
    if user_data["suggested_movie"]:
        last_movie = user_data["suggested_movie"][-1]["movie"]
        print(f"Welcome back {name}!, The last movie suggested to you was: {last_movie}.\n")
    else:
        print(f"Hello {name}, Welcome to MovieMatch!\n")
        
    genre, selected_movie = randomize_movie(cur)
    
    if selected_movie:
        save_user_history(name, "suggested", genre, selected_movie, conn, cur)
        
    genre_check, new_movie = UserAddMovie(name, conn, cur)
    
    if new_movie:
        save_user_history(name, "added", genre_check, new_movie, conn, cur)
    
    print("-"*30)
    print(f"{name}, The movie suggested to you is: {selected_movie} in the {genre} genre. Hope you enjoy it !!")
    print(f"Thank you {name} for using MovieMatch!. Your history has been saved.\n")
    
    conn.close()

    '''CheckUserHistory(name, user_data)
    genre, selected_movie = RandomizeMovie(movie_data)
    
    #saving user history
    user_data[name]["suggested_movie"].append({"movie": selected_movie, "genre": genre})
    
    #Calling a function
    genre_check, new_movie = UserAddMovie(movie_data, name)
    
    # Save newly added movie to both user history and main database    
    if new_movie:
        user_data[name]["added_movie"].append({"movie": new_movie, "genre": genre_check})
        SaveMovieHistory(Movie_history, movie_data)
    
    SaveUserHistory(User_history, user_data)
    
    
    print(f"\n {name}, your movie suggestion is: {selected_movie} in the {genre} genre. Hope you enjoy it!!")
    print(f"\n Thank you {name} for using MovieMatch! Your history has been saved. \n")'''
    

if __name__ == "__main__":
    main()