from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        # The fields are from contrib.auth. the form will give access to thous fields
        fields =('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Give label to the field like in html it will show on the HTML
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'Email address'
