
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


def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print('Client is not in clients list')

def _add_coma():
    global clients

    clients += ', '


def _print_welcome():
    print('WELCOME TO SALES')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return input('What is the client name? ')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name + ',', updated_client_name + ',')
        list_clients()
    else:
        print('Invalid Command')