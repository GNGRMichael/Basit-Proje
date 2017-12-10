#kullanıcı girişi ilk proje
"""
@author:Burak BOZ
"""
id = "burak"    #kullanıcı adını belirledik.
pw = "123"  #şifreyi belirledik

kullanici = input("Kullanıcı Adınızı Giriniz: ")    #kullanıcı adının girilmesini istedik
sifre = input("Şifrenizi Giriniz: ")    #şifrenin girilmesini istedik.

if (id == kullanici and sifre == pw ):  # kullanıcı adı ve şifre doğruysa
    print("\nGiriş Başarıyla Gerçekleşti.\nYükleniyor...")  #içerdeki metni yazdırdık \n alt satıra git demek
elif (id == kullanici) and (sifre != pw):   #kullanıcı adı doğru ve şifre doğru değilse
    print("\nHatalı Şifre Giriniz.\nTekrar Deneyin...")     #metni yazdırdık
elif (id != kullanici) and (sifre == pw):   #kullanıcı adı yanlış şifre doğru ise
    print("\nHatalı Kullanıcı Adı Girdiniz.\nTekrar Deneyin...")    #metni yazdırdık
else:   #yukardaki koşulun dışında ikiside yanlış girilmişşe
    print("\nHatalı Giriş...")  #metni yadırdık