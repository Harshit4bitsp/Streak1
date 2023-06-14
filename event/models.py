from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from phonenumber_field.modelfields import PhoneNumberField

class user(models.Model):
    id=models.AutoField(primary_key = True)
    phone_number=PhoneNumberField(unique=True)
    created_at= models.DateTimeField(default=timezone.now)
    user_types=[("T","Teen"),
               ("P","Parent"),
               ("B","Both")
               ]
    user_type=models.CharField(max_length=10,choices=user_types,default=True)
    total_points= models.IntegerField()
    def __str__(self):
        return str(self.phone_number)
    

class event(models.Model):
    user_types=[("T","Teen"),
               ("P","Parent"),
               ("B","Both")
               ]
    transaction_choices=[("C","Credit"),
                  ("D","Debit"),
                 ]
    id=models.AutoField(primary_key = True)
    event_tag=TaggableManager()
    created_at= models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(default=timezone.now)
    user_type=models.CharField(max_length=10,choices=user_types,default=True)
    transaction_type= models.CharField(max_length=10,choices=transaction_choices,default=True)
    points=models.IntegerField()
    percentage=models.IntegerField()

    def __str__(self):
        return str(self.id)


class event_log(models.Model):
    id= models.AutoField(primary_key = True)
    user_ref= models.ForeignKey(user, on_delete=models.CASCADE)
    event_ref=models.ForeignKey(event,on_delete=models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)
    # tranaction_choices=[("C","Credit"),
    #               ("D","Debit"),
    #              ]    
    # transaction_type= models.CharField(max_length=10,choices=tranaction_choices,default=True)
    opening_balance= models.IntegerField()

    def __str__(self):
        return str(self.event_ref.id)
    
    # testing