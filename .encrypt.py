import os
from primePy import primes

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
        passkey *= ord(char)
        passkey += ord(string[0])
        dummy = string[0]
        string.pop()
        string.append(dummy)
    return passkey

def get_greatest_prime(number):
    num = number
    flag = 1
    while flag:
        prime = primes.between(num, num+number)
        try:
            flag = 0
            return prime[0]
        except:
            num += number

def encrypt(message):
    encrypted = []
    prime_2 = int(input("Enter passkey: ")) # choose the private prime you want for the encryption
    key = get_greatest_prime(key2(list(input("Enter key: ").strip()))) # choose the private string you want for the encryption
    addend = 0
    for char in message:
        addend += prime_2 # choose the incremental u want to be used
        string.append(char)
        dummy = (key1(char)+addend)*key
        dummy *= prime_1
        to_append = hex(dummy)
        encrypted.append(to_append)
    return encrypted

def writer(message, file):
    with open(file, "a") as output:
        for code in message:
            output.write(code)

def main():
    input_file = input("Enter filename to be encrypted: ")
    message = reader(input_file)
    encrypted_message = encrypt(message)
    file = input("Choose name of file: ") + ".txt"
    output_file = os.path.join(file)
    writer(encrypted_message, output_file)

if __name__ == "__main__":
    main()



