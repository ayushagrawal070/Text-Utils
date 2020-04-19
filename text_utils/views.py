

from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     with open("one.txt") as f:
#         a = f.read()
#         return HttpResponse(a)

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>home page </h1> <a href = '/spaceremove' >go to space remover</a>")
def about(request):
    return render(request, 'aboutus.html')
def contact(request):
    return render(request, 'contactus.html')

def analyze(request):
    mytext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capital = request.POST.get('capital','off')
    newline = request.POST.get('newline','off')
    spaces = request.POST.get('spaces','off')
    original = mytext

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!@#$%^&*(){}[];~`-':"<>,./?\|'''
        for char in mytext :
            if char not in punctuations :
                analyzed += char
        mytext = analyzed

    if capital == "on" :
        analyzed = ""
        for char in mytext:
            analyzed += char.upper()
        mytext = analyzed

    if newline == "on":
        analyzed = ""
        for char in mytext:
            if char != "\n" and char != "\r":
                analyzed+=char
        mytext = analyzed

    if spaces == "on":
        analyzed = ""
        for index, char in enumerate(mytext):
            if mytext[index] == " " and mytext[index+1] == " " :
                pass
            else:
                analyzed+=char
        mytext = analyzed
    params = {'purpose': original, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

    if not removepunc == "on" and newline == "on" and spaces == "on" and capital == "on" :
        return HttpResponse("Please check any one box")

# def capfirst(request):
#     return HttpResponse("I WILL CAPITALIZE FIRST LETTER")
#
# def spaceremove(request):
#     return HttpResponse("I WILL REMOVE SPACES FROM SENTENCE")