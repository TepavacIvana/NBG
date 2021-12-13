from django.urls import path
from korisnik import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('registration/', views.UserList.as_view()),
    path('login/', views.Loger.as_view()),
    path('registration/<id>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
