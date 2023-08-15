###################case7#################
# a=int(input("massani kiriting")) 
# b=int(input("massaning birligini kiriting(1-kg,2-mg,3-gr,4-t,5-sr)")) 
# match b: 
#     case 1: 
#         print(a,"kg") 
#     case 2: 
#         print(a/1000000,"kg") 
#     case 3: 
#         print(a*0.001,"kg") 
#     case 4: 
#         print(a*1000,"kg") 
#     case 5: 
#         print(a/100,"kg") 
#     case other: 
#         print("bunday og`irlik birligi yo`q!")


################case8##################
# d =  int(input("kun = "))
# m = int(input("Oy = "))
# match m:
#     case 1:
#         if 0<d<31:
#             print(d,"-Yanvar")
#         else:
#             print("Bunday kun mavjud emas")
#     case 2:
#         if 0<d<28:
#             print(d,"-Fevral")
#         else:
#             print("Bunday kun mavjud emas")
#     case 3:
#         if 0<d<31:
#             print(d,"-Mart")
#         else:
#             print("Bunday kun mavjud emas")
#     case 4:
#         if 0<d<30:
#             print(d,"-Aprel")
#         else:
#             print("Bunday kun mavjud emas")
#     case 5:
#         if 0<d<31:
#             print(d,"May")
#         else:
#             print("Bunday kun mavjud emas")
#     case 6:
#         if 0<d<30:
#             print(d,"-Iyun")
#         else:
#             print("Bunday kun mavjud emas")
#     case 7:
#         if 0<d<31:
#             print(d,"-Iyul")
#         else:
#             print("Bunday kun mavjud emas")
#     case 8:
#         if 0<d<31:
#             print(d,"-Avgust")
#         else:
#             print("Bunday kun mavjud emas")
#     case 9:
#         if 0<d<30:
#             print(d,"-Sentyabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case 10:
#         if 0<d<31:
#             print(d,"-Oktyabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case 11:
#         if 0<d<30:
#             print(d,"-Noyabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case 12:
#         if 0<d<31:
#             print(d,"-Dekabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case other :
#         print("Bunday oy  va kun mavjud emas")




########################case9##########################
# d =  int(input("kun = "))
# m = int(input("Oy = "))
# match m:
#     case 1:
#         if 0<d<31:
#             print(d+1,"-Yanvar")
#         else:
#             print("Bunday kun mavjud emas")
#     case 2:
#         if 0<d<28:
#             print(d+1,"-Fevral")
#         else:
#             print("Bunday kun mavjud emas")
#     case 3:
#         if 0<d<31:
#             print(d+1,"-Mart")
#         else:
#             print("Bunday kun mavjud emas")
#     case 4:
#         if 0<d<30:
#             print(d+1,"-Aprel")
#         else:
#             print("Bunday kun mavjud emas")
#     case 5:
#         if 0<d<31:
#             print(d+1,"May")
#         else:
#             print("Bunday kun mavjud emas")
#     case 6:
#         if 0<d<30:
#             print(d+1,"-Iyun")
#         else:
#             print("Bunday kun mavjud emas")
#     case 7:
#         if 0<d<31:
#             print(d+1,"-Iyul")
#         else:
#             print("Bunday kun mavjud emas")
#     case 8:
#         if 0<d<31:
#             print(d+1,"-Avgust")
#         else:
#             print("Bunday kun mavjud emas")
#     case 9:
#         if 0<d<30:
#             print(d+1,"-Sentyabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case 10:
#         if 0<d<31:
#             print(d+1,"-Oktyabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case 11:
#         if 0<d<30:
#             print(d+1,"-Noyabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case 12:
#         if 0<d<31:
#             print(d+1"-Dekabr")
#         else:
#             print("Bunday kun mavjud emas")
#     case other :
#         print("Bunday oy  va kun mavjud emas")


###################case10####################
# tomon = input("Tomon  = ")
# match tomon :
#     case "S":
#         print("Shimol")
#     case "J":
#         print("Janub")
#     case "Q":
#         print("Sharq")
#     case "G":
#         print("G'arb")
#     case other:
#         print("Bunday tomon mavjud emas")
# komanda = input("Raqam = ")
# match komanda:
#     case 0 :
#         print("Harakat davom ettir")
#     case 1 :
#         print("Chapga buril")
#     case 2 :
#         print("O'ngga buril")
#     case other:
#         print("Bunday komanda mavjud emas")


#################case12####################
# P = 3,14
# element = input("Element:")
# son = int(input("Qiymati ="))
# match element:
#     case "R":
#         print("Deametr = ",son*2)
#         print("Uzunligi = ",P*2*son)
#         print("Yuzasi = ",P*(son**2))
#     case "D":
#         print("Radius = ",son/2)
#         print("Uzunligi = ",(son/2)*P*son)
#         print("Yuzasi = ",((son/2)**2)*P)
#     case "L":
#         print("Deametr = ",son/(P*4))
#         print("Radius = :",son/(P*2))
#         print("Yuzasi = ",(son/2)*son)

    


##################case15################
# Karta = float(input("Karta turi = "))
# match karta:
#     case karta if 1 <= karta <= 4:
#         print("M turdagi karta")
#     case karta if 6 <= karta <= 14:
#         print("N turdagi karta")
#     case other:
#         print("Xatolik")


#####################case12###################
# radius=float(input("r ni kiriting"))
# komanda=int(input("komandani kiriting"))
# match komanda:
#     case 1:
#         print(radius)
#         print(radius*2)
#         print(radius*2*3.14)
#         print(3.14*(radius**2))
#     case 2:
#         print(radius)
#         print(radius*2)
#         print(radius*2*3.14)
#         print(3.14*(radius**2))
#     case 3:
#         print(radius)
#         print(radius*2)
#         print(radius*2*3.14)
#         print(3.14*(radius**2))
#     case 4:
#         print(3.14*(radius**2))














#case

# yosh1 = int(input("Yosh = "))
# match yosh1:
#     case 1:
#         print("Bir")
#     case 2:
#         print("Ikki")
#     case 3:
#         print("Uch")
#     case 4:
#         print("To'rt")
#     case 5:
#         print("Besh")
#     case 6:
#         print("Olti")
#     case 7:
#         print("Yetti")
#     case 8:
#         print("Sakkiz")
#     case 9:
#         print("To'qqiz")




