from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, TableStyle, Table
from reportlab.lib import colors

def generate_pdf(data, file_name = None):

    doc = SimpleDocTemplate(file_name or 'report.pdf', pagesize=letter)
    header = ['Project', 'Open issues', 'Closed issues', 'Completed tasks', 'Pull requests', 'Conclusion (%)']

    table_data = []

    for row in data:
        table_data.append(header)
        table_data.append(row)
    
    print(table_data)

    t = Table(table_data, 6*[1.2*inch], len(table_data)*[0.4*inch])

    t.setStyle(TableStyle([
        ('ALIGN',(1,1),(-2,-2),'RIGHT'),
        ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
        ('VALIGN',(0,0),(0,-1),'TOP'),
        ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
        ('ALIGN',(0,-1),(-1,-1),'CENTER'),
        ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
        ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ]))

    doc.build([t])