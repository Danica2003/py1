# 3. Otvorite novi .py fajl i u njega kopirajte prethodni primer. 
# U tom fajlu, dodajte još jedno polje za unos mesečne količine novca
# koju možete da odvajate za taj auto, i polje za unos cene tog auta. 
# Program treba da ispisuje broj godina koji će vam trebati da ga kupite.
#  (Kada se zaposlite kao testeri, videćete da ovaj broj znatno pada )
# >>> Vuk -u će trebati 25 godina da kupi Corvetu ZR1 2014. godište.

ime= input('Unesite vase ime: ')
marka= input('Unesite marku vaseg automobila: ')
model= input('Unesite model vaseg automobila: ')
godiste= int(input('Godina proizvodnje vaseg automobila: '))

UkupnaCena= int(input('unesite cenu automobila: '))
Rata= int(input('Unesite mesecnu ratu: '))
brojMesecnihRata= UkupnaCena/Rata

godinaOtplate= (brojMesecnihRata/12)

print(ime, 'ce za', godinaOtplate, 'godina da kupi',marka, model,godiste,'godiste.')