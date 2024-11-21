import random

poprawna_odpowiedz = False
while not poprawna_odpowiedz:
    pogoda = random.choice(["Pada", "Nie pada"])
    print("Czy pada? (tak/nie)")
    odpowiedz = input().strip().lower()
    
    if (pogoda == "Pada" and odpowiedz == "tak") or (pogoda == "Nie pada" and odpowiedz == "nie"):
        print("Masz racje,brawo!")
        poprawna_odpowiedz = True
    else:
        print("Nie masz racji, better luck next time.")
        break
