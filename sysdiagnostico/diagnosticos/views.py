from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io
from .models import Diagnosticos

class PDFGenerator(View):
    def get(self, request, pk):
        diagnostico = get_object_or_404(Diagnosticos, pk=pk)

        template_path = "D:\Desktop\ProyectoDiagnostico\sysdiagnostico\diagnosticos\Diagnostico_PDF.pdf"
        template_pdf = PdfReader(open(template_path, "rb"))
        output_pdf = PdfWriter()

        # Crea un objeto PDF utilizando ReportLab
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=(letter))

      


        # Agrega el contenido dinámico a tu diseño personalizado
        # Puedes usar las coordenadas exactas para ubicar tus datos en el diseño
        c.drawString(100, 700, f"ID: {diagnostico.ID}")
        c.drawString(100, 680, f"FechaSalida: {diagnostico.FechaSalida}")
        c.drawString(100, 660, f"Para: {diagnostico.Para}")
        c.drawString(100, 640, f"De: {diagnostico.De}")
        c.drawString(100, 620, f"FechaIngreso: {diagnostico.FechaIngreso}")
        c.drawString(100, 600, f"Asunto: {diagnostico.Asunto}")
        c.drawString(100, 580, f"PorEsteMedioEmito: {diagnostico.PorEsteMedioEmito}")
        c.drawString(100, 560, f"de: {diagnostico.de}")
        c.drawString(100, 540, f"DeLaOficina_Delegacion: {diagnostico.DeLaOficina_Delegacion}")
        c.drawString(100, 520, f"marca: {diagnostico.marca}")
        c.drawString(100, 500, f"modelo: {diagnostico.modelo}")
        c.drawString(100, 480, f"S_N: {diagnostico.S_N}")
        c.drawString(100, 460, f"color: {diagnostico.color}")
        c.drawString(100, 440, f"INV: {diagnostico.INV}")
        c.drawString(100, 420, f"situacion: {diagnostico.situacion}")
        c.drawString(100, 400, f"conclusión: {diagnostico.conclusión}")
        c.drawString(100, 380, f"identificador: {diagnostico.identificador}")

        # Guarda el contenido de ReportLab en el búfer
        c.save()
        buffer.seek(0)

        # Agrega el contenido del búfer a la página del diseño personalizado
        page = template_pdf.pages[0]
        page.merge_page(PdfReader(buffer).pages[0])
        output_pdf.add_page(page)
        # Crea un archivo PDF de salida para el resultado
        result_buffer = io.BytesIO()
        output_pdf.write(result_buffer)

        # Configura la respuesta del archivo PDF
        result_buffer.seek(0)
        response = HttpResponse(result_buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="Diagnosticos_{diagnostico.pk}.pdf"'

        return response
