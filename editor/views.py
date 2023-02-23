from django.shortcuts import render
from . import plotlyeditor

# Create your views here.

def main(request):

    context = {'context':'context'}
    return render(request, 'editor/main.html', context)