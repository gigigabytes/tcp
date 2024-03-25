import socket

def main():
    host = '127.0.0.1'
    porta = 1234

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    dados = cliente.recv(1024)
    print("Dados recebidos:", dados.decode())

    cliente.close()

if __name__ == "__main__":
    main()
