from Insan import Insan

insan1 = Insan("12345678910", "Ahmet", "Yılmaz", 30, "Erkek", "Türk")
insan2 = Insan("98765432100", "Aliye", "Ata", 22, "Kadın", "Türk")
print(insan1)
print(insan2)
issiz1 = Issiz("12345678910", "Ali", "Demir", 33, "Erkek", "Türk")
issiz1.set_statu({"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})
issiz2 = Issiz("98765432100", "Veli", "Şen", 24, "Kadın", "Türk")
issiz2.set_statu({"mavi yaka": 1, "beyaz yaka": 3, "yönetici": 5})
issiz3 = Issiz("56789012345", "Ayşe", "Mutlu", 35, "Erkek", "Türk")
issiz3.set_statu({"mavi yaka": 3, "beyaz yaka": 5, "yönetici": 7})
print(issiz1)
print(issiz2)
print(issiz3)

calisan1 = Calisan("12345678910", "Fatma", "Gür", 32, "Erkek", "Türk", "teknoloji", 10, 12000)
calisan2 = Calisan("28765432100", "Aylin", "Kaya", 26, "Kadın", "Türk", "muhasebe", 2, 18000)
calisan3 = Calisan("36789012345", "Elif", "Eren", 35, "Erkek", "Türk", "inşaat", 7, 25000)

print(calisan1)
print(calisan2)
print(calisan3)