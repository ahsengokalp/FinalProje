from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, tecrubeler=None):
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrubeler = tecrubeler if tecrubeler is not None else {}
        self.__statu={}

    def set_statu(self, statu):
        self.__statu = statu

    def get_statu(self):
        return self.__statu

    def get_tecrubeler(self):
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler

    def statu_bul(self):
        max_statu = ""
        max_value = 0
        for statu, yil in self.__statu.items():
            etki=0
            if statu == "mavi yaka":
                etki = yil * 0.2
            elif statu == "beyaz yaka":
                etki = yil * 0.35
            elif statu == "yönetici":
                etki = yil * 0.45
            if etki > max_value:
                max_value = etki
                max_statu = statu
        return max_statu

    def __str__(self):
        return super().__str__() + "Statü: {}\n".format(self.statu_bul())






