
clients = 'Mario, Alberto, '

def create_client(client_name):
    global clients

    clients += client_name
    _add_coma()


def list_clients():
    global clients

    print(clients)


def _add_coma():
    global clients

    clients += ', '


if __name__ == '__main__':
    list_clients()

    create_client('Prueba')

    list_clients()