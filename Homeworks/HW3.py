
"""
Ders Notu Uygulaması 
- 5 öğrenci oluşturun. Kullanıcıdan bu öğrencilere sorun.
- Bu öğrencilerin her birinin bir ara notu, proje notu ve final notu olması gerekir.
- Her öğrencinin ders geçme notu olacaktır.
- geçme notu = ara sınav * (0.3) + proje * (0.3) + final * (0.4) geçme notu bu şekilde belirlenmelidir.
- Bu öğrencilerin bilgilerini tutan bir sözlük oluşturun.
- Öğrencinin notlarını hesaplayın ve indeksleme yardımı ile listeye aktarın.
- Son olarak, notu en yüksek olan öğrenciyi ilk dizinde ve en düşük notu olan öğrenciyi listenin son dizininde olacak şekilde ayarlayın.
"""
#### Course Grade Application ##############

dict={}
ogr = []
arasinav = []
proje = []
final = []
gecme = []
def gecmenotu(note):
    gecmen = note[0] * (0.3) + note[1] * (0.3) + note[2] * (0.4)
    print("gecme notu: ",gecmen)
    return gecmen
for i in range(5):
    ogr.append(input(str(i+1)+". öğrencinin adı:"))
    arasinav.append(input(str(i+1)+". öğrencinin ara sınav notu:"))
    proje.append(input(str(i+1)+". öğrencinin proje notu:"))
    final.append(input(str(i+1)+". öğrencinin final notu:"))
    dict[str(ogr[i])] = [int(arasinav[i]), int(proje[i]), int(final[i])]
    gecme.append(gecmenotu(dict[str(ogr[i])]))

gecme.sort(reverse=True)

print("",dict)
print("gecme notu: ",ogr)

