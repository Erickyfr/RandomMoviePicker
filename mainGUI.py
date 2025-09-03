import tkinter as tk
from tkinter import messagebox, simpledialog
from movie_utils import get_all_movies, randomize_movie, load_user_history, save_user_history, UserAddMovie, build_database


class MovieMatchApp:
    def __init__(self,root):
        self.root = root
        self.root.title("MovieMatch 🎥")
        self.conn, self.cur = build_database()
        self.root.geometry("500x500")
        
        self.username = tk.StringVar()
        self.suggested_movie = tk.StringVar()
        self.added_movie = tk.StringVar()
        #self.genre = tk.StringVar()
        #self.selected_movie = tk.StringVar()
        #self.genre_check = tk.StringVar()
        #self.new_movie = tk.StringVar()
        
        self.start()
        #self.show_menu()
    
    def start(self):
        self.head_label = tk.Label(self.root, text="Welcome to MovieMatch !!!", font=("Algerian", 21))
        self.head_label.pack(pady=20)
        self.name_label = tk.Label(self.root, text="Enter your name:", font=("Times New Roman", 12, "bold"))
        self.name_label.pack(pady=4)
        self.name_entry = tk.Entry(self.root, textvariable=self.username)
        self.name_entry.pack(pady=3)
        self.btn_label = tk.Button(self.root, text="Submit",font=("Arial", 12), command= self.submit_name)
        self.btn_label.pack(pady=7)
        #self.show_menu()
        
    def submit_name(self):
        name = self.username.get()
        if not name:
            messagebox.showerror("❌ Error", "Please enter your name.")
            return
        else:
            messagebox.showinfo("Welcome", f"{name}, Welcome to MovieMatch!")
            
        #self.head_label.destroy()
        self.name_label.destroy()
        self.name_entry.destroy()
        self.btn_label.destroy()
        
        self.show_menu()
    
    def show_menu(self):
        greeting = f"Hello {self.username.get()}, Welcome what would you like to do?"
        
        self.menu_label = tk.Label(self.root, text=greeting, font=("Algerian", 15))
        self.menu_label.pack(pady=20)
        
        self.recommend_movie_btn = tk.Button(self.root, text= "Movie Recommendation", font=("Sans Serif", 12), command = self.suggest_movie)
        self.recommend_movie_btn.pack(pady=10)
        
        self.add_movie_btn = tk.Button(self.root, text="Add Movie", font= ("Sans Serif", 12), command = self.add_movie)
        self.add_movie_btn.pack(pady=10)
        
        self.show_user_history_btn = tk.Button(self.root, text= "Show User History 📜", font=("Sans Serif", 12), command = self.show_history)
        self.show_user_history_btn.pack(pady=10)
        
        self.exit_btn = tk.Button(self.root, text="Exit", font=("Sans Serif", 10), command = self.exit_app)
        self.exit_btn.pack(pady=10)

    def suggest_movie(self):
        #messagebox.showinfo("Recommendation", "Feature coming soon!")
        genre, movie_title = randomize_movie(self.cur)
        
        if movie_title:
            messagebox.showinfo("Movie Recommendation 🥳", f"Here is the movie recommended for you to watch: --{movie_title}-- in the --{genre}-- genre")
            save_user_history(self.username.get(), "suggested", genre, movie_title, self.conn, self.cur)
        else:
            messagebox.showerror("No Movies", "No Movies available in the database.")
        
        #self.recommend_movie_btn.destroy()
        
    def add_movie(self):
        genre_check = simpledialog.askstring("Genre", "Please enter the genre you want to add a movie to:")
        if not genre_check:
            return
        
        genre_check = genre_check.strip().title()
        
        self.cur.execute("SELECT DISTINCT genre FROM MOVIE_HISTORY")
        existing_genres = {row[0] for row in self.cur.fetchall()}
        
        if genre_check not in existing_genres:
            messagebox.showerror("Genre Error ‼️", f"Sorry {self.username.get()}, the genre --{genre_check}-- does not exist in our database")
            return
        
        new_movie = simpledialog.askstring("Movie", "Enter the movie name:")
        if not new_movie:
            return
        new_movie = new_movie.strip().title()
        
        self.cur.execute("SELECT 1 FROM MOVIE_HISTORY WHERE genre = ? AND movie_title = ?", (genre_check, new_movie))
        if self.cur.fetchone():
            messagebox.showerror("ALready Exists ⁉️", f"{new_movie} already exists in {genre_check} genre.")
            return
        
        self.cur.execute("INSERT INTO MOVIE_HISTORY(genre, movie_title) VALUES (?, ?)", (genre_check, new_movie))
        self.conn.commit()
        
        save_user_history(self.username.get(), "added", genre_check, new_movie, self.conn, self.cur)
        
        messagebox.showinfo("Movie Added 🎉", f"{new_movie} has been added to {genre_check} genre")
        
        #genre_check = UserAddMovie(self.username.get(), self.conn, self.cur)
        #self.add_movie_btn.destroy()
      
    def show_history(self):
        load_user_history(self.username.get(), self.cur)
        
    def exit_app(self):
        self.conn.close()
        self.root.destroy()

    '''def submit_name(self):
        
        tk.Label(self.root, text="Welcome to MovieMatch !!!", font=("Algerian", 21)).pack(pady=20)
        tk.Label(self.root, text="Enter your name:").pack(pady=4)
        tk.Entry(self.root, textvariable=self.username).pack(pady=3)
        tk.Button(self.root, text="Submit", command=self.submit_name).pack(pady=7)
        submit_name = tk.Label(self.root, textvariable=self.submit_name).pack(pady=5)
        
        name = self.username.get()
        if not name:
            messagebox.showerror("Name missing", "please enter your name.")
            return
        self.username.set(name)
        self.suggested_name = tk.Label.messagebox.showinfo(self.root, text=f"Hello {name}, Welcome to MovieMatch!").pack(pady=5)
        star = self.suggested_name.cget("text")
        messagebox.showinfo("Welcome", star)
        self.suggest_movie()
        
    def suggest_movie(self):
         
        tk.Label(self.root, text="Movie Suggestion:").pack(pady=10)
        tk.Label(self.root, textvariable=self.suggested_movie).pack(pady=5)
        
        name = self.username.get()
        if not name:
            messagebox.showerror("Name missing", "Please enter your name.")
            return
        
        
        genre, selected_movie = randomize_movie(self.cur)
        user_data = load_user_history(name, self.cur)
        if selected_movie:
            save_user_history(name, "suggested", genre, selected_movie, self.conn, self.cur)
            self.suggested_movie.set(f"The movie suggested to you is: {selected_movie} in the {genre} genre. Hope you enjoy it !!")
        else:
            self.suggested_movie.set("No movies in the database.")
            
    def add_movie(self):
        tk.Label(self.root, text="Would you like to add a movie?").pack(pady=10)
        tk.Button(self.root, text="Yes", command=self.add_movie).pack(pady=5)
        tk.Button(self.root, text="No", command=self.no_add_movie).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.exit_app).pack(pady=20)
        
        name =self.username.get()
        if not name:
            messagebox.showerror("Name missing", "Please enter your name.")
            return
        
        genre, new_movie = UserAddMovie(name, self.conn, self.cur)
        
        if new_movie:
            save_user_history(name, "added", genre, new_movie, self.conn, self.cur)
            messagebox.showinfo("Movie Added", f"{new_movie} has been added to {genre} genre.")
        else:
            messagebox.showerror("Already Exist", f"{new_movie} already exists in {genre} genre.")
            
    def no_add_movie(self):
        #tk.Button(self.root, text="No", command=self.no_add_movie).pack(pady=5)
        messagebox.showinfo("All Good!", "No problem! Enjoy your movie 😊")

        
    def exit_app(self):
        self.conn.close()
        self.root.destroy()'''
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MovieMatchApp(root)
    root.mainloop()
    