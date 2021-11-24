from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Todo usuario debe ingresar un email")
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
            user = self.create_superuser(
                email=email,
                password=password
            )
            user.is_admin = True
            user.save(using=self._db)
            return user

class User(AbstractBaseUser, PermissionsMixin):
    id                  = models.BigAutoField(primary_key=True)
    email               = models.EmailField('Email', max_length = 100, unique =True)
    password            = models.CharField('Password', max_length = 256)
    name                = models.CharField('Name', max_length = 60)
    last_name           = models.CharField('Last Name', max_length = 60)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt) #decimos que la contraseña va a ser igual a la union de la contgra con el salt y el hasher para enciptarla
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD ='email'