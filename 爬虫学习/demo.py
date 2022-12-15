import json

dict1 = {'a':1, 'b':-1}

with open('demo.json', 'w', encoding='utf8') as f:
    json.dump(dict1, fp=f)

