# 4. Napišite program u kom korisnik unosi iznos kredita, broj meseci otplate, i kamatu. 

IznosKredita= int(input('Unesite ukupan iznos kredita: '))
brojMesecnihRata= int(input('Unesite broj mesecnih rata: '))
KamatnaStopa= float(input('Unesite kamatnu stopu: '))

rata=(1+KamatnaStopa/1200)**-brojMesecnihRata
rataa=(1200*(1-rata))
IKxKS=IznosKredita*KamatnaStopa
MesecnaRataiznos=IKxKS/rataa

tex= input('Vasa mesecna rata iznosi: ')
print(MesecnaRataiznos)


