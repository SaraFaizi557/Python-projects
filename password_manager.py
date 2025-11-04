from cryptography.fernet import Fernet

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            try:
                decrypted_password = fer.decrypt(passw.encode()).decode()  # Decrypt password
                print("User:", user, "| Password:", decrypted_password)
            except Exception as e:
                print(f"Error decrypting {user}'s password: {str(e)}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    encrypted_password = fer.encrypt(pwd.encode()).decode()  # Encrypt the password
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_password + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
