""" Utility code for the report apps"""
import uuid,base64,os
from io import BytesIO
from django.core.files.base  import ContentFile
from .models import Report
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from django.conf import settings

def get_report_image(data):
    """ this function takes a base64 encoded string gotten from the formdata image src, and converts it to a file like object that can be saved as a png image"""

    _,str_image = data.split(";base64")
    decoded_image = base64.b64decode(str_image)
    img_name =str(uuid.uuid4())[:10]+".png"
    data = ContentFile(decoded_image,name=img_name)
    return data

def get_report_pdf(report_pk):
	""" This function takes a report model object pk or id as an input. creates a pdf file using reportlab module. call the cleanup() function to delete the created pdf file. 
	"""
	report = Report.objects.get(id = report_pk)
	name = report.name + str(report.id)+ "_ralchemy.pdf"
	remark = report.remark
	author = report.author.user.username
	created = report.created.strftime("%h %d,%Y. %H:%M %P")
	image_path = os.path.abspath("") + report.image.url
	print(image_path)
	# Create the PDF document
	doc = SimpleDocTemplate(name, pagesize=A4)
	story = []
	# Load styles
	styles = getSampleStyleSheet()
	h1 = styles["Heading1"]
	h2 = styles["Heading2"]
	body_text = styles["BodyText"]
	
	# Add Header
	story.append(Paragraph("SALES REPORT", h1))
	story.append(Spacer(1, 0.2 * inch))
	
	# Add Image
	img = Image(image_path, width=4 * inch, height=3 * inch)
	story.append(img)
	story.append(Spacer(1, 0.25 * inch))
	
	# Add Paragraph
	story.append(Paragraph("Remark",h2))
	story.append(Paragraph(remark,body_text))
	story.append(Paragraph("Author",h2))
	story.append(Paragraph(author,body_text))
	story.append(Paragraph("Created",h2))
	story.append(Paragraph(created,body_text))
	
	# Build PDF
	doc.build(story)
	buffer = BytesIO()
	with open(name,'rb') as fd:
		buffer.write(fd.read())
		buffer.seek(0)
	return buffer,name
	
def cleanup(name):
	import os
	os.remove(name)

