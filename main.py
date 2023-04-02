#!/usr/bin/python3
import os
import random  # pip install r-requirements.txt
from luhn import verify
import requests
import sys
import time
import string as strg
from colorama import init, Fore
import ctypes

headers = {'User-Agent': 'TikTok 17.4.0 rv:17yellow_to_red14 (iPhone; iOS 13.6.1; sv_SE) Cronet',
           'Connection': 'keep-alive'
    ,},

timeout = 60


def issue():
    os.system('cls')
    print(Fore.LIGHTMAGENTA_EX + '''
                  ▄████  ██▓  █████▒▄▄▄█████▓ ▄████▄   ▄▄▄       ██▀███  ▓█████▄   ██████    
                  ██▒ ▀█▒▓██▒▓██   ▒ ▓  ██▒ ▓▒▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▒██    ▒    
                  ▒██░▄▄▄░▒██▒▒████ ░ ▒ ▓██░ ▒░▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌░ ▓██▄      
                  ░▓█  ██▓░██░░▓█▒  ░ ░ ▓██▓ ░ ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌  ▒   ██▒   
                  ░▒▓███▀▒░██░░▒█░      ▒██▒ ░ ▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ▒██████▒▒   
                   ░▒   ▒ ░▓   ▒ ░      ▒ ░░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░   
                   ░   ░  ▒ ░ ░          ░      ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░   
                   ░ ░   ░  ▒ ░ ░ ░      ░      ░          ░   ▒     ░░   ░  ░ ░  ░ ░  ░  ░     
                       ░  ░                   ░ ░            ░  ░   ░        ░          ░     
                             ░                            ░                  
                                       Made By Brizzzzzer2and#0071
                -----------------------Welcome In The Gen Giftcards--------------------------
''')

    print(Fore.RESET + 'Gen Room:\n',
          Fore.GREEN + '\n[1]- PSN Card\n[2]- Playstore\n[3]- Roblox\n[4]- Amazon\n[5]' '- Netflix\n[6]-' ' xBox\n[7]- Itunes\n[8]- Nitro-Gen\n[9]- Tiktok\n[10]- Exit')
    gen = input('Please enter a number :')
    os.system('cls')
    if gen == '1':
        psn()
        os.system('cls')
    elif gen == '2':
        playstore()
        os.system('cls')
    elif gen == '3':
        roblox()
        os.system('cls')
    elif gen == '4':
        amazon()
        os.system('cls')
    elif gen == '5':
        netflix()
        os.system('cls')
    elif gen == '6':
        xBox()
        os.system('cls')
    elif gen == '7':
        Itunes()
        os.system('cls')
    elif gen == '8':
        nitro_gen()
        os.system('cls')
    elif gen =='9':
        tiktok()
        os.system('cls')
    elif gen =='10':
        sys.exit()
    else:
        print('Enter a Valid Number !')


os.system('cls')
init(convert=True and False)
ctypes.windll.kernel32.SetConsoleTitleW('Gen Giftcard made by Brizzr')
ctr = print(Fore.LIGHTCYAN_EX + '''
 ▄▄▄▄    ██▀███   ██▓▒███████▒▒███████▒ ██▀███   ▄▄▄       ███▄    █ ▓█████▄    
▓█████▄ ▓██ ▒ ██▒▓██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌   
▒██▒ ▄██▓██ ░▄█ ▒▒██▒░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌   
▒██░█▀  ▒██▀▀█▄  ░██░  ▄▀▒   ░  ▄▀▒   ░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌   
░▓█  ▀█▓░██▓ ▒██▒░██░▒███████▒▒███████▒░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓    
░▒▓███▀▒░ ▒▓ ░▒▓░░▓  ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒    
▒░▒   ░   ░▒ ░ ▒░ ▒ ░░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒    
 ░    ░   ░░   ░  ▒ ░░ ░ ░ ░ ░░ ░ ░ ░ ░  ░░   ░   ░   ▒      ░   ░ ░  ░ ░  ░    
 ░         ░      ░    ░ ░      ░ ░       ░           ░  ░         ░    ░       
      ░              ░        ░                                       ░         
''')

time.sleep(0.9)
print(Fore.RED + 'Made by Brizzzzzer2and#0071')
time.sleep(0.8)

# debut
print(Fore.RED + 'Welcome In The Gen Giftcards !')
time.sleep(0.8)
character = strg.ascii_letters + strg.digits

# fonction
def main():
    print(Fore.GREEN + '[1]- PSN Card\n''[2]- Playstore\n[3]- Roblox\n[4]-' ''  ' Amazon\n[5]-'' Netflix\n[6]- xBox\n[7]- '  'Itunes\n[8]- Nitro-Gen\n[9]- Tiktok Gen\n[10]- Exit')

    gen = input('Please enter a number :')
    os.system('cls')
    if gen == '1':
        psn()
    elif gen == '2':
        os.system('cls')
        playstore()
    elif gen == '3':
        os.system('cls')
        roblox()
    elif gen == '4':
        os.system('cls')
        amazon()
    elif gen == '5':
        os.system('cls')
        netflix()
    elif gen == '6':
        os.system('cls')
        xBox()
    elif gen == '7':
        os.system('cls')
        Itunes()
    elif gen == '8':
        os.system('cls')
        nitro_gen()
    elif gen =='9':
        os.system('cls')
        tiktok()
    elif gen =='10':
        sys.exit()
    else:
        print('Veuillez rentrer un numero correct !')


def psn():
    amount = input('How many codes do you want to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------PSN CARD-------------\n')
    try:
        for gen_psn in range(amount):
            psn_card = "".join(random.choices(character, k=12))
            url_code_psn = "https://web.np.playstation.com/api/graphql/v1/transact/wallets/vouchers/" + psn_card
            status = requests.get(url_code_psn)
            if status.status_code == 403:
                print(f'{Fore.GREEN} Valid |' + psn_card)
                break
            else:
                print(f'{Fore.RED} Invalid |' f'{Fore.RESET} {psn_card} ')
    except:
        pass
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


def playstore():
    amount = input('How many codes do you want to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------PLAYSTORE CARD-------------\n')
    try:
        for play_store in range(amount):
            play_store = ''.join(random.choices(character, k=20))
            time.sleep(0.1)
            print(play_store)
    except:
        pass
    time.sleep(0.4)
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


def roblox():
    amount = input('How many codes do you want to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------ROBLOX CARD-------------\n')
    try:
        for roblox in range(amount):
            roblox = ''.join(random.choices(strg.digits, k=10))
            time.sleep(0.1)
            print(roblox)
    except:
        pass
    time.sleep(0.4)
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


def amazon():
    amount =input('How many code do you want to gen ?:')
    amount = int(amount)
    os.system('cls')
    print('------------AMAZON CARD-------------\n')
    for amazo in range(amount):
        amazo = ('').join(random.choices(strg.digits, k=8))
        if amazo == verify:
            print(f"{Fore.GREEN} Valid | "f'{Fore.RESET}{amazo}')
        else:
            print(f"{Fore.RED} Invalid |"f'{Fore.RESET}{amazo}')
            time.sleep(1)

    time.sleep(0.4)
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


def netflix():
    amount = input('How many codes do you want to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------NETFLIX CARD-------------\n')
    try:
        for netf in range(amount):
            netf = ''.join(random.choices(character, k=11))
            time.sleep(0.1)
            print(netf)
    except:
        pass
    time.sleep(0.4)
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


def xBox():
    amount = input('How many codes do you want to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------XBOX CARD-------------\n')
    try:
        for xbox in range(amount):
            xbox = ''.join(random.choices(character, k=25))
            xbox = xbox.upper()
            time.sleep(0.1)
            print(xbox)
    except:
        pass
    time.sleep(0.4)
    print(Fore.RESET + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


def Itunes():
    amount = input('How many codes do you want to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------ITUNES CARD-------------\n')
    try:
        for itunes in range(amount):
            itunes = ''.join(random.choices(character, k=16))
            itunes = itunes.upper()
            time.sleep(0.1)
            print(itunes)
    except:
        pass
    time.sleep(0.4)
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


def nitro_gen():
    amount = input('How many codes do you want to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------NITRO GEN-------------\n')
    try:
        for nitro in range(amount):
            nitro = ''.join(random.choices(character, k=16))            #soon...With proxies
            url = "https://discord.gift/" + nitro
            chkr = requests.get(url)
            if chkr.status_code == '200':
                 mdd= print(f'{Fore.GREEN} Valid |'F'{Fore.RESET}' + url)
                 break
            else:
                 mda =print(f'{Fore.RED} Invalid |'f'{Fore.RESET}' + url)
            with open('nitro.txt', 'a+') as file:
                file.write(url)
                file.write('\n')
                file.close()
        ctypes.windll.kernel32.SetConsoleTitleW('Valid |' + str(len(mdd)).append, 'Invalid | ' + str(len(mda)).append)
    except:
        pass
    time.sleep(0.4)
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()

def tiktok():
    amount = input('How many account do you to generate ? :')
    amount = int(amount)
    os.system('cls')
    print('------------TIKTOK ACCOUNT-------------\n')
    try:
        for tik in range(amount):
            tik = ''.join(random.choices(character, k= 6))
            url ="https://www.tiktok.com/@" +tik
            tok = requests.Session()
            check = tok.get(url, timeout =60)
            chk = check.status_code
            if chk ==404:
                 print(f'{Fore.GREEN} Valid |'f'{Fore.RESET}'+url)
            elif chk == 429:
                print(f'{Fore.YELLOW} Too Many Requests | 'f'{Fore.RESET}'+url)
            else:
                print(f'{Fore.RED} Invalid |'f'{Fore.RESET}' +url)
    except:
        pass
    time.sleep(0.4)
    print(Fore.WHITE + '\n ------Generating Completed------ !')
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    return issue()


if __name__ == '__main__':
    main()