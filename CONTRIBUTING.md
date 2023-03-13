# Contributing to ART

Thank you for your interest in contributing to ART (Advanced Terminal)!

Requirements
    Python 3.x

Usage
To run the program, use the following command:

``python
python index.py
``

ART will prompt you to choose your system (Windows or Linux) and then display a list of available commands. Simply type in a command to perform the corresponding action.

Contributing Guidelines
If you would like to contribute to ART, please follow these guidelines:

Fork this repository and clone it to your local machine.
Create a new branch for your changes: git checkout -b my-new-feature.
Make your changes to the code or documentation.
Test your changes thoroughly.
Commit your changes with a descriptive commit message: git commit -am 'Add some feature'.
Push your changes to your fork: git push origin my-new-feature.
Submit a pull request to this repository and wait for feedback from the maintainers.
Please ensure that your code adheres to the PEP 8 style guide and includes appropriate documentation and tests. By contributing to this project, you agree to license your work under the MIT License.

Available Commands
Here are some examples of available commands in ART:

    help: display all available commands
    cpu: display CPU usage statistics
    mem: display memory usage statistics
    net: display network usage statistics
    kill <pid>: terminate process with given PID
    quit/exit: exit the program

Note that the kill command requires you to specify a process ID (<pid>) to terminate a specific process. You can find the PID of a process using the ps command on Linux systems or the Task Manager on Windows systems.

Credits
This program was created by KailUser(Syirezz).