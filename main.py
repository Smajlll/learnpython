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
    if data == ['Ahoj, světe!']:
        print("Skvěle! Takhle bude fungovat celý test, budeš upravovat/psát soubory, které pak program zkontroluje. Tak pojďme na to!")
        # Pokud se argument data rovná "Ahoj, světe!", pokračuj na první test :D
        test1()
        # Jinak vypiš notok a pokračuj na funkci error
    else:
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
    input("Stiskni enter pro pokračování")
    time.sleep(1)
    clear()
    print("Tak s těmito znalosti by jsi mohl/a zkusit napsat už svůj první řádek kódu, co ty na to? :D\n")

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
        test2()
    else:
        input("Takhle to asi není správně, koukni se jestli si vše napsal dobře a jestli je první písmenko velké, pak stiskni enter a já zkontroluji tento program znovu.")
        test1kontrola()

def test2():
    clear()
    time.sleep(1)
    print("Část 2. - Proměné\n")
    print("Je to tady, jedna funkce, kterou budeš používat (skoro) ve všech tvých programech.")
    print("Proměné se dělí na 3 základní typy\nint - dokáže do paměti uložit celé číslo, třeba 1\nfloat - float je taky něco s čím můžeš uložit číslo, tentokrát ale i s desetinou čárkou, například 3.14159\n str - také známý jako string, dokáže do paměti uložit text, třeba 'Ahoj, světe'.")
    print("Proměné se mohou hodit pokud potřebuješ udržet nějaké číslo v paměti a poté s ním pracovat, nebo uložit nějaký vztup od uživatele. Dále se taky mohou hodit pokud potřebuješ použít nějaké číslo nebo text použít víckrát :D")
    print("\n")
    print("ahoj = 'Ahoj!'\njedna = 1\n\nprint(ahoj, jedna)\n")
    print("Tohle je ukázka kódu která používá proměné int a str. Je také uložen ve složce testy, tam složka 2 - ukazka1.py")
    print("Můžeš si všimnout, že proměné můžu nastavit na jakoukoliv hodnotu pomocí napsání jeho jména a poté hodnoty.\nMůžeš si také všimnout že python si dokáže o typu proměné rozhodnout sám, takže se o to nemusíš starat, když kód píšeš")
    print("Další věc která zde je k povšimnutí je, že čísla (int a float) nemusím obalovat v závorkách! Text musíme.\nAni jeden vyp však při vypisování pomocí print nemusíme obalovat v závorkách! Všechny proměné oddělujeme čárkou.")
    print("\n")
    print("Teď si zkusíme práci s proměnýma, schválně zkus upravit proměnoj 'jedna' na číslo tři, a koukni se co se stane :D")
    input("Pro pokračování stiskni enter...")

def test2_u1():

    uprava1_2 = subprocess.run(['python ./testy/2/ukazka1.py'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')

    if uprava1_2 == "Ahoj! 3\n":
        print("Koukám že už si tu promněnou upravil, pojďme se kouknout na výpis souboru:\n")
        subprocess.run("python ./testy/2/ukazka1.py", shell=True)
        print("Jak vidíš, vypsal se text 'Ahoj!' a poté číslo 3. Přesně jak má být. Nejlepší na tomto je, že pokud upravíš hodnotu proměné, upraví se hodnota všude kde si jí použil.\nTo si ukážeme v další části :D")
        input("Stiskni enter pro pokračování...")
        test2_2()
    else:
        input("Nevypadá to že by jsi proměnou upravil na číslo 3 :(, zkus to prosím znovu a pak stiskni enter\n")
        test2_u1()

def test2_2():
    clear()
    time.sleep(1)
    snip2 = "jmeno = 'Pepa'\n\nprint(jmeno, ' je 38 let starý')\nprint(jmeno, ' měří 189cm na výšku')\nprint(jmeno, ' váží 68kg')\nprint(jmeno, ' je svobodný')\nprint(jmeno, ' se narodil 1.3.1985')\n"
    print("Jak už jsem říkal, proměné se hodí pokud potřebuješ použít jednu hodnotu na více místech. Zde je ukázka:")
    print(snip2)
    print("Řekněme že chceme nahradit jméno 'Pepa' na jméno 'Karel'. Vyzkoušej to v dokumetu který je uložen ve složce 'testy -> 2 -> ukazka2.py'")
    input("Až změnu dokončís, stiskni enter...")
    test2_u2()

def test2_u2():
    
    uprava2_2 = subprocess.run(['python ./testy/2/ukazka2.py'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
    # print(uprava2_2)

    if uprava2_2 == "Karel je 38 let starý\nKarel měří 189cm na výšku\nKarel váží 68kg\nKarel je svobodný\nKarel se narodil 1.3.1985\n":
        print("Vidíš! Stačilo změnit pouze text v proměné a nemusel si jej měnit 5x!")
        input("Můžeme se posunout dál! Jenom stiskni enter...")
    else:
        print("Karla tu pořád ještě nevidím :(, asi ještě nedorazil. Zkus se po něm podávat, nezapomeň že stringy musí být v uvozovkách a první písmena jmen jsou velká ;D")
        input("Po úpravách stiskni enter...")
        test2_u2()

def test2_3():
    #TODO Část o matematice a floatech (+, -, *, /, %)
    clear()
    time.sleep(1)
    print("Už jsme se podívali na vypisování čísel a textu na obrazovku, ale co takhle matematika? Na tu se podíváme teď!")
    print("V pythonu můžeme používat normální znaménka, jako '+' pro sčítání, '-' pro odčítání, '*' pro násobení a '/' pro dělení")
    print("Dále jsou zde však 3 'speciální' znaménka, '%' - vypíše zbytek při dělení (například 7 % 3 - výsledek = 1), a poté '**', to jsou mocniny' (například 3**2 = 9)")
    print("Poslední je '//', to vypíše pouze podíl, bez žádných čísel za desetinou čárkou.")
    print("Podívej se do souboru ukazka3.py, ve složce testy -> 2, ve které jsou všechny tyto znaménka použíta!")
    input("Až si soubor prohlídneš, stiskni enter a já jej spustím.\n")
    subprocess.run('python ./testy/2/ukazka3.py', shell=True)
    time.sleep(1)



def test2_u3():
    #TODO Část o listech
    pass

def main():
    # print("Hello, world!")
    print("Vítej!")
    print("Dnes se naučíme základy programovacího jazyku 'python', neboj se je to jednoduché, stačí se jen trochu snažit ;D")
    print("Pro pokračování na část 'Obeznámení s Programem' stiskni enter.")
    input("Napsal a vytvořil: Vít Smolík ")
    #create_file_in_home()
    test2_3() # PRO DEBUG, ODSTRANIT NA PRODUCTION

main()

#TODO Skipnutí na jakýkoli test z hl. menu