import json
with open('doc1.json', 'r') as myfile:
    datos = myfile.read()
    objeto1 = json.loads(datos)

    print("/\/\/\/\/\/\/\/ JSON \/\/\/\/\//\/\/")
    print(json.dumps(objeto1, indent=3))
    print("tipo de objeto del registro: ", type(objeto1),"\n")
