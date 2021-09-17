
import socket

host = '0.0.0.0'
port = 3222
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    case = int(input("1 - to check the domain.\n2 - to update domain.\n3 - to close session.\n"))
    if case == 1:
        data = input("Enter domain name:\n")
        client_socket.sendto(data.encode(), (host, port))
        server_data, sender = client_socket.recvfrom(512)
        print("Result is {}".format(server_data.decode()))
    elif case == 2:
        data = input("Enter domain name and new ip address like - domain:address\n")
        data = 'ADD ' + data.replace(" ", "")
        client_socket.sendto(data.encode(), (host, port))
        server_data, sender = client_socket.recvfrom(512)
        print("Result: {}".format(server_data.decode()))
    elif case == 3:
        exit(0)
    else:
        print("No such option(")
        exit(2)

    print('####################################')