"""Bilgi yarışması
- Bir bilgi yarışması programı yazın
- Toplamda 10 sorudan oluşmalıdır
- Her sorunun yalnızca bir cevabı olacaktır
- Soruların yanıtlarını büyük / küçük harf duyarlılığına göre ayarlayın
- Her soru 10 puan değerinde olmalıdır
- Kullanıcı 5 veya daha az soruyu yanıtlarsa, başarısız sayılır
- Kullanıcı 5 sorudan daha fazlasını doğru yanıtlarsa başarılı sayılır
"""
sorular = ["Tarihin sıfır noktası olarak bilinen, insanlık tarihinin ilk somut kalıntılarının bulunduğu Göbekli tepe hangi ilimizdedir?",
           "Haberleşmenin eski dildeki adı nedir? ",
           "Telli çalgılarda sazların en kalın teli",
           "Şehzadelerin hükümdar olarak tahta çıkması anına törenlerine ne ad verilir?",
           "Japonların geleneksel güreşine ne ad verilir?",
           "Kapı önünde bulunan basamağa ne ad verilir?",
           "Kız Kalesi hangi ilimizdedir?",
           "İp üstünde gösteri yapanlar hangi mesleği icra eder?",
           "Rusya'nın Başkenti Moskova'da devletin resmi işlerinin de yürütüldüğü ünlü kızıl renkli görkemli sarayının adı nedir?",
           "Hicri Takvime göre Kadir gecesi hangi aydadır?"]
cevaplar = ["Şanlıurfa",
            "Muhabere",
            "Bam Teli",
            "Cülus",
            "Sumo",
            "Eşik",
            "Mersin",
            "Cambaz",
            "Kremlin",
            "Ramazan"]
def soru():
    puan = 0
    for i in range(9):
        
        print(str(i+1)+".soru: ",sorular[i])
        
        cevap = input('Cevabınız Nedir: ')
        
        if (cevap == cevaplar[i] or cevap.replace("İ", "I") == cevaplar[i].upper() or cevap == cevaplar[i].lower()):
            print("Doğru Cevap")
            puan += 10
        else:
            print("Cevabınız yanlıştır!!!")
            
    print("Puan: ",format(puan))
    
    if (puan>=50):
        print("Yarışmayı başarıyla tamamladınız")
        
    else:
        print("Yarışmayı başarıyla tamamlayamadınız!!!")

soru()

)
