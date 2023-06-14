from django.views.generic import ListView,DetailView
from django.shortcuts import render
from .models import event,user,event_log



def home(request):
        return render(request, 'event/home.html')

# def event_view(request):
#         # ev=Event.objects.all()
#         # context={
#         #         'event_ref':ev.event_ref
#         # }

#         context={
#                 'events':event.objects.all()
#         }
#         return render(request,'event/events.html',context)
class EventListView(ListView):
        model=event
        template_name='event/event_log.html'
        context_object_name='events'
        ordering=['-event_date']

class UserListView(ListView):
        model=user
        template_name='event/user.html'
        context_object_name='view_users'
        # ordering=['-event_date']

class AddEventListView(ListView):
        model=event
        template_name='event/event.html'
        context_object_name='add_Event'
        ordering=['event_id']

class EventDetailView(DetailView):
        model=event
        template_name='event/event_detail.html'
        context_object_name='add_Event'
        # ordering=['-event_date']
# Create your views here.

def add_event(request):
        return render(request, 'event/addevent.html')
