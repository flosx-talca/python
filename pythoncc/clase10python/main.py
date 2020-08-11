from xhtml2pdf import pisa
from jinja2 import  Template
import os

ruta= "/Applications/bitnami/apache2/htdocs/clase_10_python/"
sourcehtml= open(os.path.join(ruta, "archivo.html")).read()
outputfilename = ruta + "ejemplo.pdf"
data = {"nombre": "Nicolás ROzas", "ruta": ruta}
resultfile = open(outputfilename, "w+b")
#pisaStatus= pisa.CreatePDF(sourcehtml,dest=resultfile)
template = Template(open(os.path.join(ruta, "archivo.html")).read())
html = template.render(data)
pisaStatus = pisa.CreatePDF(html, dest=resultfile)
resultfile.close()



