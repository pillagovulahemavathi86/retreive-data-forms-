from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic inserted successfully')
    return render(request,'insert_topic.html') 


def insert_webpage(request):
   
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['url']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=em)[0]
        WO.save()     
        return HttpResponse('webpage inserted successfully')   


    return render(request,'insert_webpage.html',d)


def insert_access(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}

    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        WO=Webpage.objects.get(name=na)
        AO=Accessrecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()

        return HttpResponse('accessrecord inserted successfully')
    return render(request,'insert_access.html',d)




def retrive_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrive_data.html',d)