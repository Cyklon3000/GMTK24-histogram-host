from pprint import pprint
from collections import defaultdict

idIgnoreList = [679464756]

with open("discordExampleString.txt", "r") as file:
    data = file.readlines() # unhandeled

data = \
[
{"level" : line.split(" ")[4][:1], "playerID": int(line.split(" ")[0]), "score": float(line.split(" ")[7][:-2])}
for line in data
    if not
        (
            line.startswith("highscoreUpdates") or
            line.startswith("APP") or
            line.startswith(" ") or
            int(line.split(" ")[0]) in idIgnoreList
        )
]

# pprint(data)

scoreData = defaultdict(list)
for d in data:
    level = d.pop('level')
    scoreData[level].append(d)

# pprint(dict(levelData))

def prepareJsonDict(highestScore: float, totalCount:int):
    jsonDict = \
    {
        "highestCount": 0, # highestCount cannot be determined yet
        "highestScore": highestScore,
        "lowestScore": 0.0,
        "totalCount": totalCount,
        "values": [
            # Set with spacing based on highest score
        ]
    }
    
    for i in range(10):
        min_val = i * (highestScore / 10)
        max_val = (i + 1) * (highestScore / 10)
        jsonDict["values"].append(
            {"count": 0 , "max": round(max_val, 3), "min": round(min_val, 3)}
        )
    
    return jsonDict

for level in scoreData:
    # highestCount cannot be determined yet
    highestScore:float = 0.0
    totalCount:int     = 0
    
    uniquePlayerScores = dict()
    for scoreEntry in scoreData[level]: # scoreEntry : {'playerID': 12345678, 'score': 2.5}
        uniquePlayerScores[scoreEntry['playerID']] = \
                max(scoreEntry['score'], uniquePlayerScores[scoreEntry['playerID']]) \
            if scoreEntry['playerID'] in uniquePlayerScores else \
                scoreEntry['score']
        
        highestScore = max(highestScore, scoreEntry['score'])
    totalCount = len(uniquePlayerScores)
    
    jsonDict = prepareJsonDict(highestScore, totalCount)
    
    highestCount:int = 0
    for playerID in uniquePlayerScores:
        barIndex = min(int((uniquePlayerScores[playerID] / highestScore) * 10), 9)
        jsonDict["values"][barIndex]["count"] += 1
        highestCount = max(highestCount, jsonDict["values"][barIndex]["count"])
    
    jsonDict["highestCount"] = highestCount
    
    print(f"\n'level{level}.json':\n{'-' * 14:}")
    pprint(jsonDict)
    
    # Activate when fake histograms are not needed anymore
    with open(f"level{level}.json", "w") as file:
        pprint(jsonDict, stream=file)
    with open(f"level{level}.json", "r") as file:
        fileContent = file.read()
    fileContent = fileContent.replace("'", "\"")
    with open(f"level{level}.json", "w") as file:
        file = file.write(fileContent)