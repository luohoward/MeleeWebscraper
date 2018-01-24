import random


def randomlyGenerateColor(): 
    s = '#'
    for i in range(0, 6):
        d = random.randint(0, 15)
        s = s + str(colorRand[d])    

    return s




colorRand = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

character = [] 

with open('tournamentResults.txt', 'r') as f:
    results = [x.strip('\n') for x in f.readlines()]
    for result in results:
        if len(result.split('\t')) == 1:
            continue
        else:
            splitResult = result.split('\t')
            for i in range(2, len(splitResult)):
                character.append(" ".join(splitResult[i].split()[:-1]))

s = ""        

with open('characters.txt', 'r') as f:
    s = f.read().strip()

listColor = s.split('\n')    
d = {}

for item in listColor:
    key, value = item.split(':')
    d[key] = value

for c in character:
    if c not in d:
        d[c] = randomlyGenerateColor()

print d

with open('characters.txt', 'w') as f:
    s = ""
    for key, value in d.iteritems():
        s = s + key + ':' + value + '\n'
    f.write(s.strip())
