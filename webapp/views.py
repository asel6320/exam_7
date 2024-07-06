from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import GuestBook, status_choices

# Create your views here.
def index(request):
    guests = GuestBook.objects.all()
    return render(request, 'index.html', context={"guests": guests})

def create_note(request):
    pass