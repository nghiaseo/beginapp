import re
import os
import msvcrt

class ExtractURL:
    def __init__(self):
        
                os.system('cls')                
                print("Extract URL")
                text = input("Enter url or Enter to back: ")
                print(self.extract_url(text))
                print("Press any key to continue...")
                msvcrt.getch()
        
    def extract_url(self, text):                
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = re.findall(url_pattern, text)
        if(len(urls) != 1):
            return "No URL found"
        else:            
            protocol = re.findall(r'(http[s]?://)', urls[0])
            domain = re.findall(r'(?:http[s]?://)?([a-zA-Z0-9.-]+)', urls[0])            
            path = re.findall(r'(?:http[s]?://)?(?:[a-zA-Z0-9.-]+)?(?:/[a-zA-Z0-9.-]+)?(/.*)', urls[0])
            path[0] = path[0].replace('/',"")
            if(path[0] == domain[0]):
                path[0] = 'index.html'
            return "Protocol: "+(protocol[0].replace("://",""))+"\nDomain: "+domain[0]+"\nFile: "+path[0]