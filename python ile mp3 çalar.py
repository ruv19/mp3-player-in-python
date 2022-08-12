from random  import choice

class MP3Calar():
    def __init__(self,sarkiListesi=[]):
        self.suanCalanSarki = ""
        self.ses=100
        self.sarkiListesi =sarkiListesi
        self.durum=True

    def sarkiSec(self):
        sayac=1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac,sarki))
            sayac+=1
            secilenSarki = int(input("secmek istediğiniz şarkının numarasini giriniz:"))
            while secilenSarki <1 or secilenSarki >len(self.sarkiListesi):
                secilenSarki = int(input("secmek istediğiniz şarkının doğru  numarasini giriniz(1-{}):".format(self.sarkiListesi)))

            self.suanCalanSarki =self.sarkiListesi[secilenSarki-1]
          
    def sesArttir(self):
        if self.ses ==100:
                pass
        else:
            self.ses+=10
        
    def sesAzalt(self):
        if self.ses==0:
                pass
        else:
            self.ses-=10
    def rastgeleSarkiSec(self):
         rssec= choice(self.sarkiListesi)
         self.suanCalanSarki = rssec
    def sarkiEkle(self):
        sanatci=input("sanatçıyı/grubu giriniz: ")
        sarki=input("şarkıyı giriniz: ")

        self.sarkiListesi.append(sanatci+ "-"+ sarki)

    def sarkiSil(self):
        sayac=1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac,sarki))
            sayac+=1
            silenecekSarki = int(input("silmek istediğiniz şarkının numarasini giriniz:"))

            while silenecekSarki <1 or silenecekSarki >len(self.sarkiListesi):
                silenecekSarki = int(input("silmek istediğiniz şarkının doğru  numarasini giriniz(1-{}):".format(self.sarkiListesi)))

            self.sarkiListesi.pop(silenecekSarki-1)
    def kapa(self):
        self.durum=False
    def menuGoster(self):
        print("""
        --- RND MP3 ÇALARA HOŞGELDİNİZ ---
ŞARKI LİSTESİ:{}
ŞU AN ÇALAN ŞARKI:{}
SES DÜZEYİ:{}
1)ŞARKI SEÇ
2)SES ARTTIR
3)SES AZALT
4)RASTGELE BİR ŞARKI SEÇ
5)ŞARKI EKLE
6)ŞARKI SİL
7)KAPAT
""" .format(self.sarkiListesi,self.suanCalanSarki,self.ses))

    def secim(self):
            sec=int(input("seçiminizi giriniz:"))

            while sec<1 or sec>7:
                sec=int(input("seçtiğiniz değer yanlış,lütfen belirtilen aralıklarda değer giriniz(1-7):"))
            return sec
        
    def calistir(self):
        self.menuGoster()
        secim =self.secim()

        if secim ==1 :
            self.sarkiSec()
        if secim ==2 :
            self.sesArttir()
        if secim ==3 :
           self.sesAzalt()
        if secim ==4 :
            self.rastgeleSarkiSec()
        if secim==5 :
           self.sarkiEkle()
        if secim ==6 :
            self.sarkiSil()
        if secim ==7 :
            self.kapa()
    
mp3calar=MP3Calar()
while mp3calar.durum:
    mp3calar.calistir()

print("program sonlandi")
