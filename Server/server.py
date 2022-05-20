import socket

from cryptography.fernet import Fernet

socket_address = ("127.0.0.1", 5050)  # Localhost on port 5050


def read_file(file):
    """Reads a file"""
    with open(file, 'rb') as file:
        return file.read()


def main():
    """Main function"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(socket_address)  # Open up port 5050 on localhost
        server.listen()
        connection, address = server.accept()  # If there's a connection, accept it

        with connection:

            # Decryption key
            fernet = Fernet(read_file("../Client/key.key").decode("utf-8"))

            data_string = ""

            while True:
                data = connection.recv(1024)
                data_string += data.decode("utf-8")
                if not data:
                    break

            print(fernet.decrypt(data_string.encode("utf-8")))


if __name__ == "__main__":
    main()
