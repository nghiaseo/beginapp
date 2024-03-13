import list
import os
import random
import msvcrt
list_task = [
    "Generate IP Address v4",
    "Generate IP Address v6",
    "Generate MAC Address",    
    ]


class GenerateIP:
    def __init__(self):
        task_list = list.List(list_task)
        while True:
            key =  task_list.display()
            self.excute_task(key)
            if key == '0':
                break


    def excute_task(self,key):
        match key:
            case '0':
                os.system('cls')                
            case '1':
                os.system('cls')                
                print("Generate IP Address v4")
                print(self.generate_ipv4())
                print("Press any key to continue...")
                msvcrt.getch()                
            case '2':
                os.system('cls')                
                print("Generate IP Address v6")
                print(self.generate_ipv6())
                print("Press any key to continue...")
                msvcrt.getch()        
            case '3':
                os.system('cls')                
                print("Generate MAC Address")   
                print(self.generate_mac())
                print("Press any key to continue...")
                msvcrt.getch()                    
            case _:
                os.system('cls')                
                print("Invalid key")


    def generate_ipv4(self):
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        return ip
    
    def generate_ipv6(self):
        ip = ":".join(format(random.randint(0, 0xffff), 'x') for _ in range(8))
        return ip.upper()
    
    def generate_mac(self):
        mac = ":".join(format(random.randint(0, 0xff), 'x') for _ in range(6))
        return mac.upper()
            

