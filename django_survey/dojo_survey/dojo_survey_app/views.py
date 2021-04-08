from django.shortcuts import render, redirect

def index(request):
        return render(request, "index.html")
    

def result(request):
    if request.method == "POST":
        context = {
            'name':request.POST['name'],
            'gender':request.POST['gender'],
            'language':request.POST['language'],
            'location':request.POST['location']
        }
        return render(request, "result.html", context)