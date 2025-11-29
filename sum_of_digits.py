sayi = int(input("Please enter an integer: "))
toplam = 0
while sayi > 0:
    son_basamak = sayi%10
    toplam += son_basamak
    sayi = sayi//10
print(f"The sum of the digits of the integer you entered is {toplam}")






