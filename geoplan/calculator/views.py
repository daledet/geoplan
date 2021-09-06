from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def home(request):
    return render(request, 'home.html', {})


def project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # for debugging only, handle according to your need
            print("Invalid input from user")

    form = ProjectForm()
    all_items = Project.objects.all()

    return render(request, 'project.html', {'form': form, 'all_items': all_items})


def input(request):
    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        return render(request, "input.html", {'num1': num1})

    return render(request, "input.html", {})
