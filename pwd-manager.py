master_pwd = input("What is the Master password? ")


def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + " " + pwd )


while True:
    mode = input("Would you like to add a new password or view existing ones (view,add) ? press q to quit ?").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue