from django.urls import path
from . import views
from .views import EventDetailView,EventListView,AddEventListView,UserListView


urlpatterns = [
    path('', views.home, name='event-home'),
    # path('events/',views.event_view, name='event-view'),
    path('events/',views.EventListView.as_view(), name='event-view'),
    path('users/',views.UserListView.as_view(), name='user-view'),
    path('viewevents/',views.AddEventListView.as_view(), name='add_event-view'),
    path('events/<int:pk>',views.EventDetailView.as_view(), name='event-detail'),
    path('events/add/',views.add_event, name='add-event'),
    path('events/edit',views.add_event, name='edit-event'),
]