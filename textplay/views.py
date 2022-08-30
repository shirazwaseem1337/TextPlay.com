#This is the file I created

from http.client import HTTPResponse
from os import remove
from django.http import HttpResponse
from django.shortcuts import render;


def index(request):
    # params={'name':'shiraz','age':17}
    return render(request,'index.html')

def analyze(request):
    djtext= request.POST.get('text','default')
    removepunc= request.POST.get('punctuationremoved','off') 
    captext=request.POST.get('capitalize','off')
    lineremover=request.POST.get('lineremover','off')
    extraspaceremover=request.POST.get('spaceremover','off')

    print(djtext)
    

    # For removing punctuations
    if (removepunc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
    

        params={'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)



    #for capitalizing the text
    if (captext=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params={'purpose': "Capitalaizing text", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    #for removing the space between lines
    if (lineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\r" and char != "\n":
                analyzed=analyzed+char
        params={'purpose': "Line remover", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

        # For removing the space between the text
    if (extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose': "Extra Space remover", 'analyzed_text': analyzed}
        


    if(removepunc!='on' and extraspaceremover!='on' and lineremover!='on' and captext!='on'):
        return HttpResponse('Please enable any one of the options')

    return render(request,'analyze.html',params)

        


    






   
      









