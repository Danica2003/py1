# 1. Napišite program u kome korisnik unosi godinu. 
# Program potom računa i ispisuje da li je godina prestupna ili nije. 
# Napomena: Ostatak pri deljenju u pythonu se računa sa "%" simbolom. 
# Npr: 9 % 3 = 0, pošto je ostatak od deljenja broja 9 sa brojem 3 = 0

god= int(input('Unesite godinu: '))
print(god)

if (god%100==0) or (god%400==0) or (god%4==0):
    print('Godina je prestupna!')

else: 
    print('Godina nije prestupna')


