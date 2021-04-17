# 3. Napišite program u kome korisnik unosi ocenu od 1-5, a program ispisuje opis te ocene.
# (5 - Odličan, 4 - Vrlo Dobar, 3 - Dobar, 2 - Dovoljan, 1 - Nedovoljan). 
# Ako kornsik unese ocenu veću od 5, ili manju od 1, program treba da ispiše poruku "Netačan unos"

ocena=int(input('Unesite ocenu: '))

if ocena==1:
    print('Nedovoljan ',ocena)
elif ocena==2:
    print('Dovoljan ',ocena)
elif ocena==3:
    print('Dobar ',ocena)
elif ocena==4:
    print('Vrlo Dobar ',ocena)    
elif ocena==5:
    print('Odličan ',ocena)

else:
    print('Greška u unosu!')
