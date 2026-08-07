#accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
class CustomUSerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")

class CustomUSerChangeForm(UserChangeForm):
    class MEta(UserChangeForm.Meta):
        model = CustomUser
        fields = ("username", "email")

