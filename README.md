# ART - Advanced Terminal

ART (Advanced Terminal) is a simple Python program that provides basic system information and allows you to terminate processes using the command line interface. It uses the psutil module to retrieve system information such as CPU usage, memory usage, and network statistics.

Requirements
    Python 3.x
Usage
Run the program using the following command:
``python
python index.py
``

ART will prompt you to choose your system (Windows or Linux) and then display a list of available commands. Simply type in a command to perform the corresponding action. Here are some examples of available commands:

    help: display all available commands
    cpu: display CPU usage statistics
    mem: display memory usage statistics
    net: display network usage statistics
    kill <pid>: terminate process with given PID
    quit/exit: exit the program

Note that the kill command requires you to specify a process ID (<pid>) to terminate a specific process. You can find the PID of a process using the ps command on Linux systems or the Task Manager on Windows systems.

Credits
This program was created by KailUser(Syirezz).