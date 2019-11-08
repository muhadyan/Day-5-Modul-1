
# DICTIONARY
andi = {
    'name': 'Andi',
    'age': 22,
    'is_married': False,
    'cars': ['Alphard', 'Xpander', 'Innova'],
    'address': {
        'street': 'Mawar Ungu',
        'RT': 5, 'RW': 121, 'kecamatan': 'X',
        'zipcode': 123456,
        'geo': {
            'lat': 111.11,
            'lng': 65.89
        }
    }
}

print(andi['name'])
print(andi['age'])
print(andi['is_married'])
print(andi['cars'][0])
print(andi['address']['geo'])
# atau
print(andi.get('name'))
print(andi.get('age'))
print(andi.get('is_married'))
# keluar semua infonya
print(andi)

# kalau datanya ga ada (harus pake .get)
print(andi.get('job'))
# Bisa diisi dengan
print(andi.get('job', 'Maaf Andi masih nganggur'))

# ubah value (nama Andi jadi Budi)
andi['name'] = 'Budi'

# buat nambahin elemen
andi['salary'] = 25000000
# atau
andi.update({'no_ktp': 3276063004950007})

# ngecek values nya aja
print(andi.values())

# ngeubah jadi list
print(list(andi))
print(list(andi.keys()))
print(list(andi.values()))  # values nya dijadiin list

# keys dan values nya tetep muncul kalo jadi list
x ={1: True, 2: False}
print(x.items())


# IF STATEMENT
# equation
print(x == 3)
print(x >= 3)
print(x <= 3)
# comparison
print(x > 3)
print(x < 3)
print(x != 3)   #tidak sama dengan

x = 4
if x == 4:
    print('Ini 4')
else:
    print('Ini bukan 4')

x = 6
if x < 10:
    print('x kurang dari 10')
else:
    print('x lebih dari 10')

nilai = 81
if nilai > 80:
    print('Anda lulus!')
elif nilai < 40:
    print('Anda tidak lulus!')
else:
    print('Anda remedial!')


jomblo = True
if jomblo:
    print('Anda jomblo')
else:
    print('Anda taken')
# atau
jomblo = True
if jomblo == True:
    print('Anda jomblo')
else:
    print('Anda taken')

jomblo = True; nganggur = True
if jomblo == True and nganggur == True:
    print('Anda jomblo pengangguran')
elif jomblo == True and nganggur == False:
    print('Anda kurang piknik')
elif jomblo == False and nganggur == True:
    print('Anda bucin')
else:
    print('Anda OK')
#atau
jomblo = False; nganggur = True
if jomblo and nganggur:
    print('Anda jomblo pengangguran')
elif jomblo and not nganggur:
    print('Anda kurang piknik')
elif not jomblo and nganggur:
    print('Anda bucin')
else:
    print('Anda OK')




# kalo diubah ke list, nanti yg muncul cuma key (name, age, dst) nya aja
# di boolean (True False) ada 'or' juga