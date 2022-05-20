import socket
import encrypt
from cryptography.fernet import Fernet

HOST = "127.0.0.1"  # Localhost
PORT = 5050


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    connection, address = server.accept()
    with connection:

        fernet = Fernet(encrypt.read_file("key.key").decode("utf-8")) # Decryption key

        data_string = ""

        while True:
            data = connection.recv(1024)
            data_string += data.decode("utf-8")
            if not data:
                break

        print(fernet.decrypt(data_string.encode("utf-8")))