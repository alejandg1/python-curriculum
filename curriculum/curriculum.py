import pdfkit
import jinja2
from datetime import datetime

info={}
info['fecha']=datetime.now().strftime('%A-%B-%Y')
info['nombre']= 'José Alejandro'
info['apellidos']='Gómez Paredes'
info['cedula']='091243423'
info['sexo']='M'
info['nacimiento']='29/9/2003'
info['email']= 'jgomezp4@unemi.edu.ec'
info['estado']= 'soltero'
info['domicilio']= 'cdla. El Recreo 5ta etapa'
info['cursos']= "CS50's Introduction to Computer Science"
info['firmas']= 'Alejandro Gómez'
info['colegio'] = 'Unidad educativa Durán '
info['escuela'] = 'semillitas de esperanza'
info['universidad']= 'Universidad estatal de Milagro'
context = {'info':info}
tempLoader = jinja2.FileSystemLoader('C:/Users/USUARIO/Music/Workspace/projects/curriculum-py/curriculum')
envTemp = jinja2.Environment(loader=tempLoader)
htmlTemp = 'index.html'
template = envTemp.get_template(htmlTemp)
text = template.render(context)
ejecutableWkt = b'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
configuracion = pdfkit.configuration(wkhtmltopdf=ejecutableWkt)
pdf = 'Curriculum.pdf'
pdfkit.from_string(text, pdf, configuration=configuracion)
