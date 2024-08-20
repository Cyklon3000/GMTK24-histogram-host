import json
for i in range(1, 4):
    data = None
    with open('level' + str(i) + '.json', 'w') as file:
        data = json.load(file)
    
    highestCount = 0
    highestScore = 0
    totalCount = 0
    for j in range(len(data['values'])):
        values = data['values'][j]
        highestCount = max(highestCount, values['count'])
        highestScore = max(highestScore, values['max'])
        totalCount += values['count']
    
    data["highestCount"] = highestCount
    data["highestScore"] = highestScore
    data["totalCount"] = totalCount
    with open('level' + str(i) + '.json', 'w') as file:
        json.dump(data, file)