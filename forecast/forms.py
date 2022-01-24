from django import forms


FORECAST_CHOICES = (
    ("0", "---"),
    ("1", "Srebrna Góra"),
    ("2", "Czarna Góra"),
    ("3", "Rychleby"),
    ("4", "Kouty"),
    ("5", "Bielsko-Biała"),
)


class ForecastForm(forms.Form):
    location = forms.ChoiceField(label='Miejscówka', choices=FORECAST_CHOICES)

    def clean(self):
        cleaned_data = super().clean()

        if self.cleaned_data["location"] != "0":
            return cleaned_data
        else:
            raise forms.ValidationError("Wybierz lokalizację.")