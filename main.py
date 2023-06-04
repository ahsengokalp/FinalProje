from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
 print("İnsan Bilgileri:")
 insan1 = Insan("12345678910", "Ahmet", "Yılmaz", 30, "Erkek", "Türk")
 print(insan1,"\n")
 insan2 = Insan("98765432100", "Aliye", "Ata", 22, "Kadın", "Türk")
 print(insan2)
 print("-------------------------------------------------")
 print("Issiz Bilgileri:")
 issiz1 = Issiz("12345678910", "Ali", "Demir", 33, "Erkek", "Türk", "mavi yaka", {"mavi yaka": 5})
 print(issiz1, "\n")
 issiz2 = Issiz("98765432100", "Veli", "Şen", 24, "Kadın", "Türk", "beyaz yaka", {"beyaz yaka": 8})
 print(issiz2, "\n")
 issiz3 = Issiz("56789012345", "Ayşe", "Mutlu", 35, "Erkek", "Türk", "yönetici", {"yönetici": 10})
 print(issiz3)
 print("-------------------------------------------------")
 print("calisan bilgileri:")
 calisan1 = Calisan("12345678910", "Fatma", "Gür", 32, "Erkek", "Türk", "teknoloji", 10, 12000)
 print(calisan1,"\n")
 calisan2 = Calisan("28765432100", "Aylin", "Kaya", 26, "Kadın", "Türk", "muhasebe", 2, 18000)
 print(calisan2,"\n")
 calisan3 = Calisan("36789012345", "Elif", "Eren", 35, "Erkek", "Türk", "inşaat", 7, 25000)
 print(calisan3)
 print("--------------------------------------------------")
 print("Mavi Yaka Bilgileri: ")
 mavi_yaka1 = MaviYaka("44545678910", "Bengü", "Murat", 30, "Erkek", "Türk", "teknoloji", 3, 12000, 0.2)
 print(mavi_yaka1,"\n")
 mavi_yaka2 = MaviYaka("55565432100", "Yavuz", "Kaya", 27, "Kadın", "Türk", "muhasebe", 2, 18000, 0.5)
 print(mavi_yaka2,"\n")
 mavi_yaka3 = MaviYaka("76789012342", "Alp", "Yıldız", 32, "Erkek", "Türk", "inşaat", 12, 25000, 0.3)
 print(mavi_yaka3)
 print("Beyaz Yaka Bilgileri: ")
 beyaz_yaka1 = BeyazYaka("89945678910", "Merve", "Yılmaz", 32, "Erkek", "Türk", "teknoloji", 12, 12000, 500)
 print(beyaz_yaka1,"\n")
 beyaz_yaka2 = BeyazYaka("98765992100", "Mehmet", "Şen", 45, "Kadın", "Türk", "muhasebe", 5, 18000, 1500)
 print(beyaz_yaka2,"\n")
 beyaz_yaka3 = BeyazYaka("16709012305", "Zeynep", "Demir", 35, "Erkek", "Türk", "inşaat", 1, 25000, 1000)
 print(beyaz_yaka3)
 print("----------------------------------------------------------------------")

except Exception as e:
    print(str(e))

data = {
    "nesne": ["calisan1", "calisan2", "calisan3", "mavi_yaka1", "mavi_yaka2", "mavi_yaka3", "beyaz_yaka", "beyaz_yaka", "beyaz_yaka"],
    "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(),mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
    "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
    "soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
    "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
    "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
    "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
    "sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
    "tecrube": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
    "maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
    "yipranma_payi": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0, 0],
    "tesvik_primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
    "yeni_maas": [calisan1.get_yeni_maas(), calisan2.get_yeni_maas(), calisan3.get_yeni_maas(), beyaz_yaka1.get_yeni_maas(), beyaz_yaka2.get_yeni_maas(), beyaz_yaka3.get_yeni_maas(), mavi_yaka1.get_yeni_maas(), mavi_yaka2.get_yeni_maas(), mavi_yaka3.get_yeni_maas()]
}

df = pd.DataFrame(data)
df.fillna(0, inplace=True)


tecrube_ort = df.groupby("sektor")["tecrube"].mean()
yeni_maas_ort = df.groupby("sektor")["yeni_maas"].mean()
print("Tecrube Ortalamalari:\n", tecrube_ort)
print("Yeni Maas Ortalamalari:\n", yeni_maas_ort)


maas_15000_ust = df[df["maas"] > 15000].shape[0]
print("15000TL Üzerinde Maaş Alanların Toplam Sayısı:", maas_15000_ust)


df.sort_values(by="yeni_maas", inplace=True)
print("Yeni Maaşa Göre Sıralama:\n", df)

beyaz_yaka_tecrube_3 = df[(df["nesne"] == "beyaz_yaka") & (df["tecrube"] > 3)]
print("Tecrübesi 3 Seneden Fazla Olan Beyaz Yakalılar:\n", beyaz_yaka_tecrube_3)

yeni_maas_10000_ust = df[df["yeni_maas"] > 10000].iloc[2:5].loc[:, ["tc_no", "yeni"]]
print("Yeni Maaşı 10000 TL Üzerinde Olanlar(2-5 Satır):\n", yeni_maas_10000_ust)

yeni_df = df[["ad", "soyad", "sektor", "yeni_maas"]]
print("Yeni DataFrame:\n", yeni_df)

