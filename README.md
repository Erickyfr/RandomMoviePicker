# MovieMatch
## Overview
MovieMatch is a Python-based movie recommendation system that suggests random movies from various genres and allows users to contribute to the movie database. The application maintains user histories and movie lists in SQLite for session persistence. The project was first built using object-oriented programming (OOP) principles to handle movies, users, and recommendations. After implementing database persistence, development moved toward adding a graphical user interface (GUI). An initial version is being built with Tkinter, but the project is considering migrating to PyQt for a more modern and flexible interface.

## Features
- **Random Movie Suggestions**: Recommends a random movie from a curated list of genres.
- **User History Tracking**: Remembers previous recommendations for returning users.
- **Movie Database Expansion**: Allows users to add new movies to existing genres.
- **Data Persistence**: Saves all data in SQLite for future sessions.
- **Genre Categories**: Includes 7 popular movie genres with 5 movies each.

## Available Genres
- Action
- Comedy
- Drama 
- Sci-Fi
- Horror
- Thriller
- Animation

## Installation
- Ensure you have Python 3.x installed on your system.
- No additional dependencies beyond Python's standard library are required.

## Usage
- Run the script using the command:
  
`python mainCLI.py` <!-- Command-Line Interface.--> <br>
`python mainGUI.py` <!--GUI interface.-->

- Follow the on-screen prompts:
    - Enter your name when prompted.
    - The system will greet you and provide a movie recommendation.
    - You'll have the option to add a movie to the database.
    - Your interaction history will be saved for future sessions.
 
## Example of Interaction with mainCLI
- Below is an example of how MovieMatch interacts with a user. The program greets returning users, suggests a movie, and allows them to add a new movie to a genre:
  
 ![Screenshot 2025-03-25 164949](https://github.com/user-attachments/assets/cd591c51-9e16-49fc-a7fa-21617bb84bc1)
 
