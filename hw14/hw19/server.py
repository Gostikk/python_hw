import socket



host = '0.0.0.0'
port = 3222
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((host, port))
local_domains = {}
while True:
    data, sender = server_socket.recvfrom(512)
    data_list = data.decode().split()
    if len(data_list) > 1 and data_list[0] == "ADD":
        local_domains[data_list[1].split(":")[0]] = data_list[1].split(":")[1]
        server_socket.sendto(b"domain address successfully updated", sender)
    elif data_list[0] in local_domains:
        server_socket.sendto(local_domains[data_list[0]].encode(), sender)
    else:
        try:
            server_socket.sendto(socket.gethostbyname(data_list[0]).encode(), sender)
        except:
            server_socket.sendto(b"unknown domain name", sender)