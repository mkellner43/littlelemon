from django.forms import DateTimeInput, ModelForm

from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {"date": DateTimeInput(attrs={"type": "datetime-local"})}
