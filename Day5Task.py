#Task Dictionary
days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday', 'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday', 'minggu': 'sunday'
}
# latihan bikin kamus
# id = eng
hari = input('Ketik nama hari : ')
print(f'Bahasa Inggrisnya {hari.upper()} = {days.get(hari.lower(), "Ga ada!")}')

# 'id - eng' dan 'eng - id'
hari = list(days)
day = list(days.values())

x = input('Ketik nama hari (ENG/IDN) : ')
if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs Inggris {x.lower()} adalah {engHari}')
else:
    idDay = hari[day.index(x.lower())]
    print(f'Bhs Indonesia {x.lower()} adalah {idDay}')



# Task Boolean
nilai = 62
if nilai >= 82:
    print('Nilai kamu A')
elif 72 <= nilai <= 81:
    print('nilai kamu B')
elif 62 <= nilai <= 71:
    print('nilai kamu C')
elif 52 <= nilai <= 61:
    print('nilai kamu D')
else:
    print('nilai kamu E')