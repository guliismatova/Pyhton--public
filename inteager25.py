birinchi_kun = 5
k = int(input("Kunni kiriting:"))
hafta = ["Yakshanba","Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba"]
topish_kk = (k+birinchi_kun-5)%7
print(f"{k} raqam  haftaning = {hafta[topish_kk]} kuniga teng")