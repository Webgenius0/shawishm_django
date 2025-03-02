from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not password:
            raise ValueError('The Password field must be set')
        
        username = self.model(username=username, **extra_fields)
        username.set_password(password)
        username.save()
        return username
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active' , True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, password,**extra_fields)