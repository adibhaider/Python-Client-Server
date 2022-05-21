# Imports
import socket

from cryptography.fernet import Fernet

# Variables
socket_address = ("127.0.0.1", 5050)  # Localhost on port 5050


# Code begins
def read_file(file):
    """Reads a file"""
    with open(file, 'rb') as file:
        return file.read()


def main(encrypted_file=False, write_output=True, print_required=True):
    """Main function"""
    data = ""  # Empty string to hold the data

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(socket_address)  # Open up the designated socket address
        server.listen()
        connection, address = server.accept()  # If there's a connection, accept it

        with connection:
            while True:
                bytes_received = connection.recv(1024)

                # The data is converted into UTF-8 to be store in a string
                data += bytes_received.decode("utf-8")

                if not bytes_received:
                    break

    if encrypted_file:
        fernet = Fernet(read_file("../Client/key.key").decode("utf-8"))  # Decryption key
        # The data is converted back into bytes for Fernet to decrypt
        data = fernet.decrypt(data.encode("utf-8"))

    if print_required:
        print(data)
    if write_output:
        with open("./output.txt", "w") as file:
            file.write(data)


if __name__ == "__main__":
    # Set the encrypted_required argument to False if sending a dictionary
    main(encrypted_file=False, write_output=True, print_required=True)
