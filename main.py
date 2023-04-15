from pathlib import Path
import os
import time
import subprocess

def clear():
    # Tato funkce vymaže obrazovku, pokud zjistí, že os type je 'nt', neboli windows, vyvolá příkaz "cls", na UNIX a UNIX-like systémech vyvolá příkaz 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(file):
        # Otevře soubor
    myfile = open(file)
        # Přečte soubor
    data = myfile.readlines()
        # Zavře soubor
    myfile.close()

        #print(data) - použito pro debug, vypíše argument data který předává dál do konzole. Default = okomentováno

        # Předá funkci na ověření informací argument "data", který je vyčten ze souboru ahoj.txt
    ok_notok(data)
        
def error():
        # Pokud se požadovaný text v souboru nenajde, je zavolána tato funkce
    input("Tohle se nepovedlo, zkus to znovu, pak stiskni enter.")
        # Znovu volání funkce read_file která znovu překontroluje tento soubor
    read_file('ahoj.txt')

def ok_notok(data):
        # Pokud se "data" rovná 'Ahoj, světe!', vypiš ok a zkonči
    if data == ['Ahoj. světe!']:
        print("Skvěle! Takhle bude fungovat celý test, budeš upravovat/psát soubory, které pak program zkontroluje. Tak pojďme na to!")
        # Pokud se argument data rovná "Ahoj, světe!", pokračuj na první test :D
        test1()
        # Jinak vypiš notok a pokračuj na funkci error
    else:
        print("notok")
        error()

def create_file_in_home():
    clear()
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
    print("Nyní když máš soubor 'ahoj.txt', přidej do něj text 'Ahoj, světe' a pak stiskni Enter")
    input("Čekám na Enter...")
    read_file('ahoj.txt')


def test1():
    # Test na print a texty

    clear()

    ahojsvete = "print('Ahoj, světe!')"
    cmd_str = "python ./ahoj.py"

    print("Dobře, když už jsi seznámen s tím jak bude tento program fungovat, můžeme se vrhnout do učení! \n")
    #TODO Dodělat čtení souboru hw.py (hello world) a jeho spuštění
    
    print("Takže, na začátku každého projektu, začátku každého učení nového programovácího jazyka, se setkáme s 'Hello, world', v češtině 'Ahoj světe'")
    print("Jeden takový program ti teď vytvořím a pak jej spolu zkusíme zpustit!")
    
    hwfile = Path('ahoj.py')
    hwfile.touch(exist_ok=True)
    hw = open(hwfile, "w")
    hw.writelines(ahojsvete)
    hw.close()

    input("Až budeš připraven, stiskni enter a já sputím program, který do konzole vypíše 'Ahoj, světe!' \n")

    clear()
    print("Spouštím program \n")
    time.sleep(1)
    subprocess.run(cmd_str, shell=True)
    time.sleep(1)
    print("\n")
    print("Nyní si projdeme co tento program dělá:")
    print("Kód programu který jsi práve spustil je tento:")
    print("     print('Ahoj, světe!')\n")
    print("Můžeš si všimnou že používáme funkci 'print' - ta v pythonu umožňuje vypsat text na obrazovku. \nDále si můžeš všimnout závorky ve které jsou uvozovky a text. \nTo že jsme text obalili v závorkách říka pythonu že doopravdy, bude vypisovat text.")
    print("\n")
    time.sleep(1)
    clear()
    print("Tak s těmito znalosti by jsi mohl/a zkusit napsat už svůj první řádek kódu, co ty na to? Myslím si že ano :D\n")

    test1 = Path("./testy/1/test1.py")
    test1.touch(exist_ok=True)

    print("Ve složce testy máš složku 1, v ní je test1.py, napiš do něj část kódu která mu umožní vypsat 'Dobrý den' ")
    input("Až to uděláš, stiskni enter a já to zkontroluji ;D")
    test1kontrola()

def test1kontrola():

    #testThis = 
    result = subprocess.run(['python ./testy/1/test1.py'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')

    # print(result) - Pro debugování nefukční proměné result :D

    if result == "Dobrý den\n":
        print("Tak to se povedlo, si šikovný/á. Myslím že můžeme přejít na část číslo 2!")
        input("Až budeš připraven, stiskni enter")
        # TODO udělat druhý test
    else:
        input("Takhle to asi není správně, koukni se jestli si vše napsal dobře a jestli je první písmenko velké, pak stiskni enter a já zkontroluji tento program znovu.")
        test1kontrola()

def test2():
    clear()
    time.sleep(1)
    

def main():
    # print("Hello, world!")
    print("Vítej!")
    print("Dnes se naučíme základy programovacího jazyku 'python', neboj se je to jednoduché, stačí se jen trochu snažit ;D")
    print("Pro pokračování na část 'Obeznámení s Programem' stiskni enter.")
    input("Napsal a vytvořil: Vít Smolík ")
    create_file_in_home()
    

main()