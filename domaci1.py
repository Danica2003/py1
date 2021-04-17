# # >>> U 7 godina ima 84 meseca, 2555 dana, 61320 sati, 3679200 minuta.
minuta= 60
sat= 60
dan= 24
mesec= 12
godina= 365

godine = int(input('Unesite broj godina: '))

print(godine, 'godina ima', godine*mesec, 'meseca', godine*godina, 'dana', 
godine*godina*dan, 'sati', godine*godina*dan*sat, 'minuta')

