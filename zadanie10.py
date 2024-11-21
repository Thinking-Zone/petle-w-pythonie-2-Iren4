#znajdź pierwszą nieparzystą liczbe podzielną na 3 w przedziale liczb o 1 do 100
for liczba in range(1, 101):
    if liczba % 2 != 0 and liczba % 3 == 0:
        print("Pierwsza nieparzysta liczba podzielna przez 3 to:", liczba)
        break
