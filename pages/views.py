from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'pages/index.html')


def aboutus(request):
    name = "John"
    student = {
        1: "John", 2: "Jane", 3:"blake", 4: "Kriti"
    }

    results = {
        1 : {"name" : "john", "cgpa" : [6,2, 9.8, 9.1, 9.7]},
        2 : {"name" : "sam", "cgpa" : [6,2, 9.8, 9.1, 9.7]},
        3 : {"name" : "jam", "cgpa" : [6,2, 9.8, 9.1, 9.7]},
        4 : {"name" : "tina", "cgpa" : [6,2, 9.8, 9.1, 9.7]},
        5 : {"name" : "trevour", "cgpa" : [6,2, 9.8, 9.1, 9.7]}
    }
    context = {
        "name" : "Sam",
        "age" : 20,
        "num1" : 12,
        "num2" : 10,
        "k" : [1,2,3,4,5],
        "students" : student,
        "results" : results
    }


    return render(request, "pages/about.html", context)


def form(request):
    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'pages/form.html', context)