# ploxied kardesime selamlar

import os
import time
from colorama import init, Fore

init()

os.system("title DDOS SCANNER by HOWERT")
print(Fore.LIGHTBLUE_EX)
print("DDOS Taranıyor...")
time.sleep(2)
output = os.popen("netstat -an -p tcp").read()

syn_sent_lines = [line.strip() for line in output.splitlines() if "syn sent" in line.lower()]

if syn_sent_lines:
    for line in syn_sent_lines:
        print(Fore.RED)
        print(line)
        print("\n\n\nDDoS Bulundu!")
        time.sleep(10)
else:
    print(Fore.GREEN)
    print("DDoS Bulunamadı.")
    time.sleep(10)


