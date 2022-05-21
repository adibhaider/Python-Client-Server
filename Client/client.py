# Imports
import socket

import encrypt

import pickling

# Variables

encryption_required = False # Only for files
socket_address = ("127.0.0.1", 5050)  # Localhost on port 5050

# Sample dictionary
cars = {
    "Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93},
    "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110}
}


# Code begins
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect(socket_address)

        # Send a dictionary through pickling
        # server.sendall(pickling.to_json(cars))

        # Send a file
        if encryption_required:
            encrypt.encrypt("./data.txt")
            server.sendall(encrypt.read_file("./encrypted_file.txt")) # Send file to the server
        else:
            server.sendall(encrypt.read_file("./data.txt"))


if __name__ == "__main__":
    main()
