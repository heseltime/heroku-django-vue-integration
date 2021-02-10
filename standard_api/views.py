from django.shortcuts import render

from django.http import JsonResponse

def knight_names(request):
    return JsonResponse({'names': ['William', 'Roderick', 'Frank']})
