# 📄 Project Statement

## 1. Problem Definition

Traditional Snake Water Gun games are often implemented as command-line programs where the user enters a choice using text. While this approach is useful for learning basic programming, it does not provide an interactive graphical experience.

This project aims to develop a **desktop-based Snake Water Gun game using Python and Tkinter**. The application provides a graphical interface where the player can select **Snake, Water, or Gun** using buttons.

After the player makes a selection, the computer randomly generates its own choice. The program compares the two selections according to the rules of the Snake Water Gun game and displays the result of the round.

The application also maintains separate scores for the player and computer, allowing multiple rounds to be played during the same session.

---

# 2. Project Scope

The project is designed as a small and lightweight desktop application that runs locally on a computer.

The main focus is on implementing the graphical interface, game rules, random computer selection, result calculation, and score management.

### 2.1 Features Included

The application provides:

- A graphical interface developed using **Tkinter**
- Three playable choices:
  - 🐍 Snake
  - 💧 Water
  - 🔫 Gun
- Random computer selection
- Automatic comparison of player and computer choices
- Round-result calculation
- Display of the game result
- Separate player and computer scores
- Multiple rounds within one session
- Reset/New Game functionality
- Modular Python source files
- Event-driven GUI interaction

### 2.2 Features Not Included

The current version does not provide:

- Online multiplayer
- User registration or login
- Database integration
- Internet-based services
- Cloud storage
- Permanent match history
- Online leaderboards
- Network-based gameplay

The project is intended to remain a local single-player desktop application.

---

# 3. Target Users

The project is designed for the following users:

### Students

Students can use the project to understand Python programming, GUI development, and modular software design.

### Python Beginners

The project provides practical examples of functions, modules, conditional statements, dictionaries, random selection, and event handling.

### Tkinter Learners

Beginners can study how Tkinter widgets and button events can be used to create an interactive desktop application.

### Casual Players

Users can play a simple Snake Water Gun game locally without requiring an internet connection.

### Academic Demonstrations

The project can be used to demonstrate concepts such as modular programming, event-driven programming, GUI development, and basic game logic.

---

# 4. Functional Requirements

The system consists of several main functions that work together to provide the complete game.

## 4.1 Graphical User Interface

The application should provide a simple graphical window containing all the controls and information required to play the game.

The player should be able to interact with the application through buttons rather than entering commands through a terminal.

---

## 4.2 Player Selection

The interface provides three choices:

```text
Snake
Water
Gun
