import os

string = ["a", "b", "c", "d"] # choose the public string you want for the encryption
prime_1 = 1 # choose the public prime you want for the encryption

def reader(file):
    with open(file, "r") as file:
        data = file.read().strip()
    temp = data.split("0x")
    message = []
    for word in temp:
        if word == '':
            continue
        message.append(word)
    return message

def key1(num):
    passkey = chr(num)
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

def decrypt(message):
    decrypted = []
    prime_2 = int(input("Enter passkey: ")) # choose the private prime you want for the encryption
    key = (key2(list(input("Enter key: ").strip()))) # choose the private string you want for the encryption
    addend = 1
    for num in message:
        addend *= prime_2
        to_append = int(num, 16)
        to_append //= prime_1
        to_append //= key
        to_append -= addend
        decrypted.append(key1(to_append))
    return decrypted

def writer(message, file):
    with open(file, "w") as output:
        for code in message:
            output.write(code)

def main():
    input_file = input("Enter the filename to be decrypted: ").strip()
    format = input("Enter the file format: ").strip()
    message = reader(input_file + format)
    decrypted_message = decrypt(message)
    output_file = os.path.join(input_file + "_decrypted." + format)
    writer(decrypted_message, output_file)

if __name__ == "__main__":
    main()
