from logging import disable
from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class Event(models.Model):
    """
    Storing the Events
    """
    Title = models.CharField("Title", max_length=100, blank=True)
    description = models.TextField("Description")
    logo = models.URLField("Logo", max_length=200)
    treshold = models.PositiveIntegerField("Treshold", blank=True)
    #Event_Time = models.TimeField("Event_Time", auto_now=False, auto_now_add=False)
    Repeat_all_Day = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    Repeat = models.PositiveIntegerField("Repaet('Day')", blank=True, default=0)
    Upcoming_DateTime = models.DateTimeField("Upcoming_DateTime", auto_now=False, auto_now_add=False)
    created = models.DateTimeField("Created_Date", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)

class CustomUserManager(BaseUserManager):
    """
    custom user model manager where email is the unique 
    identifiers for authentication instead of username
    """
    def create_user(self, email, password, **extra_fields):
        """
        create and save a User with the given email and password
        """
        if not email:
            raise ValueError(_('the Email must be Set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
       """
       create and save a SuperUser with the given email and password
       """
       extra_fields.setdefault('is_staff',True)
       extra_fields.setdefault('is_superuser',True)
       extra_fields.setdefault('is_active',True)
       if extra_fields.get('is_staff') is not True:
            raise ValueError(_('super user must have is_staff = True.'))
       if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser = Ture.'))
       return self.create_user(email, password,extra_fields)



#class MyUser(AbstractBaseUser, PermissionsMixin):
#    email = models.EmailField(max_length=255, unique=True)
#    is_superuser = models.BooleanField(default=False)
#    is_staff = models.BooleanField(default=False)
#    is_active = models.BooleanField(default=True)
#    USERNAME_FIELD = 'email'
#    created_date = models.DateTimeField(auto_now_add=True)
#    updated_date = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.email
