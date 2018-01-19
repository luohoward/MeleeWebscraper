mostSuccessfulCharactersSecondaries = {}
mostSuccessfulMains = {}
mostSuccessfulPlayer = {}

with open("tournamentResults.txt", "r") as f:
    for line in f:
        strippedLine = line.strip()
        delimitedList = strippedLine.split("\t")
        if len(delimitedList) > 1:
            for i in range(2,len(delimitedList)):
                character = " ".join(delimitedList[i].split()[:-1])
                if character in mostSuccessfulCharactersSecondaries:
                    mostSuccessfulCharactersSecondaries[character] += 1
                else:
                    mostSuccessfulCharactersSecondaries[character] = 1

            character = " ".join(delimitedList[2].split()[:-1])
            if character in mostSuccessfulMains:
                mostSuccessfulMains[character] += 1
            else:
                mostSuccessfulMains[character] = 1

            player = delimitedList[1][8:]
            if player == "Dr. PeePee":
                player = "PPMD"

            if player in mostSuccessfulPlayer:
                mostSuccessfulPlayer[player] += 1
            else:
                mostSuccessfulPlayer[player] = 1

print mostSuccessfulCharactersSecondaries
print mostSuccessfulMains
print mostSuccessfulPlayer