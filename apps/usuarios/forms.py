from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

#Estendido de AbstractUser ou AbstractBaseUser?
class CustomUserCreationForm(UserCreationForm):	#Form para criar novo usuário

    class Meta:
    	
        model = MyUser
        fields = ['nome', 'email']