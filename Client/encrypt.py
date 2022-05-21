from cryptography.fernet import Fernet


def generate_key():
    """Generate an encryption key and write it to a file"""
    with open("./key.key", "wb") as file:
        file.write(Fernet.generate_key())


def read_file(file):
    """Reads a file"""
    with open(file, 'rb') as file:
        return file.read()


def encrypt(data):
    # Generate an encryption key and initialize the Fernet class
    fernet = Fernet(read_file("key.key"))

    # Create a new file called "encrypted_file.txt"
    with open("./encrypted_file.txt", "wb") as file:
        # Encrypt the data and write it to the file
        file.write(fernet.encrypt(read_file(data)))
