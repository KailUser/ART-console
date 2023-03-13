import os
install = input("Install reqiurements module? y - yes n - no ")
if install.lower() == "y":
    os.system("pip3 install psutil")
elif install.lower() == 'n':
    pass
else:
 os.kill()
import core as cr   # Importing the 'core' module to access the 'windows' and 'linux' functions
import psutil       # Importing the 'psutil' module to get system information

#Main Code


if __name__ == "__main__":
    os.system('cls')
    os.system('clear')
    print("Welcome to ART\nThanks for using my terminal")

    # Asking the user which operating system they are on
    system= input("What is your system? ( L ) - Linux ( W ) - Windows\n>> ")

    # Launching the 'windows' function if the user is on Windows
    if system.lower() == "w":
        cr.windows()

    # Launching the 'linux' function if the user is on Linux
    elif system.lower() == "l":
        cr.linux()

    # Displaying an error message if the user inputs an invalid option
    else:
        print("Invalid option. Please choose either 'L' or 'W'.")