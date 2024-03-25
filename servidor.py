import socket
from datetime import datetime

def main():
    host = '127.0.0.1'
    porta = 1234

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))

    print("Aguardando conexões...")
    servidor.listen(1)

    while True:
        conexao, endereco_cliente = servidor.accept()
        print(f"Conexão estabelecida com {endereco_cliente}")

        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conexao.sendall(data_atual.encode())

        conexao.close()

if __name__ == "__main__":
    main()
