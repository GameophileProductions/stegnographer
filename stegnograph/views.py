from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')

def view(request):
    if request.method == "POST":
        pass
    return render(request, 'base.html')