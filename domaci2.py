# 2. Korisnik treba da unese svoje ime, naziv i godište svog omiljenog auta. 
# Program treba da ispište te informacije u sledećem formatu:
# >>> Vuk vozi Corvetu ZR1 2014. godište.

ime= input('Unesite vase ime: ')
marka= input('Unesite marku vaseg automobila: ')
model= input('Unesite model vaseg automobila: ')
godiste= int(input('Godina proizvodnje vaseg automobila: '))

print(ime,'vozi',marka, model, godiste,'godiste')
