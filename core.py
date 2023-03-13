import psutil  # Importing the 'psutil' module to get system information
import os      # Importing the 'os' module to clear the console

# Defining a function to display the program on Windows systems
def windows():
    os.system('cls')   # Clearing the console on Windows systems
    print("Welcome to ART Windows")
    print("Write 'help' for get all commands")

    while True:
        option = input(">> ")

        if option == 'help':
            print('Available commands:')
            print('- help: print this message')
            print('- cpu: display CPU usage statistics')
            print('- mem: display memory usage statistics')
            print('- net: display network usage statistics')
            print('- kill <pid>: terminate process with given PID')
            print('- quit/exit: exit the program')

        elif option == 'cpu':
            cpu_percent = psutil.cpu_percent()
            print(f'CPU Usage: {cpu_percent}%')

        elif option == 'mem':
            virtual_memory = psutil.virtual_memory()
            print(f'Total Memory: {virtual_memory.total / (1024*1024):.2f} MB')
            print(f'Available Memory: {virtual_memory.available / (1024*1024):.2f} MB')

        elif option == 'net':
            net_io_counters = psutil.net_io_counters()
            print(f'Bytes sent: {net_io_counters.bytes_sent}')
            print(f'Bytes received: {net_io_counters.bytes_recv}')

        elif option.startswith('kill'):
            pid = int(option.split()[1])
            try:
                process = psutil.Process(pid)
                process.kill()
                print(f'Process {pid} terminated.')
            except psutil.NoSuchProcess:
                print(f'Process {pid} not found.')

        elif option in ['quit', 'exit']:
            break

        else:
            print(f'Invalid command: {option}. Type "help" for a list of available commands.')

# Defining a function to display the program on Linux systems
def linux():
    os.system('clear')  # Clearing the console on Linux systems
    print("Welcome to ART Linux")
    print("Write 'help' for get all commands")

    while True:
        option = input(">> ")

        if option == 'help':
            print('Available commands:')
            print('- help: print this message')
            print('- cpu: display CPU usage statistics')
            print('- mem: display memory usage statistics')
            print('- net: display network usage statistics')
            print('- kill <pid>: terminate process with given PID')
            print('- quit/exit: exit the program')

        elif option == 'cpu':
            cpu_percent = psutil.cpu_percent()
            print(f'CPU Usage: {cpu_percent}%')

        elif option == 'mem':
            virtual_memory = psutil.virtual_memory()
            print(f'Total Memory: {virtual_memory.total / (1024*1024):.2f} MB')
            print(f'Available Memory: {virtual_memory.available / (1024*1024):.2f} MB')

        elif option == 'net':
            net_io_counters = psutil.net_io_counters()
            print(f'Bytes sent: {net_io_counters.bytes_sent}')
            print(f'Bytes received: {net_io_counters.bytes_recv}')

        elif option.startswith('kill'):
            pid = int(option.split()[1])
            try:
                process = psutil.Process(pid)
                process.kill()
                print(f'Process {pid} terminated.')
            except psutil.NoSuchProcess:
                print(f'Process {pid} not found.')

        elif option in ['quit', 'exit']:
            break

        else:
            print(f'Invalid command: {option}. Type "help" for a list of available commands.')
