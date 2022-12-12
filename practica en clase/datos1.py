import pdfkit
import jinja2
from datetime import datetime

data = {}
data['nombre'] = 'Jess'
data['hora'] = '60'
data['fecha'] = datetime.now().strftime('%d-%m-%Y')

context = {'data': data}
template_loader = jinja2.FileSystemLoader('D:/python--clase')
env_template = jinja2.Environment(loader=template_loader)

html_template = 'index.html'
template = env_template.get_template(html_template)
output_text = template.render(context)
path_wkthtmltopdf = b'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'

config = pdfkit.configuration(wkhtmltopdf=path_wkthtmltopdf)

output_pdf = 'certificado.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config)