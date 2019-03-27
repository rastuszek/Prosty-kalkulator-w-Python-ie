import math
from tkinter import *                           #Zaimportowanie  biblioteki umożliwiającej tworzenie interfejsu graficznego dla Pythona opartej na bibliotece Tk 

Pamiec = 0
Suma = 0                                        #Przy uruchomieniu programu nadanie obiektowi Suma wartośc "0", aby przy włączeniu programu taka wartosc byla przechowywana w pamieci i taka tez wyświetlala się. 
Operator = None                                 #Przy uruchomieniu programu ustawienie żadnego operatora. Ustawienie flagi operator na wartosc none, to to samo co null w innych jezykach.

def Kasuj():                                    #Deklaracja funkcji rodzaju DEF o nazwie "kasuj", która uruchamia się tylko wtedy, kiedy jest wywołana. W bloku poniżej znajduje się to co wykonuje.
    global wyświetlaczStr,Suma,Operator         #Słowo kluczowe "global" pozwala na zmiane w danym bloku zmiennej, która występuje również poza nim.
    wyświetlaczStr.set("0")                     #Tutaj ustawienie wyświetlania cyfry "0".
    Suma = 0                                    #Nadanie zmiennej wartości "0", aby w przechowywanej pamięci program również miał wartość 0.
    Operator = None                             #Dzięki temu program usunie z pamięci ostatnio wykorzystywany operator. Zwykle kasowanie zmiennych uzywanych do obliczen

def Cyfra0():                                   #Tak jak powyżej.
    global wyświetlaczStr                       #Tak jak powyżej.
    s = wyświetlaczStr.get()                    #Nadanie zmiennej s wartosci, która znajduję się w poniższej funkcji.
    if(len(s) < 10 and s != '0'):               #Jeśli długość zmiennej s, która jest stringiem i jest mniejsza od 10 oraz nie jest równa 0.
        s = s + '0'                             #To jest równe sumie wyświetlanej plus zero.
        wyświetlaczStr.set(s)                   #Ustawienie wartości zmiennej, która została określona przez powyższą funkcję i jej wyswietlenie. Osobna metoda dla cyfry zero, poniewaz zwykla metoda cyfra nie mialaby zastosowania z tego wzgledu, ze instrukcje watunkowe w innyh metodach opierajace sie o zero wlasnie.

def Cyfra(c):                                   #Deklaracja funkcji DEF, ktora przybiera wartosc nacisnietego przycisku.
    global wyświetlaczStr                       #Global pozwala na zmiane wczesniej zadeklarowanej zmienej.
    s = wyświetlaczStr.get()                    #Nabieranie zmiennej "s" wartosci, ktora opisuje ponizsza funkcja. 
    if(len(s) < 10):                            #Jesli dlugosc "s" jest mniejsza od 10 to:
        if(s == '0'):                           #Jesli dlugosc "s" jest rowne 0 to:
            s = c                               #Wartosc "s" jest tym samym co wartosc "c".
        else:                                   #W przeciwnym wypadku:
            s = s + c                           #Wartosc s = wartosci s plus c.
        wyświetlaczStr.set(s)                   #Na wyswietlaczu pojawia sie wartosc zmiennej "s". Metoda ustawiajaca na wyswietlaczu wcisniete cyfry.

def Plus():                                     #Deklaracja funkcji dodawania.
    global wyświetlaczStr,Suma,Operator         #Zmienne, ktorych wartosc zmieni sie globalnie.
    s = wyświetlaczStr.get()                    #Zmienna "s" bedzie miala wartosc ponizszej funkcji:
    if(s != '0'):                               #Jesli "s" nie jest rowne 0 to:
        Suma = int(s)                           #Zmienna suma nabiera wartosc stringa zmiennej s na wartosc liczbe calkowita.
        Operator = "+"                          #Ustawienie zmiennej operator jako dodawania.
    wyświetlaczStr.set(str("0"))                #Na wyswietlaczu pojawia sie wartosc 0, poniewaz po wcisnieciu plusa musi sie wyzerowac wartosc na wyswietlaczu, tak jak robi  to kalkulator.

def RównaSię():
    global wyświetlaczStr, Suma,Operator        #Metoda sprawdza jaki znak byl wcisniety ostatnio, w oparciu o zmienna operator i wykonuje dzialanie.
    s = wyświetlaczStr.get()                    #
    if (Operator == "+"):                       #
        Suma = Suma + int(s)                    #
    elif (Operator == "-"):                     #
        Suma = Suma - int(s)                    #
    elif (Operator == "*"):                     #
        Suma = Suma * int(s)                    #
    elif (Operator == "/"):                     #
        Suma = Suma / int(s)                    #
    elif (Operator == "M+"):
        Suma = Pamiec + Suma + int(s)
    wyświetlaczStr.set(str(Suma))               #

def Minus():                                    #
    global wyświetlaczStr, Suma,Operator        #Po wcisnieciu minusa zmienna operator jest ustawiana na "-" dzieki temu metoda rowna sie jest w stanie rozpoznac jaka operacja powinna byc wykonana
    s = wyświetlaczStr.get()                    #
    if(s != '0'):                               #
        Suma = int(s)                           #
        Operator = "-"                          #
    wyświetlaczStr.set(str("0"))                #

def Iloczyn():
    global wyświetlaczStr, Suma,Operator        #
    s = wyświetlaczStr.get()                    #Tak jak wyzej.
    if(s != '0'):                               #
        Suma = int(s)                           #
        Operator = "*"                          #
    wyświetlaczStr.set(str("0"))                #

def Iloraz():                                   #Tak jak wyzej.
    global wyświetlaczStr, Suma,Operator        #
    s = wyświetlaczStr.get()                    #
    if(s != '0'):                               #
        Suma = int(s)                           #
        Operator = "/"                          #
    wyświetlaczStr.set(str("0"))                #

def Pierwiastek():                              #
    global wyświetlaczStr, Suma,Operator        #
    s = wyświetlaczStr.get()                    #
    if(s != '0'):                               #
        Suma = int(s)                           #
        Operator = "√"                          #
    wyświetlaczStr.set(str(s))
    Suma = int(math.sqrt(int(s)))
    wyświetlaczStr.set(str(Suma)) 

def PamiecPlus():                               #
    global wyświetlaczStr, Pamiec
    Pamiec = Pamiec + int(wyświetlaczStr.get())
    

def PamiecMinus():
    global wyświetlaczStr, Pamiec
    Pamiec = Pamiec - int(wyświetlaczStr.get())

def PamiecCzysc():
    global Pamiec
    Pamiec = 0

def PamiecWyswietl():
    global wyświetlaczStr, Pamiec
    wyświetlaczStr.set(str(Pamiec))
    
    

def Cyfra1():                       #Tutaj deklaracje funkcji, które działają z funkcją 'Cyfra', przyciskiem i nadają jej określoną w nawiasie wartość.
    Cyfra('1')

def Cyfra2():
    Cyfra('2')

def Cyfra3():
    Cyfra('3')

def Cyfra4():
    Cyfra('4')

def Cyfra5():
    Cyfra('5')

def Cyfra6():
    Cyfra('6')

def Cyfra7():
    Cyfra('7')

def Cyfra8():
    Cyfra('8')

def Cyfra9():
    Cyfra('9')

okno = Tk()                                                                     #Wywołanie okna graficznego, opartego na bibliotece Tk.
wyświetlaczStr = StringVar()                                                    #Dzieki temu na wyswietlaczu beda sie pojawiac obiekty, ktore w pamieci beda jako zmienne rodzaju string.                                                                        
wyświetlaczStr.set("0")                                                         #Ustawienie wartosci "0" na wyswietlaczu na poczatku.
wyświetlacz = Entry(okno, width=10, font=("Courier New","12", "bold"),textvariable=wyświetlaczStr,justify=RIGHT) #Tutaj stylizacja wyswietlacza, jego wielkosc, czcionka, miejsce wyswietlania napisu.
wyświetlacz.grid(row=0,columnspan=4)                                            #Ustawienie polozenia i siatki przyciskow.

cyfra7 = Button(okno, text="7",command=Cyfra7)                                  #Ponizej przypisanie do kazdego przycisku danej cyfry, gdzie ma sie znajdowac i jakie polecenie ma wywolywac jego przycisniecie.                              
cyfra7.grid(row=1,column=0)                                                     #Czyli jaka wartosci ma posiadac.

cyfra8 = Button(okno, text="8",command=Cyfra8)                                  #Analogicznie jest stworzony kazdy przycisk.
cyfra8.grid(row=1,column=1)

cyfra9 = Button(okno, text="9",command=Cyfra9)
cyfra9.grid(row=1,column=2)

cyfra4 = Button(okno, text="4",command=Cyfra4)
cyfra4.grid(row=2,column=0)

cyfra5 = Button(okno, text="5",command=Cyfra5)
cyfra5.grid(row=2,column=1)

cyfra6 = Button(okno, text="6",command=Cyfra6)
cyfra6.grid(row=2,column=2)

cyfra1 = Button(okno, text="1",command=Cyfra1)
cyfra1.grid(row=3,column=0)

cyfra2 = Button(okno, text="2",command=Cyfra2)
cyfra2.grid(row=3,column=1)

cyfra3 = Button(okno, text="3",command=Cyfra3)
cyfra3.grid(row=3,column=2)

cyfra0 = Button(okno, text="0",command=Cyfra0)
cyfra0.grid(row=4,column=1)

plus = Button(okno, text="+",command=Plus)
plus.grid(row=4,column=3)

równasię = Button(okno, text="=",command=RównaSię)
równasię.grid(row=4,column=2)

kasuj = Button(okno, text="C",command=Kasuj)
kasuj.grid(row=4,column=0)

minus = Button(okno, text="-",command=Minus)
minus.grid(row=3,column=3)

pomnoz = Button(okno, text="*", command=Iloczyn)
pomnoz.grid(row=2,column=3)

podziel = Button(okno, text="/", command=Iloraz)
podziel.grid(row=1,column=3)

pierwiastek = Button(okno, text="√", command=Pierwiastek)
pierwiastek.grid(row=5,column=0)

PamiecPlus = Button(okno, text="M+", command=PamiecPlus)
PamiecPlus.grid(row=5,column=1)

PamiecMinus = Button(okno, text="M-", command=PamiecMinus)
PamiecMinus.grid(row=5,column=2)

PamiecCzysc = Button(okno, text="MC", command=PamiecCzysc)
PamiecCzysc.grid(row=5,column=3)

PamiecWyswietl = Button(okno, text="MW", command=PamiecWyswietl)
PamiecWyswietl.grid(row=5,column=4)


okno.mainloop()                                     #Uruchomienie funkcji mainloop() - czyli głównej pętli, która będzie "napędzać" cały program.

#W mainloop() wykonują się w pętli takie rzeczy jak pobieranie informacji o myszy i klawiaturze, przekazywanie tego do obiektów w oknie, obsługa zdarzeń,
#wywoływanie funkcji przypisanych do menu i przycisków w oknie - tak więc nasze funkcje nie mogą się wykonywać w nieskończoność (nie powinny mieć
#nieskończonych pętli while True lub używać time.sleep()) bo inaczej reszta zadań nie będzie wykonywanych i okno przestanie reagować czyli potocznie "zawiśnie".
