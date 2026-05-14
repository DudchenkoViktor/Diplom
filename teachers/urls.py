from django.urls import path
from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('',  views.RosterView.as_view(), name='roster'),
    path('search/',  views.RosterView.as_view(), name='search'),
    path('forms/<slug:mentors_slug>/', views.MentorView.as_view(), name='mentors'),
    path('complaint/', views.ComplaintView.as_view(), name='complaint'),
]
