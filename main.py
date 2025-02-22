import requests as req
from colorama import Fore
import os
import asyncio

red = Fore.RED
blue = Fore.BLUE

r = Fore.RESET
green = Fore.GREEN

async def Info():
    os.system('cls')
    print(blue + r"""
.___        _____       
|   | _____/ ____\____  
|   |/    \   __\/  _ \ 
|   |   |  \  | (  <_> )
|___|___|  /__|  \____/ 
         \/             
""")
    webhook = input(f'{red}[?] WEBHOOK URL :{r} ')
    res = req.get(url=webhook)
    json = res.json()

    webhookid = json['id']

    print(f"""\n

    Guild ID : {json['guild_id']}

    Name : {json['name']}

    Avatar : https://cdn.discordapp.com/avatars/{webhookid}/{json['avatar']}.png

""")

    input(f'\n\n{blue}[?] Press enter to continue...')



async def Checker():   
    os.system('cls')
    print(blue + r"""
_________ .__                   __                 
\_   ___ \|  |__   ____   ____ |  | __ ___________ 
/    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \
\     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
 \______  /___|  /\___  >\___  >__|_ \\___  >__|   
        \/     \/     \/     \/     \/    \/       

""")
    webhook = input(f'{red}[?] WEBHOOK URL :{r} ')
    res = req.get(url=webhook)
    if res.status_code == 200:
        print(f'\n\n{green}[+] WEBHOOK IS VALID')
    else:
        print(f'\n\n{red}[-] Error {res.status_code} : {res.text}')
    
    input(f'\n\n{blue}[?] Press enter to continue...')


async def Delete():
    os.system('cls')
    print(red + r"""
________         .__          __                
\______ \   ____ |  |   _____/  |_  ___________ 
 |    |  \_/ __ \|  | _/ __ \   __\/ __ \_  __ \
 |    `   \  ___/|  |_\  ___/|  | \  ___/|  | \/
/_______  /\___  >____/\___  >__|  \___  >__|   
        \/     \/          \/          \/       

""")
    webhook = input(f'{red}[?] WEBHOOK URL :{r} ')
    res = req.delete(url=webhook)
    if res.status_code == 204:
        print(f'\n\n{green}[+] WEBHOOK DELETED SUCCESSFULLY')
    else:
        print(f'{red}[-] Error {res.status_code} : {res.text}')

    input(f'\n\n{blue}[?] Press enter to continue...')


async def Spam():
    os.system('cls')
    print(blue + r"""
  _________                                          
 /   _____/__________    _____   _____   ___________ 
 \_____  \\____ \__  \  /     \ /     \_/ __ \_  __ \
 /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/
/_______  /   __(____  /__|_|  /__|_|  /\___  >__|   
        \/|__|       \/      \/      \/     \/       
          
""")
    webhook = input(f'{red}[?] WEBHOOK URL :{r} ')
    message = input(f'{red}[?] MESSAGE :{r} ')
    times = input(f'{red}[?] TIMES(ex:10) :{r} ')
    times = int(times)
    data = {'content':message}

    for i in range(times):
            
                res = req.post(url=webhook,data=data)
                if res.status_code == 204:
                    print(f'{green}[+] MESSAGE SENT SUCCESSFULLY : {message}')
                else:
                    print(f'{red}[-] Error {res.status_code} : {res.text}')
    
    print(f'\n\n{green}[+] SPAMMING COMPLETED')

    input(f'\n\n{blue}[?] Press enter to continue...')


async def menu():
    while True:
        os.system('cls')
        print(rf"""

{red} __      __      ___.   .__                   __     
/  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __ 
\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / 
 \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  
  \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \ 
       \/       \/    \/     \/                   \/ 
                                                        
                                             {blue}____  __.__.__  .__                
                                            |    |/ _|__|  | |  |   ___________ 
                                            |      < |  |  | |  | _/ __ \_  __ \
                                            |    |  \|  |  |_|  |_\  ___/|  | \/
                                            |____|__ \__|____/____/\___  >__|   
                                                    \/                 \/       
            
    {red}By c1a1337                  https://github.com/c1a1337/WebhookKiller            https://discord.gg/ulq


    {blue}1. Delete webhook       2. Spam webhook

    3. Check webhook        4. Webhook info
    """)
        
        choice = input(f'{red}[?] Choice : {r}')

        if choice == '1':
            await Delete()


        elif choice == '2':
            await Spam()
        
        elif choice == '3':
            await Checker()

        elif choice =='4':
            await Info()
            
        
        else:
            print(f'{red}[-] Invalid choice')
            continue
        
        


asyncio.run(menu())

            
            


