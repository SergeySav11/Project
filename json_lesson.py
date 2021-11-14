import json
'''
with open('json.json') as infile:
    a = json.load(infile)
print(a['string_key'])
b = True
a['boolean_key'] = b
with open('json.json','w') as outfile:
    json.dump(a,outfile)
'''
a = dict()
a = {'Соболева Александра Даниловна': 'Соболева Александра Даниловна' ,'Шилова Варвара Ивановна': 'Шилова Варвара Ивановна' ,'Степанов Михаил Владимирович': 'Степанов Михаил Владимирович','':''}
running = True
with open('json.json','a',encoding='utf-8') as infile:
    while running:
        g = a[input()]
        infile.write(str(g))
        if g == '':
            running = False
    v = a
    infile.write(str(v))