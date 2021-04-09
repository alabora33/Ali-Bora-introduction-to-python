"""
kullanıcı giriş uygulaması:
-kullanıcıdan kullanıcı adı ve şifre değerlerini alın.
-if ifadesindeki değerleri kontrol edin ve başarılı olup olmadıklarını söyleyin
ekstra:
-Aynı kullanım giriş uygulamasını oluşturmaya çalışın, ancak bu sefer sözlüğü kullanın
"""

###user login application####

username = "alabora33"
password = "12345"

kullaniciadi = input("Kullanıcı adını giriniz:")
sifre = input("Şifreyi giriniz:")

if (kullaniciadi==username and sifre==password):
    print("Başarıyla giriş yaptınız ")
else:
    print("Kullanıcı adı veya şifre yanlıştır!!!")
    
### extra #####

d = {
 "username" : "alabora33",
 "password" : "12345"              
}    

kullaniciadi = input("Kullanıcı adını giriniz:")
sifre = input("Şifreyi giriniz:")

if(d.get("username")==kullaniciadi and d.get("password")==sifre):
    print("Başarıyla giriş yaptınız ")
else:
    print("Kullanıcı adı veya şifre yanlıştır!!!")






















