from django.contrib import admin
from .models import event_log,event,user

admin.site.register(event_log)
admin.site.register(event)
admin.site.register(user)

# class event_admin(admin.ModelAdmin):
#     fields=('add_event_tag','add_date','the_user','transaction_type','add_points')
# admin.site.register(add_Event,event_admin)
# Register your models here.
