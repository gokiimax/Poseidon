import os
import fade
from colorama import Fore

# Clear the console to get better view :)
if os.name == "nt":        # Check if the system is windows
    os.system("cls")
else:
    os.system("clear")     # All the other systems 

# ========================================================================================================================================================= #

banner = """
    ____                  _     __          
   / __ \____  ________  (_)___/ /___  ____ 
  / /_/ / __ \/ ___/ _ \/ / __  / __ \/ __ \\
 / ____/ /_/ (__  )  __/ / /_/ / /_/ / / / /
/_/    \____/____/\___/_/\__,_/\____/_/ /_/ 
>> Made by gokiimax      
>> https://github.com/gokiimax
"""
faded_banner = fade.purplepink(banner)
print(faded_banner)

info = """
╭─────────────────────────────────────╮
│ Poseidon v1.0                       │
│ Developed by gokiimax               │
│ !! For Educational Purposes Only !! │
╰─────────────────────────────────────╯
"""
faded_info = fade.purplepink(info)
print(faded_info)

# ========================================================================================================================================================= #

def encrypt(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key", "wb") as key_out:
        key_out.write(key)
        encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)

# ========================================================================================================================================================= #

def decrypt(filename, key):
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open("d_" + filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)

# ========================================================================================================================================================= #

options = f"""{Fore.LIGHTBLUE_EX}
[1] Encrypt
[2] Decrypt

[99] Exit 
"""
print(options)

# ========================================================================================================================================================= #

option = int(input(f"{Fore.LIGHTBLUE_EX}╭── {Fore.WHITE}[{Fore.LIGHTBLUE_EX}Poseidon@home{Fore.WHITE}]\n{Fore.LIGHTBLUE_EX}╰──────# {Fore.RESET}"))

if option == 1:
    file = input("|-~> File: ")
    encrypt(filename=file)
    print("Your file got successfully encrypted!")

# ========================================================================================================================================================= #

elif option == 2:
    file = input("|-~> File: ")
    key = input("|-~> Key: ")
    decrypt(filename=file, key=key)
    print("Your file got successfully decrypted!")

# ========================================================================================================================================================= #

elif option == 99:
    exit(-1)
        
# ========================================================================================================================================================= #