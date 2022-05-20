import socket
import encrypt
import pickling

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5050  # The port used by the server

# Sample dictionary
cars = {
    "Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93},
    "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110},
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Pickling options
    # pickling.to_bin(dict)
    # pickling.to_xml(dict)
    # pickling.to_json(dict)

    # s.sendall(pickling.to_xml(cars))

    encrypt.encrypt("data.txt")

    s.sendall(encrypt.read_file("encrypted_file.txt"))
