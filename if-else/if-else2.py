#11masala
# a = int(input("A sonini kiriting:"))
# b = int(input("B sonini kiriting:"))
# if a>b:
#     print("A = ",max(a,b), "B =",(a,b))
# elif a<b:
#    print("A = ",max(a,b), "B =",(a,b))
# else:
#     print("A = ",0, "B =",0)

#12masala
# a = int(input("A sonini kiriting:"))
# b = int(input("B sonini kiriting:"))
# c = int(input("C sonini kiriting:"))
# if a>b>c:
#     print(f"Sonlardan eng kichigi =",c)
# elif a<b<c:
#     print(f"Sonlardan eng kichigi =",a)
# else:
#     print(f"Sonlardan eng kichigi =",b)


#13masala
# a = int(input("A sonini kiriting:"))
# b = int(input("B sonini kiriting:"))
# c = int(input("C sonini kiriting:"))
# if a>b>c:
#     print(f"Sonlarning o'rtachasi =",b)
# elif a<c<b:
#     print(f"Sonlarning o'rtachasi =",c)
# elif c<a<b:
#     print(f"Sonlarning o'rtachasi =",a)

#14masala
# a = int(input("A sonini kiriting:"))
# b = int(input("B sonini kiriting:"))
# c = int(input("C sonini kiriting:"))
# if a>b>c:
#     print(f"Sonlarning kattasi =",b)
#     print(f"Sonlarning kattasi =",a)
# elif a<c<b:
#     print(f"Sonlarning kattasi =",b)
#     print(f"Sonlarning kattasi =",a)

# elif c<a<b:
#     print(f"Sonlarning o'rtachasi =",a)

#15masala





# def avto(**malumot):
#     return malumot
# print(avto(nomi="Lacetti",yil=2023))

# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar


# avto1 = avto_info("GM","Malibu",Rangi ="qora",yil = 2018)
# avto2 = avto_info("Kia","K5",Rangi = "qizil",narh = 35000)
# print(avto2)'


# def kopaytirish(*sonlar):
#     kopaytma = 1
#     for i in sonlar:
#         kopaytma *= i
#     return kopaytma

# print(kopaytirish(8,9,5))

# def talabalar(**malumotlar):
#     return malumotlar
# print(talabalar(ism = "Ozoda",familiya = "Xushnudova",yosh = 13,manzil =" Qarshi sh. 245uy",maktab = "10-umumtalim maktabi",sinf = "7sinf"))


# a = int(input("A sonini kiriting"))
# b = int(input("B sonini kiriting"))
# c = int(input("C sonini kiriting"))
# print(sorted[a,b,c])

# sonlar = []
# n = int(input("Nechta son tartiblamoqchisiz = "))
# for i in range(n):
#     son = int(input(f"{i+1}-sonni kiriting"))
#     sonlar.append(son)
# sonlar.sort()
# print(f"Eng kichigidan tartiblash")
# for son in sonlar:
#     print(son)