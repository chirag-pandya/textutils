from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("<h2>This is Home Page </h2>")
    # params = {'name':'chirag', 'place':'Mars'}
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spacemover = request.POST.get('spacemover', 'off')

    # analyze the text.
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Full Capital','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html', params)

    if spacemover == "on":
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'Sapce Remove', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spacemover != "on"):
        return HttpResponse("Error!!! You have Not selected any Options")
    return render(request, 'analyze.html', params)