# Beginner-File-System
##  Project Title
**Beginner File System CLI** – A simple file and folder management tool built with Python.

##  What It Does
This project simulates a very basic file system where you can:
- Create and delete files and folders
- Navigate between directories
- Display current working directory
- View folder contents

All operations happen in memory (RAM), and the system structure is built using a tree data model.

## Features
- Mimics real file system navigation
- Works fully on command line
- Built for beginners with readable, clean code
- No external dependencies required

## Commands
| Command         | Description                                  |
|----------------|----------------------------------------------|
| `folder [name]` | Create a new folder                         |
| `file [name]`   | Create a new file                           |
| `list`          | List files and folders in current directory |
| `remove [name]` | Delete a file or folder                    |
| `go [name]`     | Change directory (`..` to go back)         |
| `path`          | Print full current directory path          |
| `exit`          | Exit the shell                             |

## 💻 How to Run
1. Save the code in a file called `beginner_file_system.py`
2. Open a terminal and run:
```bash
python3 beginner_file_system.py
```

## 🧠 Learning Goals
- Practice data structures (tree)
- Understand folder navigation logic
- Handle user input and parsing commands

## 📘 Sample Session
```
$ folder projects
$ go projects
$ file demo.txt
$ list
demo.txt
$ path
/projects
```

**Made by Shashank **  
