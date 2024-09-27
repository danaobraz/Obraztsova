from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    name = 'Bohdana'
    surname = 'Obraztsova'
    second_name = 'Serhiivna'
    time = datetime.now()
    response = f"Hello, World! My name is {surname} {name} {second_name}. Current time: {time.strftime('%d-%m-%Y %H:%M:%S')}"
    return HttpResponse(response)