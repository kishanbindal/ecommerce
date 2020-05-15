from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from Users.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('phone_number',)


class CustomUserAdmin(UserAdmin):
    pass

# class UserAdmin(BaseUserAdmin):
#     add_form = CustomUserCreationForm
#
#     add_fieldsets =
# Register your models here.

admin.site.register(User, CustomUserAdmin)
