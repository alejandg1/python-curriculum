import pdfkit
import jinja2
from datetime import datetime

info={}
info['fecha']=datetime.now().strftime('%A-%B-%Y')
info['nombre']= 'José Alejandro'
info['apellido']='Gómez Paredes'
info['descripcion']=''
info['educacion']='Estudios en curso: ingenieria en software'
info['experiencia']='sin experiencia laboral'

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
