# this is my file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return render(request , 'index.html')
#     # return HttpResponse('''Harry  Django CodeWithHarry''')

# variables ko templates me kyse bheje
# def index(request):
#     params = {'name':'aman' , 'place':'Aliagrh'}
#     return render(request , 'index.html' , params)

def index(request):
    return render(request , 'index.html')

def about(request):
    return HttpResponse('about section')

def nevigator(request):
    s = '''<h1>navigator bar</h1><br> <a href ="https://www.linkedin.com/in/aman-sharma-01b185190/">  with aman </a>'''
    return HttpResponse(s)


# # Analyze text  index.html
# def analyze(request):
#     return render(request , 'index.html')
# def analyzer(request):
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)

#     remove_punc = request.GET.get('removepunc', 'off')
#     print(remove_punc)
#     # Analyze the text
#     return HttpResponse("remove punc")
# # Analyze text

# Analyze text  analyze.html
# def analyze(request):
#     return render(request , 'index.html')
# def analyzer(request):
#     # get the text
#     djtext = request.POST.get('text', 'default')  #djtext = request.GET.get('text', 'default')
#     print(djtext)

#     # remove_punc
#     remove_punc = request.POST.get('removepunc', 'off')
#     print(remove_punc)

#     # upper case
#     fullcasp = request.POST.get('fullcasp' , 'off')

#     # new line remover
#     newlineremover = request.POST.get('newlineremover' , 'off')

#     # extra space remover
#     extraspaceremover = request.POST.get('extraspaceremover' , 'off')

#     # character counter
#     charactercounter = request.POST.get('charactercounter' , 'off')


#     # Analyze the text
#     if remove_punc=="on":
#         punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
#         analyzed=""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         param = {'purpose':'Removed Punctuations' , 'analyzed_text':analyzed}
#         return render(request , 'analyze.html' , param)
    
#     elif(fullcasp=='on'):
#         analyzed=""
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#         param = {'purpose':'Changed to Uppercase' , 'analyzed_text':analyzed}
#         return render(request , 'analyze.html' , param)

#     elif(newlineremover=='on'):
#         analyzed = ""
#         for char in djtext:
#             if char!='\n' and char!="\r":
#                 analyzed = analyzed + char
#         param = {'purpose':'new line remover' , 'analyzed_text':analyzed}
#         return render(request , 'analyze.html' , param)

#     elif(extraspaceremover=='on'):
#         analyzed=""
#         for index , char in enumerate(djtext):
#             if not(djtext[index] == " " and  djtext[index+1]== " "):
#                 analyzed = analyzed+char
#         param = {'purpose':'extra remove space' , 'analyzed_text':analyzed}
#         return render(request , 'analyze.html' , param)

#     elif(charactercounter=='on'):
#         count=0
#         for char in djtext:
#             count = count+1
#         param = {'purpose':'count the character' , 'analyzed_text':count}
#         return render(request , 'analyze.html' , param)


    
#     else:
#         return HttpResponse("Error")

# Analyze text



# Analyze text ek saath sare toogle on krne k liye
def analyze(request):
    return render(request , 'index.html')
def analyzer(request):
    # get the text
    djtext = request.POST.get('text', 'default')  #djtext = request.GET.get('text', 'default')
    print(djtext)

    # remove_punc
    remove_punc = request.POST.get('removepunc', 'off')
    print(remove_punc)

    # upper case
    fullcasp = request.POST.get('fullcasp' , 'off')

    # new line remover
    newlineremover = request.POST.get('newlineremover' , 'off')

    # extra space remover
    extraspaceremover = request.POST.get('extraspaceremover' , 'off')

    # character counter
    charactercounter = request.POST.get('charactercounter' , 'off')


    # Analyze the text
    if remove_punc=="on":
        punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose':'Removed Punctuations' , 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request , 'analyze.html' , param)
    
    if(fullcasp=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose':'Changed to Uppercase' , 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request , 'analyze.html' , param)

    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!="\r":
                analyzed = analyzed + char
        param = {'purpose':'new line remover' , 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request , 'analyze.html' , param)

    if(extraspaceremover=='on'):
        analyzed=""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and  djtext[index+1]== " "):
                analyzed = analyzed+char
        param = {'purpose':'extra remove space' , 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request , 'analyze.html' , param)

    if(charactercounter=='on'):
        count=0
        for char in djtext:
            count = count+1
        param = {'purpose':'count the character' , 'analyzed_text':count}
        djtext = analyzed
        # return render(request , 'analyze.html' , param)

    
    if(remove_punc!="on" and fullcasp!='on' and newlineremover!='on' and extraspaceremover!='on' and charactercounter!='on'):
            return HttpResponse("Error")
    return render(request , 'analyze.html' , param)
# Analyze text ek saath sare toogle on krne k liye








