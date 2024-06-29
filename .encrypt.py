import os

string = ["a", "b", "c", "d"] # choose the public string you want for the encryption
prime_1 = 1 # choose the public prime you want for the encryption

def reader(file):
    with open(file, "r") as file:
        data = file.read().strip()
    message = list(data)
    return message

def key1(char):
    passkey = ord(char)
    return passkey

def key2(key):
    passkey = 1
    for char in key:
        passkey += ord(char)
        passkey *= ord(string[0])
        dummy = string[0]
        string.pop()
        string.append(dummy)
    return passkey

def encrypt(message):
    encrypted = []
    prime_2 = int(input("Enter passkey: ")) # choose the private prime you want for the encryption
    key = (key2(list(input("Enter key: ").strip()))) # choose the private string you want for the encryption
    addend = 0
    for char in message:
        addend *= prime_2 # choose the incremental u want to be used
        dummy = (key1(char)+addend)*key
        dummy *= prime_1
        to_append = hex(dummy)
        encrypted.append(to_append)
    return encrypted

def writer(message, file):
    with open(file, "w") as output:
        for code in message:
            output.write(code)

def main():
    input_file = input("Enter filename to be encrypted: ").strip()
    format = input("Enter the file format: ").strip()
    message = reader(input_file + '.' + format)
    encrypted_message = encrypt(message)
    output_file = os.path.join(input_file + "_encrypted." + format)
    writer(encrypted_message, output_file)

if __name__ == "__main__":
    main()



