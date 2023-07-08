def oquvchi(ism,familiya,yosh,maktab,sinf,manzil,sharif = None):
    talaba =  {
        'ism': ism,
        'familiya': familiya,
        'yosh': yosh,
        'maktab': maktab, 
        'sinf' : sinf,
        'manzil' : manzil,
        'sharif' : sharif,
    }
    return talaba
oquvchilar = []

while True :
    ism = input('Ism kiriting:')
    familiya = input('Familiya kiriting:')
    yosh = input('Yosh kiriting:')
    maktab = input('Maktab kiriting:')
    sinf = input('Sinf kiriting:')
    manzil = input('Manzil kiriting:')
    sharif = input('Sharif kiriting:')

    oquvchilar.append(oquvchi(ism,familiya,yosh,maktab,sinf,manzil,sharif))
    javob = input("Yana malumot qo'shaszmi?:")
    if javob == "No" or "N" and "Y":
        break
print(oquvchilar)