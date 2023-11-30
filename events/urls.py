# events/urls.py
from django.urls import path, include
from .views import EventViewSet, book_event, UserRegisteredEventsAPIView, UnregisterFromEventAPIView, eventSearchView
from rest_framework.routers import DefaultRouter
from. import views

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')


urlpatterns = [
    path('', include(router.urls), name="event-list"),
    path('events/<int:event_id>/book/', book_event, name='book-event'),
    path('registered-events/', UserRegisteredEventsAPIView.as_view(), name='registered-events'),
    path('unregister/<int:pk>/', UnregisterFromEventAPIView.as_view(), name='unregister-from-event'),
    path('search-event/', views.eventSearchView.as_view({'get': 'list'}), name='search_event')

    # path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),
    # path('events/<int:pk>/register/', EventRegistrationView.as_view(), name='event-registration'),
]

