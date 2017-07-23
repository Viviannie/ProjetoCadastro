from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager #Provê o esqueleto básico de um usuário                                                                         
from django.contrib.auth.models import PermissionsMixin                     #Framework de permissões para usuário

#E-mail do usuário personalizado
class EmailUserManager(BaseUserManager):    
    
    #Cria e salva um usuário com e-mail, senha
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:   #Se o e-mail não for informado, exibe mensagem de erro
            raise ValueError(('Usuário deve inserir um endereço de e-mail.'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user    

    #
    def create_superuser(self, *args, **kwargs):    #Funcionalidades de controle de superusuário 
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using = self._db)
        return user

class MyUser(PermissionsMixin, AbstractBaseUser):   #Usuário personalizado que herda de PermissionsMixin e de AbstractBaseUser

    email = models.EmailField(
        verbose_name = ('Endereço de E-mail'),
        unique = True,
    )

    nome = models.CharField(            #Para alterar padrões do nome.
        verbose_name = ('Nome'),
        max_length = 50,
        blank = False,  #Não permite um valor 'vazio'
        help_text = ('Informe seu nome completo.'),     #Campo de ajuda para preenchimento do nome.
    )   

    #O e-mail do usuário é usado para identifica-lo durante o login
    USERNAME_FIELD = 'email'
    objects = EmailUserManager()