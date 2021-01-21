from django.shortcuts import render
import random


# Create your views here.


def generate_pass(request):
    context = {}
    return render(request, 'randomPass.html', context)


def show_pass(request):
    character = list('abcdefghijklmnopqrstuvwxyz123456789')
    length = int(request.GET.get('length'))
    uper_check = False
    special_check = False
    if request.GET.get('upercase'):
        uper_check = True
        character.extend('ABCDEFGHIJKLMNOPQESTUVWXYZ')
    if request.GET.get('specialCharacter'):
        special_check = True
        character.extend('!@#$%^&*(){}[]-_=+')
    random_pass = ''
    for i in range(length):
        random_pass += random.choice(character)
    context = {
        'password': random_pass,
        'uper_check': uper_check,
        'special_check': special_check,
        'length':length
    }
    return render(request, 'randomPass.html', context)
