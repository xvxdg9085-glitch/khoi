from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model

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
class CustomerLoginForm(forms.Form):
    username = forms.CharField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"})
    )
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password.")
        return cleaned_data