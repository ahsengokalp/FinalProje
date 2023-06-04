from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        try:
            if self.__tecrube < 2:  # tecrube 2 den küçükse
                return 0
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:  # tecrube 4 den küçükse ve maaş 15000 den küçükse aşağıdaki fonksiyonu döndür
                return self.__maas % self.__tecrube / 100
            elif self.__tecrube > 4 and self.__maas < 25000:  # tecrube 4 den büyükse ve maas 25000 den küçükse aşağıdaki fonksiyonu döndür
                return (self.__maas % self.__tecrube) / 200
            else:
                return 0
        except Exception as e:  # hata oluşma durumunda hatayı gösterme
            print("Hata-", str(e))
    def get_yeni_maas(self):
        return self.__maas + self.zam_hakki()

    def __str__(self):
        yeni_maas = self.__maas + self.zam_hakki()  # yeni maas hesaplama
        return f"Ad: {self.get_ad()}\nSoyad:{self.get_soyad()}\nTecrübe:{self.__tecrube} ay\nYeni Maaş:{yeni_maas} TL"


