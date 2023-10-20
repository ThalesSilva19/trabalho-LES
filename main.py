import socket

def obter_protocolo(porta):
    try:
        with open('/etc/services', 'r') as arquivo:
            for linha in arquivo:
                if str(porta) in linha:
                    return linha.split()[1]
    except FileNotFoundError:
        return "Protocolo não encontrado"

def scanner_de_portas(endereco, portas):
    for porta in portas:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.1)
        codigo = cliente.connect_ex((endereco, porta))
        if codigo == 0:
            protocolo = obter_protocolo(porta)
            print(f"Porta {porta} está aberta. Protocolo: {protocolo}")

if __name__ == "__main__":
    endereco_alvo = '127.0.0.1'  # Altere para o endereço que você deseja escanear
    portas_alvo = [80, 443, 22, 25]  # Adicione as portas que você deseja escanear

    scanner_de_portas(endereco_alvo, portas_alvo)