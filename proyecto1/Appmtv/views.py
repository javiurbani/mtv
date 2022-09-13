from django.shortcuts import render
from django.http import HttpResponse
from Appmtv.models import Familia
from django.template import loader

def familia(self):
    familia1 = Familia(nombre = "Leandro", edad = 35, fecha_nac = "1986-1-12")
    familia1.save()

    familia2 = Familia(nombre = "Natalin", edad = 36, fecha_nac = "1985-4-6")
    familia2.save()

    familia3 = Familia(nombre = "Susana", edad = 42, fecha_nac = "1980-5-10")
    familia3.save()

    diccionario = {
        "name1": familia1.nombre, "age1": familia1.edad, "birth1": familia1.fecha_nac,
        "name2": familia2.nombre, "age2": familia2.edad, "birth2": familia2.fecha_nac,
        "name3": familia3.nombre, "age3": familia3.edad, "birth3": familia3.fecha_nac
        }
    
    plantilla = loader.get_template("familiar.html")
    document = plantilla.render(diccionario)

    return HttpResponse(document)