# friend or foe

names = ['Ryan', 'Bruce', 'Lily', 'Alfred', 'Jimmy', 'Toto', 'Scout']
friends = []
foes = []

for name in names:
    if len(name) == 4:
        friends.append(name)
    else:
        foes.append(name)

print(friends)
print(foes)