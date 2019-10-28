from django.shortcuts import render


# Create your views here.
def index(request):
    title = 'Start'
    upperText = 'upper'
    lowerText = 'LOWER'
    return render(request, 'exampleFirst/index.html', {'sampleText' : title})