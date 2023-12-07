# from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.forms import DateTimeInput

from .forms import BookingForm
from .models import Menu


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def book(request):
    form = BookingForm()
    if request.method == "POST":
        posted_form = BookingForm(request.POST)
        if posted_form.is_valid():
            posted_form.save()
            guest_number = posted_form.cleaned_data['guest_number']
            first_name = posted_form.cleaned_data['first_name']
            last_name = posted_form.cleaned_data['last_name']
            
            message_text = f'Your reservation has been made for {guest_number} guests under the name {first_name} {last_name}! Thank you for your reservation, we will see you soon.'
            messages.success(request, message_text)
            return render(request, "book.html", {'form': form})
    context = {"form": form}
    return render(request, "book.html", context)


# Add your code here to create new views


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})
