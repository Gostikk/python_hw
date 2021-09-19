# Написать класс router.
# Должен иметь методы добавить/удалить/вывести список ip address.
# Должен иметь методы добавить/удалить/вывести список ip routes.

# Есть маршруты к непосредственно-подключенным сетям:
# если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
# значит у него должен быть маршрут:
# к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.

# Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
# то надо проверять доступен ли gateway.

# Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
# 192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.

# Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
# до которого у нас пока еще нет маршрута, то должен вылетать exception.

# Например:
# Добавляем ip-address 192.168.5.14/24 eth1.
# Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
# Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
# Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.

# Итого - 1 интерфейс и 3 маршрута в таблице.

import ipaddress


class Route:
    network = ''
    gateway = ''

    def __init__(self, network, gateway):
        self.network = network
        self.gateway = gateway


class Router:
    interfaces = {}
    routes = {}
    name = ''

    def __init__(self, name):
        self.interfaces = {}
        self.routes = {}
        self.name = name

    def add_address(self, interface, address):
        # Add an address to the interface and new route to the network via this address
        # interface - name of the router interface.
        # address - address of the router interface.
        
        if interface not in self.interfaces:
            self.interfaces[interface] = ipaddress.ip_interface(address)
            self.routes[self.interfaces[interface].network] = self.interfaces[interface].ip

    def delete_address(self, interface):
        # Delete an interface on the router and the routes available through this gateway
        # interface - name of the router interface.

        if interface in self.interfaces:
            del self.interfaces[interface]
            del self.routes[self.interfaces[interface].network]

    def get_all_addresses(self):
        # Print table of interfaces of the router

        for interface, address in self.interfaces.items():
            print("Interface {} has {} ip address".format(interface, address))

    def add_route(self, route: Route):
        # Add a route to the route table.
        # route - describes route - network and the gateway.
        # return Exception if route can't be reached

        network = ipaddress.ip_network(route.network)
        gateway = ipaddress.ip_address(route.gateway)
        for route in self.routes:
            if gateway in route:
                self.routes[network] = gateway
                return
        raise Exception("There is no such route to {}".format(gateway))

    def delete_route(self, network):
        # Delete a route in the route table
        # network - network to be deleted from route table.

        network = ipaddress.ip_network(network)
        if network in self.routes:
            del self.routes[network]

    def get_all_routes(self):
        # Print table of the routes of the router

        for network, address in self.routes.items():
            print("The destination network {} via gateway {}".format(network, address))


router = Router("MyRouter")

print('\n')
print("Лобавим адресс 192.168.0.1/24 в eth1")
router.add_address("eth1", "192.168.0.1/24")
print('\n')
print("Добавим маршрут к сети 172.16.0.0/16 через 192.168.0.24")
router.add_route(Route(network="172.16.0.0/16", gateway="192.168.0.24"))
print('\n')
print("Добавим маршрут к сети 172.24.0.0/16 через 172.16.8.1")
router.add_route(Route(network="172.24.0.0/16", gateway="172.16.8.1"))
print('\n')
print("таблица интерфесов:")
router.get_all_addresses()
print('\n')
print("Таблица маршрутизации:")
router.get_all_routes()
print('\n')
print("Удлаим адресс 172.24.0.0/16")
router.delete_route("172.24.0.0/16")
print('\n')
print("Таблица маршрутизации:")
router.get_all_routes()
print('\n')
router.add_route(Route(network="172.24.0.0/16", gateway="192.168.8.1"))