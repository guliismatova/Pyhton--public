birinchi_kun = 6
k = int(input("Kunni kiriting:"))
hafta = ["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]
topish_kk = (k+birinchi_kun-6)%7
print(f"{k} raqam  haftaning = {hafta[topish_kk]} kuniga teng")