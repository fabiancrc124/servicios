from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def crearSiniestro(request):
    if request.method == 'POST':
        # Obtén el contenido XML de la solicitud
        xml_content = request.body
        xml_respuesta = '<?xml version="1.0" encoding="utf-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><ns1:ClaimsModifyResponse xmlns:ns1="http://www.example.org/ServicioSiniestros2/"><Code xmlns="">0</Code><Message xmlns="">Siniestro Procesado. Numero: 26692 - Año Ejercicio: 126241/2021 - Poliza: 8057015900</Message><IdData xmlns="">90543568</IdData></ns1:ClaimsModifyResponse></soapenv:Body></soapenv:Envelope>'

        # Aquí puedes procesar el XML recibido y realizar cualquier lógica necesaria
        # En este ejemplo, simplemente devolvemos el mismo XML en la respuesta SOAP
        response = xml_respuesta
        return HttpResponse(response, content_type='text/xml')

    return HttpResponse(status=405)


@csrf_exempt
def ordendePago(request):
    if request.method == 'POST':
        # Obtén el contenido XML de la solicitud
        xml_content = request.body
        xml_respuesta = '<?xml version="1.0" encoding="utf-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><ns1:CreateRequestResponse xmlns:ns1="http://www.example.org/ServicioSiniestros2/"><Code xmlns="">0</Code><Message xmlns="">Siniestro Procesado. Numero: 26692 - nro_liquid_sis: 20210015743 - Año Ejercicio: 124007/2021 - Poliza: 8051525700</Message><IdData xmlns="">90541443447668</IdData></ns1:CreateRequestResponse></soapenv:Body></soapenv:Envelope>'

        # Aquí puedes procesar el XML recibido y realizar cualquier lógica necesaria
        # En este ejemplo, simplemente devolvemos el mismo XML en la respuesta SOAP
        response = xml_respuesta
        return HttpResponse(response, content_type='text/xml')

    return HttpResponse(status=405)


@csrf_exempt
def crearTercero(request):
    if request.method == 'POST':
        # Obtén el contenido XML de la solicitud
        xml_content = request.body
        xml_respuesta = '''<?xml version='1.0' encoding='utf-8'?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><ns1:ThirdProcessResponse xmlns:ns1="http://www.example.org/ServicioSiniestros2/"><Code>0</Code><Message>El tercero se ha creado Exitosamente</Message><IdData>11020482161</IdData></ns1:ThirdProcessResponse></soapenv:Body></soapenv:Envelope>'''

        # Aquí puedes procesar el XML recibido y realizar cualquier lógica necesaria
        # En este ejemplo, simplemente devolvemos el mismo XML en la respuesta SOAP
        response = xml_respuesta
        return HttpResponse(response, content_type='text/xml')

    return HttpResponse(status=405)