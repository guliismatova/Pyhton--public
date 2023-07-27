N = int(input("N ni kiriting"))
birinchi_kun = N
k = int(input("Kunni kiriting:"))
hafta = ["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]
topish_kk = (k+N-birinchi_kun)%7
print(f"{k} raqam  haftaning = {hafta[topish_kk]} kuniga teng")