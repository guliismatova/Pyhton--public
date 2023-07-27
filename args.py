# def yigindi(*sonlar):
#     bosh_yigindi = 0
#     for i in sonlar:
#         bosh_yigindi += i
#     return sonlar
# print(yigindi(1,2,5))


# def yigindi(*sonlar):
#     return sum(sonlar)
# print(yigindi(10,20,30))



# musbat va manfiy sonlarni nechtaligini aniqlash

# musbat = 0
# manfiy = 0
# a = float(input("Birinchi son  = "))
# b = float(input("Ikkinchi son  = "))
# c = float(input("Uchinchi son  = "))

# if a>0:
#     musbat+=1
# elif a<0:
#     manfiy+=1
# if b>0:
#     musbat+=1
# elif b<0:
#     manfiy+=1
# if c>0:
#     musbat+=1
# elif c<0:
#     manfiy+=1

# print("Musbat sonlar soni = ", musbat)
# print("Manfiy sonlar soni = ", manfiy)


############################################

# Sonlarni kamida 2ta majburiy qiymat berishni so'raydigan, va yig'indisini aniqlaydigan funksiya
# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
# print(summa(1,2,10))


# def oquvchi(ism,familiya,*malumot):
#     return ism,familiya,malumot
# print(oquvchi("Gulmira","Ismatova","12yosh"))

