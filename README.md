# 🎮 Tiny Pygame Games Collection

A collection of tiny games built using the Pygame library! 🕹️

## ✨ About the Project
This repository contains multiple small games created while following Udemy and YouTube tutorials, with some custom modifications to enhance creativity and learning. The main goal of this project is to improve my Object-Oriented Programming (OOP) skills in Python while exploring game development with Pygame.

## 📜 Games Included
* ✔️ SnakeGame: Classic Snake Game with aspect to retro mobile Game. 
* ✔️ SpaceInvader: The Classic Space Invader Game.
* ✔️ ZombieGame: A Simple Platform Game where you fight against zombies horde.
* ✔️ ZeldaStyleGame: A simple Demo Game with basic features that remember to zelda old games.

## Quick Start

Each game is located in its own folder and has an entry file named main.py. To run a specific game:

```bash
cd <game-folder>
python main.py
```

Make sure you have Pygame installed:
```bash
pip install pygame==2.6.1
```


## Getting Started with Virtual Enviroment

If you want to run the game but do not want to install globally pygame on your computer follow this tutorial to install pygame using a virtual environment. If not the case, just skip this section.

1. Check you have python installed

```bash
python3 --version
```

2. Check if you have pip installed

   * Check:

      ```bash
      python -m pip --version
      ```

   * Install:

      ```bash
      python -m pip install --upgrade pip
      ```

1. Check you have installed venv library to be able to create a virtual enviroment

```bash
python -m venv --help
```

If you do not recieve any answer you need to install virtual enviroment dependencies as follow:

```bash
pip3 install virtualenv
```

4. Create a virtual enviroment
```bash
python3 -m venv <name-venv>
```

5. Activate and Desactivate

   * Activation on Windows
   ```bash
   <name-venv>\Scripts\activate
   ```

   * Activation on Mac/Linux
   ```bash
   source <name-venv>/bin/activate
   ```

   * Desactivate. On terminal execute:
   ```bash
   deactivate
   ```


6. Verify
```bash
which python   # Mac/Linux
where python   # Windows
```

7. Install dependencies

Once time you stay under a venv you must install pygame to be able to run each game.
The games have been tested under pygame version 2.6.1.
To install pygame execute:

```bash
pip3 install pygame==X.X.X
```

Example
```bash
pip3 install pygame==2.6.1
```

## 📚 Credits & References

The games in this repository were created while following these tutorials, with some modifications:

* [UDEMY] <a href="https://www.udemy.com/course/the-art-of-doing-video-game-creation-with-python-and-pygame/" target="_blank">The Art of Doing: Video Game Creation With Python and Pygame</a>  by Michael Eramo
* [Youtube] <a href="https://www.youtube.com/watch?v=QU1pPzEGrqw" target="_blank">Zelda Style Game</a>  by Clear Code
