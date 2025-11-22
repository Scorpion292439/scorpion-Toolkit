
    def Porty(self):
        try:
            r = requests.post("https://panel.porty.tech:443/api.php?", json={"job":"start_login","phone":self.phone}, timeout=6)
            if r.json().get("status") == "success":
                print(f"{Fore.GREEN 
