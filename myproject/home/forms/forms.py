from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date"
            },
        ),
        required=False  # Make this field optional
    )

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "full_name",
            "phone_number",
            "date_of_birth",
            "address_1",
            "address_2",
            "gender",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get("class") is None:
                field.widget.attrs["class"] = "form-control"
            field.required = False  # Make all fields optional (can remove this if not needed)
