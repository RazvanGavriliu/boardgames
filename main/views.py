from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, "main/home.html",{'message':'Hi, there!'})


def formular(request):
    return render(request, "main/formular.html")


def formular_submit(request):
    return render(request, "main/raspunsformular.html",{'name':request.POST['nume'],'prenume':request.POST['prenume'],'trimite':request.POST['trimite']})


from .forms import PersonForm
from .models import Person

def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            # print(cd['nume'])
            # print(cd['email'])
            # print(cd['phonenumber'])
            cd = form.cleaned_data
            person = Person()
            person.nume = cd['nume']
            person.mail = cd['email']
            person.phonenumber = cd['phonenumber']
            person.save()
            form = PersonForm()
        else:
            print("Form is not valid")
    else:
        form = PersonForm()

    return render(request, 'main/contact_form.html', {'form': form})


def persons(request):
    if request.method == 'GET':
        persons_obj = Person.objects.all()

    return render(request, 'main/persons.html', {'persons': persons_obj})


def deleteperson(request, id):
    print(id)
    print(Person.objects.all())
    Person.objects.all().filter(pk=int(id)).delete()
    print(Person.objects.all())
    persons_obj = Person.objects.all()
    return render(request, 'main/persons.html', {'persons': persons_obj})



