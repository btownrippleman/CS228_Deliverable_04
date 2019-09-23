from xhtml2pdf import pisa
from io import StringIO
from django.template.loader import get_template
from django.template import Context


def html_to_pdf_directly(request):

	template = get_template("template_name.html")
	context = Context({'pagesize':'A4'})
	html = template.render(context)
	result = StringIO.StringIO()
	pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	else: return HttpResponse('Errors')

site = "www.google.com"

html_to_pdf_directly(site)