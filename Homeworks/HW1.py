"""
  HOMEWORK1:

  1. Bir liste oluşturun ve listenin ikinci yarısını listenin ilk yarısıyla değiştirin
  ve bu listeyi ekrana yazdırın.

  2. Kullanıcıdan "n" değişkenine tek basamaklı bir tamsayı girmesini isteyin. Ardından,
  0'dan n'ye (n dahil) tüm çift sayıları yazdırın.
"""
##### 1. soru ####

liste = [2484,25,1,0,2,21,32,78,56,4,7,3,8]
print("my list:",liste)
lenght = 2
average = len(liste) / float(lenght)
out = []
last_number = 0.0

while last_number < len(liste):
    out.append(liste[int(last_number):int(last_number + average)])
    last_number = last_number + average

first_half = out[0]
second_half = out[1]
print("ilk yarısı:",first_half)
print("ikinci yarısı:",second_half)

for i in range(len(liste)):
    liste.pop()

for i in range(len(second_half)):
    liste.append(second_half[i])

for i in range(len(first_half)):
    liste.append(first_half[i])

print("result:", liste)

##### 2. soru ####

n = int(input("Tek basamaklı bir tamsayı giriniz!"))

for i in range(0, n+1, 1):
    if i%2 == 0:
        print(i)