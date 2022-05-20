import socket
import encrypt

socket_address = ("127.0.0.1", 5050)  # Localhost on port 5050

# Sample dictionary
cars = {
    "Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
    "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93},
    "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110},
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(socket_address)

    # Pickling options
    # pickling.to_bin(dict)
    # pickling.to_xml(dict)
    # pickling.to_json(dict)

    # s.sendall(pickling.to_xml(cars))

    encrypt.encrypt("data.txt")

    s.sendall(encrypt.read_file("../encrypted_file.txt"))

if __name__ == "__main__":
    print("Hello world!")