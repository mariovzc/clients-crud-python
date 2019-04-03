import sys

clients = ['pablo', 'ricardo']

def create_client(client_name):
    """ Create clients function """
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already in the client\'s list')


def list_clients():
    """ List clients function """
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))

def update_client(client_name, updated_client_name):
    """ Update the client name """
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        _not_found()

def delete_client(client_name):
    """ Delete the client of the list """
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _not_found()


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def _not_found():
    """ Print Not found message """
    print('Client is not in clients list')


def _print_welcome():
    """ Display Welcome Message """
    print('WELCOME TO SALES')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_name():
    """ Obtain the client name """

    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()

    if command == 'L':
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name , updated_client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        search_client(client_name)

    else:
        print('Invalid Command')