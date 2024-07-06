from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import GuestBook, status_choices
from webapp.forms import GuestForm
from webapp.validate import note_validate

# Create your views here.
def index(request):
    guests = GuestBook.objects.all()
    return render(request, 'index.html', context={"guests": guests})

def create_note(request):
    if request.method == "GET":
        form = GuestForm()
        return render(request, "create_note.html", {"form": form})
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        guest_note = request.POST.get("guest_note")

        note = GuestBook(
            name=name,
            email=email,
            guest_note=guest_note
        )

        errors = note_validate(note)
        if not errors:
            note.save()
        form = GuestForm(data=request.POST)
        if form.is_valid():
            note = GuestBook.objects.create(
                name=name,
                email=email,
                guest_note=guest_note
            )
            return redirect("main")

        return render(
            request,
            "create_note.html",
            {"errors": errors, "note": note},
            {"form": form}
        )

def update_note(request, *args, pk, **kwargs):
    if request.method == "GET":
        note = get_object_or_404(GuestBook, pk=pk)
        form = GuestForm(initial={
            "name": note.name,
            "email": note.email,
            "guest_note": note.guest_note,
        })
        return render(
            request, "update_note.html",
            context={"form": form}
        )
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            note = get_object_or_404(GuestBook, pk=pk)
            note.name = form.cleaned_data['name']
            note.email = form.cleaned_data['email']
            note.guest_note = form.cleaned_data['guest_note']
            note.save()
            return redirect("main")
        else:
            return render(
                request,
                "update_note.html",
                {"form": form}
            )