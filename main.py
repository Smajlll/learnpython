from pathlib import Path
import os
import time

#TODO Upravit funkci read_file aby brala argument s path pro soubor

def clear():
    # Tato funkce vymaže obrazovku, pokud zjistí, že os type je 'nt', neboli windows, vyvolá příkaz "cls", na UNIX a UNIX-like systémech vyvolá příkaz 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file():
        # Otevře soubor
    myfile = open('ahoj.txt')
        # Přečte soubor
    data = myfile.readlines()
        # Zavře soubor
    myfile.close()

        #print(data)

        # Předá funkci na ověření informací argument "data", který je vyčten ze souboru ahoj.txt
    ok_notok(data)
        
def error():
        # Pokud se požadovaný text v souboru nenajde, je zavolána tato funkce
    input("Tohle se nepovedlo, zkus to znovu, pak stiskni enter.")
        # Znovu volání funkce read_file která znovu překontroluje tento soubor
    read_file()

def ok_notok(data):
        # Pokud se "data" rovná cscs, vypiš ok a zkonči
    if data == ['cscs']:
        print("ok")
        # Pokud se argument data rovná "Ahoj, světe!", pokračuj na první test :D
        test1()
        # Jinak vypiš notok a pokračuj na funkci error
    else:
        print("notok")
        error()

def create_file_in_home():
    print("Tak tě zde ješte jednou vítám na naší interaktivní prohlídce pythonu, pro lepší zážitek, doporučuji dát program do své vlastní složky, třeba v Dokumentech ;D")
    
    # Pokud soubor ahoj.txt ve složce s programem neexistuje, vytvoří jej program a dá si dostatečná oprávnění k zápisu/čtení

    print("Pro obeznámení tě s programem ti nyní vytvořím ve složce kde je uložen soubor 'ahoj.txt', kde si vyzkoušíš jak tento program bude fungovat")
    # Uspí program na 1 sekundu, pak vytvoří soubor
    time.sleep(1)
    myfile = Path('ahoj.txt')
    myfile.touch(exist_ok=True)
    f = open(myfile)

    check_file_content()

def check_file_content():
    print("Nyní když máš soubor 'ahoj.txt', přidej do něj text 'ahoj' a pak stiskni Enter")
    input("Čekám na Enter...")
    read_file()


def test1():

    clear()
    print("Dobře, když už jsi seznámen s tím jak bude tento program fungovat, můžeme se vrhnout do učení!")
    #TODO Dodělat čtení souboru hw.py (hello world) a jeho spuštění
    
def main():
    # print("Hello, world!")
    print("Vítej!")
    print("Dnes se naučíme základy programovacího jazyku 'python', neboj se je to jednoduché, stačí se jen trochu snažit ;D")
    print("Pro pokračování na část 'Obeznámení s Programem' stiskni enter.")
    input("Napsal a vytvořil: Vít Smolík ")
    create_file_in_home()
    

main()