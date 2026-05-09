# 🧠 Memory Game - Modification and Version Control

## 📄 Repository Description
This repository contains the source code for the **Memory Game** in Python. The original base code belongs to the *Free Python Games* collection by Grant Jenks. The purpose of this repository is to document the modifications made to the source code while working as a team using a distributed version control system (Git and GitHub).

The source code has been documented and formatted strictly following Python style guides (**PEP 8**), ensuring clean, modular, and professional programming standards according to the institute's guidelines.

## 🛠️ Features Implemented
As part of the activity, the original code was modified by integrating the following features. The software engineering rule of "one feature per commit" was applied by working on separate branches:

*   **Tap Counter:** A real-time tap tracker was implemented using a `Turtle` writer that updates and displays the number of taps on screen as the player interacts with the board. *(Developed by: José Manuel Cisneros Palma)*
*   **Win Message:** A victory screen function was developed that detects when all tiles have been uncovered and displays a congratulatory message showing the total number of taps used to complete the game. *(Developed by: Juan Manuel Gonzalez Rocha)*

## 👥 Collaboration Dynamics (Git & GitHub Roles)
To fulfill the evidence criteria and simulate a real professional development environment, team members alternated roles using the distributed repository workflow (*Fork & Pull Request*):

*   **Owner Role:** José Manuel Cisneros Palma (`jose-de`)
*   **Fork Role (Collaborator):** Juan Manuel Gonzalez Rocha

**Workflow:**
1.  The project was divided by creating individual branches for each requirement.
2.  Code integration from the collaborator to the base repository was done via `Pull Requests`.
3.  Conflicts were resolved, and the corresponding `Merges` were executed on GitHub.
4.  A clean commit history was maintained with precise descriptions of each update.

## 🚀 How to Run the Game
1. Clone this repository to your local machine:
   `git clone https://github.com/jose-de/memory_game.git`
2. Ensure you have Python 3 and the `freegames` library installed.
3. Run the main file from your terminal:
   `python memory_game.py`
