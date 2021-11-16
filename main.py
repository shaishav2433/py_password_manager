from cryptography.fernet import Fernet

# pending work
# add error handlings
# add remove option
# clean code
# improvement for key matching

#key = Fernet.generate_key()
key = b'00ujoGeP4k-yPkfYG0K4Z15f6rAsm02rw2yL4NfWXgU='

def add_password():
    website = input('Enter Website:')
    username = input('Enter Username:')
    password = input('Enter Password:')
    f = Fernet(key)
    byte_username = bytes(username, 'utf-8')
    byte_password = bytes(password, 'utf-8')
    un = f.encrypt(byte_username).decode()
    pw = f.encrypt(byte_password).decode()

    with open('passwords.txt', 'a') as file:
        file.write(website + '|' + un + '|' + pw + '\n')
        print(f'Successfully saved password for {website}')


def view_passwords():
    with open('passwords.txt','r') as file:
        data = file.readlines()
        for item in data:
            website, username, password = item.rstrip().split('|')
            f = Fernet(key)
            un = f.decrypt(username.encode())
            pw = f.decrypt(password.encode())
            print(website)
            print(un)
            print(pw)


def run_app():
    while True:
        mode = input("Enter a mode (view/add/q): ").lower()
        if mode == 'q':
            break
        elif mode == 'view':
            view_passwords()
        elif mode == 'add':
            add_password()
        else:
            print('invalid input, please retry!')

if __name__ == '__main__':
    run_app()
