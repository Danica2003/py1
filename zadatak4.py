# 4. Napišite program u kome korisnik unosi cenu nekog proizvoda (npr. kupusa), i informacije o njegovoj
# svežini (Korisnik treba da unese "Da" ako je proizvod kupus svež, i "Ne" ako kupus nije svež). 
# Ukoliko je cena kupusa manja od 200rsd, i kupus je svež, program treba da ispiše "Kupićemo ovaj kupus".
# Ukoliko je cena iznad 200rsd, a kupus jeste svež, program treba da ispiše poruku "Jeste svež, ali je preskup!" 
# Ukoliko je cena ispod 200 rsd, a kupus nije svež, program treba da ispiše "Cena je okej, ali nije svež". 
# Ako je cena iznad 200rsd, i kupus nije svež, program treba da ispiše "Zovem vam tržišnu inspekciju".

kupus=input('Da li je kupus svež? Uesite da ili ne: ')
cenaK=int(input('Kolika je cena kupusa? '))

if kupus=='da' and cenaK<200:
    print('Kupićemo ovaj kupus')
elif kupus=='da' and cenaK>200:
    print('Jeste svež, ali je preskup!')
elif kupus=='ne' and cenaK<200:
    print('Cena je okej, ali nije svež!')
elif kupus=='ne' and cenaK>200:
    print('Zovem vam tržišnu inspekciju!')