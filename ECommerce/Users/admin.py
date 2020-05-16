from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Users.models import User


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)


UserAdmin.add_form = CustomUserCreationForm
UserAdmin.form = UserChangeForm
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2', 'phone_number'),
    }),
)
UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Contact Details'), {'fields': ('phone_number',)})
    )

admin.site.register(User, UserAdmin)
