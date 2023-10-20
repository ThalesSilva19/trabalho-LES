import socket

def get_protocol(port):
    try:
        file = open('/etc/services', 'r')
        for row in file:
            if str(port) in row:
                return row.split()[1]
    except FileNotFoundError:
        return "Protocol not found"

def ports_scanner(address, ports):
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((address, port))
        if code == 0:
            protocol = get_protocol(port)
            print "Port", port, "is opened. Protocol:", protocol

if __name__ == "__main__":
    target_address = '127.0.0.1'
    target_ports = [i for i in range(10000)]

    ports_scanner(target_address, target_ports)