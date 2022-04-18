from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):

    context ={
        "variable":"Anand Sahu"
    }
    return render(request,'index.html')
    # return HttpResponse("this is homepage")

def pritam(request):
    return render(request,'pritam.html')
    # return HttpResponse("this is about")

# def group(request):
#     return render(request,'group.html')
    # return HttpResponse("this is about")

def team(request):
    return render(request,'team.html')
    # return HttpResponse("this is about")

def research(request):
    return render(request,'research.html')
    # return HttpResponse("this is about")

def researchpaper(request):
    return render(request,'researchpaper.html')
    # return HttpResponse("this is about")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services")

def contact(request):
    if request.method=="POST":
        print(request)

        name=request.POST.get('name','')
        print(name)

        email=request.POST.get('email','')
        print(email)

        message=request.POST.get('message','')
        print(message)

        # contact=Contact(name=name,email=email,message=message)
        # contact.save()
        
    return render(request,'contact.html')
    # return HttpResponse("this is contact")

def pritam2(request):
    return render(request,'pritam2.html')
    # return HttpResponse("this is contact")


def book(request):
    return render(request,'book.html')
    # return HttpResponse("this is contact")


def patent(request):
    return render(request,'patent.html')
    # return HttpResponse("this is contact")


def reviews(request):
    return render(request,'reviews.html')
    # return HttpResponse("this is contact")

def Research_overview(request):
    return render(request,'Research_overview.html')
    # return HttpResponse("this is contact")


def researchA(request):
    return render(request,'researchA.html')
    # return HttpResponse("this is contact")

def researchB(request):
    return render(request,'researchB.html')
    # return HttpResponse("this is contact")

def researchC(request):
    return render(request,'researchC.html')
    # return HttpResponse("this is contact")

def researchD(request):
    return render(request,'researchD.html')
    # return HttpResponse("this is contact")

def researchE(request):
    return render(request,'researchE.html')
    # return HttpResponse("this is contact")

def researchF(request):
    return render(request,'researchF.html')
    # return HttpResponse("this is contact")

def researchG(request):
    return render(request,'researchG.html')
    # return HttpResponse("this is contact")

def coverpages(request):
    return render(request,'coverpages.html')
    # return HttpResponse("this is contact")

def gallery(request):
    return render(request,'gallery.html')
    # return HttpResponse("this is contact")

def labtour(request):
    return render(request,'labtour.html')
    # return HttpResponse("this is contact")





