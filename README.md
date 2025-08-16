# to-do-list
A command-line To-Do List application in Python that saves tasks to a text file for persistence.

# 📝 Command-Line To-Do List

A command-line to-do list application written in Python. This tool allows you to manage your tasks directly from the terminal and ensures your data is never lost by saving it to a local file.

## Features

* **Add, View, and Remove Tasks**: All the essential functionalities for task management.
* **File Persistence**: Your tasks are automatically saved to a `tasks.txt` file in the same directory. When you restart the application, your tasks are reloaded.
* **Menu-Driven Interface**: A simple and intuitive menu makes it easy to navigate and use.
* **Numbered Task Lists**: Tasks are displayed in a clean, numbered list, making them easy to read and reference for removal.

## How to Use

1.  Ensure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `to_do_list.py`).
3.  Run the script from your terminal:
    ```sh
    python to_do_list.py
    ```
4.  A `tasks.txt` file will be automatically created in the same directory to store your tasks.
5.  Use the menu to manage your tasks:
    * Enter `1` to add a new task.
    * Enter `2` to view your current list of tasks.
    * Enter `3` to remove a task by its number.
    * Enter `4` to close the program.
