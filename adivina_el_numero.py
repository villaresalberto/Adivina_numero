#!/usr/bin/ env python3
import random

numero_secreto = random.randint(1, 10)

intento = int(input("\n[+] Adivina el número del 1 al 10: "))
print(f"\n[+] Tú escribiste el número: {intento}")

if intento == numero_secreto:
    print(f"\n[+] Bravo, has acertado. El número secreto es: {numero_secreto}")
    exit()
    
else:
    print(f"\n[!] Vaya...Parece que te has equivocado. Vamos a probar de nuevo.")

if numero_secreto % 2 == 1:
    print(f"\n[+] Pista: el número secreto es impar")
elif numero_secreto % 2 == 0:
    print(f"\n[+] Pista el número secreto es par")

intento = int(input(f"\n[+]Adivina el número del 1 al 10: "))
print(f"\n[+] Tú escribiste el número: {intento}")

if intento == numero_secreto:
    print(f"\n[+] Bravo, has acertado. El número secreto es: {numero_secreto}")

else:
    print(f"\n[!] Vaya...Has perdido. La vida puede dar segundas, pero no terceras oportunidades ;)") 
    print(f"\n[+] El número secreto es: {numero_secreto}")
