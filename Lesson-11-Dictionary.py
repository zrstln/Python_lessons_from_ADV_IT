# (-----item----------)
# ____(key)---(value)___
enemy = {
    'loc x': 90,
    'loc y': 50,
    'color': 'grey',
    'health': 100,
    'name': 'bober',
    }
print(enemy)
print("Location X = " + str(enemy['loc x']))
print("Location Y = " + str(enemy['loc y']))
print("His name is:" + enemy['name'])
print("------------------------------")
enemy['rank'] = 'Admin'
print(enemy)
del enemy['rank']
print(enemy)
enemy['loc x'] = enemy['loc x'] + 40
enemy['loc y'] = enemy['loc y'] - 20
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'red'
print(enemy)
print(enemy.keys())
print(enemy.values())
