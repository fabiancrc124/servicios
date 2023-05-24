from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# # Create your views here.
# @csrf_exempt
# def crearSiniestrorest(request):
#     if request.method == "post":
#         print(request.body)

#     return HttpResponse(f"Estas viendo los resultados de la pregunta numero ") 



# @soap_view(['InputType'], ['OutputType'])
# def crearSiniestro(request, input_data):
#     # Lógica para procesar la solicitud SOAP y generar una respuesta
#     return output_data


@csrf_exempt
def crearSiniestro(request):
    if request.method == 'POST':
        # Obtén el contenido XML de la solicitud
        xml_content = request.body

        # Aquí puedes procesar el XML recibido y realizar cualquier lógica necesaria
        # En este ejemplo, simplemente devolvemos el mismo XML en la respuesta SOAP
        response = f'<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body>{xml_content}</soapenv:Body></soapenv:Envelope>'
        return HttpResponse(response, content_type='text/xml')

    return HttpResponse(status=405)