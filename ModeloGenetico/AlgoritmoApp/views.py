from django.shortcuts import render, redirect, reverse
from .forms import *
from .AlgoritmoGenetico import *
from django.http import HttpResponseRedirect
# Create your views here.
import csv
Solucion = [0.0,0.0,0.0,0.0]

def ParametrosAlgoritmo(request,id=0):
    
    if request.method == 'POST':
        if id == 1:
            data=request.POST
            #print(data['archivo'])
            ##print(data['finalizacion'])
            #print(data['padres'])
            
            archivo = "C:\\Users\\eddja\\Desktop\\Vacas Diciembre 2020\\IA\\LAB\\Practica1\\"+data['archivo']
            print(archivo)
            notas=[]
            with open(archivo) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    notas.append([row['PROYECTO 1'], row['PROYECTO 2'],row['PROYECTO 3'],row['PROYECTO 4'],row['NOTA FINAL']])
                    #print(row['PROYECTO 1'], row['PROYECTO 2'],row['PROYECTO 3'],row['PROYECTO 4'])
            #print(notas)
            sol = ejecutar(notas,data['finalizacion'],data['padres'],data['archivo'])
            print(sol)
            setSolucion(sol)
        if id == 2:
            data=request.POST
            print(data['p1'])
            print(data['p2'])
            print(data['p3'])
            print(data['p4'])
            print(Solucion)
            NC1 = float(data['p1']) * Solucion[0]
            NC2 = float(data['p2']) * Solucion[1]
            NC3 = float(data['p3']) * Solucion[2]
            NC4 = float(data['p4']) * Solucion[3]
            NF = NC1 + NC2 + NC3 + NC4
            print("Nota final predicha: ", str(NF))
            return render(request,'home.html',{'message':NF})
        return HttpResponseRedirect('/ParametrosAlgoritmo/')
    else:
        form = UploadFileForm()

    return render(request,'home.html',{'form':form})

def setSolucion(solu):
    global Solucion
    Solucion = solu
    print(Solucion)
