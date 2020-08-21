import xml.etree.ElementTree as ET
mytree = ET.parse('doc2.xml')
myroot = mytree.getroot()
print("/\/\/\/\/\/\/\/ XLM \/\/\/\/\//\/\/")
for x in myroot.findall('registro'):
    nombre=x.find('nombre').text
    apellido = x.find('apellido').text
    edad = x.find('edad').text
    color = x.find('color').text
    tipo = type(color)
    print('\n',nombre,'\n',apellido,'\n',edad,'\n',color,'\n','tipo : ',tipo,'\n')
