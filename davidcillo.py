from os import system, name

def clear():
    if name == 'nt': # For Windows
        _ = system('cls')
    else: # For Linux
        _ = system('clear')

def surprise():
    print("Entonces..")
    input("")
    clear()
    print("Ha llegado el momento de elegir..")
    input("")
    print("Ingrese los nombres de aquellas personas con quien le gustaría realizar su sorpresa de cumpleaños.. ")
    print("Digite 'exit' para dejar de añadir personas")
    whileTrue = True
    people = []
    while (whileTrue):
        x = input(">> ")
        if (x != "exit"):
            people += [x]
        else: # x == "exit"
            whileTrue = False
    clear()
    print("Excelente! Entonces, lo acompañarán: ", *people)
    print("\n")
    x = input("Desea conocer su sorpresa? (S/N)")
    if x.upper() == 'S':
        print("De acuerdo! Su sorpresa es..")
    elif x.upper() == 'N'


def happyBirthday():
    print("**************************************")
    print("*                                    *")
    print("*                                    *")
    print("* Feliz cumpleaños pfzzzpfffz manito *")
    print("*                                    *")
    print("*                                    *")
    print("**************************************")
    input("")
    clear()
    surprise()

def displayMenu():
    print("********************************")
    print("*                              *")
    print("*                              *")
    print("* Davidcillo pfzzzpfffz manito *")
    print("*                              *")
    print("*                              *")
    print("********************************")
    input("")
    clear()
    happyBirthday()

def main():
    clear()
    displayMenu()

main()
