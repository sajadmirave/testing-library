import requests
from colorama import init,Fore
import sys

init()

colors = {
    "GREEN":Fore.GREEN,
    "RED":Fore.RED,
    "YELLOW":Fore.YELLOW,
    "WHITE":Fore.WHITE,
    "BLUE":Fore.BLUE,
    "CYAN":Fore.CYAN
}
url = "jadi.ir"
res = requests.get(f'https://{url}')

temp1 = f'{colors["WHITE"]}[{colors["CYAN"]}+{colors["WHITE"]}] {colors["CYAN"]} URL: {colors["WHITE"]} {url}{colors["CYAN"]}'
temp2 = f'{colors["WHITE"]}[{colors["CYAN"]}+{colors["WHITE"]}] {colors["CYAN"]} Response: {colors["WHITE"]} {res}{colors["CYAN"]}'
temp3 = f'{colors["WHITE"]}[{colors["CYAN"]}+{colors["WHITE"]}] {colors["CYAN"]} Status Code: {colors["WHITE"]} {res.status_code}'

print(temp1)
print(temp2)
print(temp3)
