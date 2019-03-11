
clients = 'Mario, Alberto, '

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already in the client\'s list')

def list_clients():
    global clients

    print(clients)


def _add_coma():
    global clients

    clients += ', '


def _print_welcome():
    print('WELCOME TO SALES')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate clients')
    print('[D]elete clients')


if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid Command')