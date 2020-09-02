import webbrowser
import os
nombre=["Jose","Mario","Maria","Marcos","Miriam","Moises","Martin","Duglas","Dora","Dambio"]
edad=["30","43","45","221","22","23","34","54","22","71"]
activo=["True","False","True","True","False","False","False","True","True","False"]
saldo=["450","305","530","324","500","600","700","800","900","1000"]

contador = 0
guardarRegistro=""
while contador < 10:
    guardarRegistro=guardarRegistro+f"<tr><td>{nombre[contador]}</td><td>{edad[contador]}</td><td>{activo[contador]}</td><td>{saldo[contador]}</td></tr>"
    contador = contador + 1
myFile = open("registros.html", "w")
docHTML = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>REGISTROS</title>
</head>
<body>
   <table width="100%" border="1">
        <tr>
        	<div align="center"><strong>Registros</strong></div>
        </tr>
        <tr>
            <td>nombre</td>
            <td>edad</td>
            <td>activo</td>
            <td>saldo</td>
        </tr>
        <tr>{guardarRegistro}</tr>
    </table>
</body>
</html>
"""

myFile.write(docHTML)
myFile.close()
webbrowser.open_new_tab("registros.html")