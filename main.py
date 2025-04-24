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
    
    def start(self):
        tk.Label(self.root, text="Welcome to MovieMatch !!!", font=("Algerian", 21)).pack(pady=20)
        tk.Label(self.root, text="Enter your name:").pack(pady=4)
        tk.Entry(self.root, textvariable=self.username).pack(pady=3)
        tk.Button(self.root, text="Submit",font=("Arial", 12, "bold"), command= self.submit_name).pack(pady=7)
        
    def submit_name(self):
        name = self.username.get()
        if not name:
            messagebox.showerror("\b Error, Name missing", "Please enter your name.")
            return
        else:
            messagebox.showinfo("Welcome", f"{name}, Welcome to MovieMatch!")

    
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
    