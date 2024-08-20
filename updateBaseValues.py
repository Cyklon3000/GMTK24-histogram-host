import json
import pprint

for i in range(1, 4):
    data = None
    with open('level' + str(i) + '.json', 'r') as file:
        print(file)
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
    
    pprint.pprint(data, compact=False)
    
    with open('level' + str(i) + '.json', 'w') as file:
        pretty_json_str = pprint.pformat(data, compact=False).replace("'",'"')
        pretty_json_str = pretty_json_str\
            .replace('{"highestCount":', '{\n "highestCount":')\
            .replace('\n "', '\n    "')\
            .replace('"values": [{', '"values": [\n            {')\
            .replace('            ', '        ')\
            .replace(']}', '\n    ]\n}')
        print(json.dumps(data, indent=4))
        input("Press Enter to continue...")
        file.write(pretty_json_str)
        