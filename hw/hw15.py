from ipaddress import ip_address, ip_network

"""
Написать класс router.
Должен иметь методы добавить/удалить/вывести список ip address.
Должен иметь методы добавить/удалить/вывести список ip routes.

Есть маршруты к непосредственно-подключенным сетям:
если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
значит у него должен быть маршрут:
к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.

Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
то надо проверять доступен ли gateway.

Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.

Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
до которого у нас пока еще нет маршрута, то должен вылетать exception.

Например:
Добавляем ip-address 192.168.5.14/24 eth1.
Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.

Итого - 1 интерфейс и 3 маршрута в таблице.
"""


class Router:
    interfaces = {}
    ip_route_table = {}

    def add_ip_interface(self, addr, interface):
        try:
            self.interfaces[addr] = interface
            self.ip_route_table[ip_address(addr[:-3])] = ip_network(addr, False)
        except ValueError:
            print("Ip-address is not added. Try to use mask")

    def del_ip_interface(self, interface):
        self.interfaces.pop(interface)

    def show_ip_interfaces(self):
        print("-----IP INTERFACES-----")
        for interface in self.interfaces:
            print("{0} - {1}".format(interface, self.interfaces[interface]))

    def add_ip_route(self, addr, gateway):
        gateway = ip_address(gateway)
        for network in self.ip_route_table.values():
            if gateway in network:
                self.ip_route_table[gateway] = ip_network(addr, False)
                print("Маршрут до {0} был добавлен через {1}".format(addr, gateway))
                return True
        print("Exception! Маршрут до {0} не добавлен".format(addr))
        return False

    def del_ip_route(self, addr):
        self.ip_route_table.pop(addr)

    def show_ip_routes(self):
        print("-----IP ROUTE TABLE-----")
        for route in self.ip_route_table:
            print("{0} через {1}".format(self.ip_route_table[route], route))


router = Router()
router.add_ip_interface("192.168.5.14/24", "eth1")
router.add_ip_route("172.16.0.0/16", "192.168.5.1")
router.add_ip_route("172.24.0.0/16", "192.168.8.1")
router.add_ip_route("172.24.0.0/16", "172.16.8.1")

router.show_ip_routes()
router.show_ip_interfaces()
