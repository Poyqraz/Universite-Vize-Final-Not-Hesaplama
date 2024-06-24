
print("SÜ Not Hesaplama ve Hesap Makinesi")

OgrenciNo=input("Ogrenci No Giriniz: ")
Sifre=input("Sifrenizi Giriniz: ")

if(OgrenciNo== "1234" and Sifre == "admin"):

    islem1=int(input("Hos Geldiniz Yapmak istediğiniz adımı seçiniz.\n 1-Üniversite Harf Notu Hesaplama \n 2-Basit Hesap Makinesi "))

    if(islem1 == 1):

        VizeNotu=int(input("Vize Notunu Giriniz: "))
        FinalNotu=int(input("Final Notunu Giriniz: "))
        Ortalama = ((VizeNotu*0.30) + (FinalNotu*0.70))

        if(Ortalama < 38):
            print("Bute Girebilir.")
            ButNotu=int(input("But Notunu Giriniz(Girmediyse 0)= "))
            FinalNotu = ButNotu
            Ortalama = ((VizeNotu*0.40) + (FinalNotu*0.60))
        if(Ortalama<=33):
            print("Harf Notu = FF\nDers Notunuz =", Ortalama)
        elif(Ortalama>33 and Ortalama<38):
            print("Harf Notu = DD\nDers Notunuz =", Ortalama)
        elif(Ortalama>=38 and Ortalama<45):
            print("Harf Notu = DC\nDers Notunuz =", Ortalama)
        elif(Ortalama>=45 and Ortalama<52):
            print("Harf Notu = CC\nDers Notunuz =", Ortalama)
        elif(Ortalama>=52 and Ortalama<60):
            print("Harf Notu = CB\nDers Notunuz =", Ortalama)
        elif(Ortalama>=60 and Ortalama<67):
            print("Harf Notu = BB\nDers Notunuz =", Ortalama)
        elif(Ortalama>=67 and Ortalama<75):
            print("Harf Notu = BA\nDers Notunuz =", Ortalama)
        elif(Ortalama>=75):
            print("Harf Notu = AA\nDers Notunuz =", Ortalama)

            # Hesap makinesi

    elif(islem1 == 2):
         mat=int(input("\n 1-Toplama \n 2-Çıkarma \n 3-bölme \n 4-Çarpma \n Yapmak istediğiniz işlemi Seçiniz: "))
         if(mat == 1):
             sayi1=int(input("Birinci Sayıyı Giriniz= "))
             sayi2=int(input("İkinci Sayıyı Giriniz= "))
             Hesapla= sayi1 + sayi2
             print("Sonuç = " and Hesapla)

         if(mat == 2):
              sayi1=int(input("Birinci Sayıyı Giriniz= "))
              sayi2=int(input("İkinci Sayıyı Giriniz= "))
              Hesapla= sayi1 - sayi2
              print("Sonuç = " and Hesapla)

         if(mat == 3):
            sayi1=int(input("Bölünen Sayıyı Giriniz= "))
            sayi2=int(input("Bölen Sayıyı Giriniz= "))
            Hesapla= sayi1 / sayi2
            print("Sonuç = " and Hesapla)

         if(mat == 4):
              sayi1=int(input("Birinci Sayıyı Giriniz= "))
              sayi2=int(input("İkinci Sayıyı Giriniz= "))
              Hesapla= sayi1 * sayi2
              print("Sonuç = " and Hesapla)

else:
    print("Hatalı Giriş")