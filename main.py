import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer'
    }
]

def create_client(client):
    """ Create clients function """
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')


def list_clients():
    """ List clients function """
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))

def update_client(updated_client_fields, index):
    """ Update the client name """
    global clients

    if index is not None:
        clients[index].update(updated_client_fields)
    else:
        _not_found()


def delete_client(client_id):
    """ Delete the client of the list """
    global clients

    for idx, dummy_client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break
        else:
            _not_found()


def search_client(client_name):
    for client in clients:
        if client['name'] == client_name:
            print('{name} | {company} | {email} | {position}'.format(
                name = client['name'],
                company = client['company'],
                email = client['email'],
                position = client['position']
            ))
            break

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


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {} ?'.format(field_name))

    return field

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

def _get_index(client_name):
    global clients

    for idx, client in enumerate(clients):
        print(idx)
        if client['name'] == client_name:
            return idx


def _set_update_fields():
    updates = False
    updated_client_fields = {}

    while not updates:
        field = input('What field do you want to update? (exit to leave) ').lower()
        
        if field == 'exit':
            updates = True
            continue
        
        field_value = input('What is the new {}?: '.format(field)).capitalize()

        updated_client_fields.setdefault(field, field_value)

    return updated_client_fields


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
        list_clients()

    if command == 'L':
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        index = _get_index(client_name)
        delete_client(index)
        list_clients()

    elif command == 'U':
        client_name = input('Who do you want to update? ')
        updated_client_fields = _set_update_fields()
        index = _get_index(client_name)
        update_client(updated_client_fields, index)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        search_client(client_name)

    else:
        print('Invalid Command')