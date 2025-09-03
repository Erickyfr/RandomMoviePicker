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
 
## Example
  - Here’s an example of how MovieMatch interacts with a user in CLI mode:  
 ![Screenshot 2025-03-25 164949](https://github.com/user-attachments/assets/cd591c51-9e16-49fc-a7fa-21617bb84bc1)
  - Here's an example of how MovieMatch interacts with a user in GUI mode:
<img width="622" height="662" alt="Screenshot 2025-09-03 141952" src="https://github.com/user-attachments/assets/d18192b7-1882-4909-b18e-8117c5dd5f22" />
<img width="1919" height="1018" alt="Screenshot 2025-09-03 142013" src="https://github.com/user-attachments/assets/a089c05b-e15a-4204-af1a-0601f630c265" />
<img width="444" height="192" alt="Screenshot 2025-09-03 142027" src="https://github.com/user-attachments/assets/9355b12e-af50-4092-ae09-44b9a2a2862b" />

## Roadmap
- [x] Implement core OOP movie logic  
- [x] Add SQLite database persistence  
- [x] Build initial CLI version  
- [ ] Expand Tkinter GUI features  
- [ ] Migrate GUI to PyQt for modern UI  
- [ ] (Future) Integrate external movie API (e.g., TMDB or OMDb)  



