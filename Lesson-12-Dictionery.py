enemy = {
    'loc x': 90,
    'loc y': 50,
    'color': 'grey',
    'health': 100,
    'name': 'bober',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
    }
all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

for ene in all_enemies:
    print(ene)

all_enemies[5]['health'] = 30
all_enemies[8]['name'] = "surok"
# прибавим к переменной (к самой себе) 10
all_enemies[2]['loc x'] += 10


print("-------------------")
for ene in all_enemies:
    print(ene)
