from django.shortcuts import render ,redirect
from statictemplate.forms import Contactform


# Create your views here.
def contactsend(request):
    if request.method == "POST":
        form =Contactform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/contact')
            except:
                    pass
    else:
        form =Contactform()
        return render(request, 'contact.html', {'forms':form})

def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request, "contact.html")
def index(request):
    return render(request,"index.html")
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,"about.html")
def projects(request):
    return render(request,'projects.html')
def proj1(request):
    return render(request,"proj1.html")
def singlepost(request):
    return render(request,"singlepost.html")
def test(request):
    return render(request,"test.html")