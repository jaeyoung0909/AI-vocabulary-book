from django.urls import path

from . import views 

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('initUserAbility/', views.initUserAbility, name='initUserAbility'),
    path('updateUserAbility/', views.updateUserAbility, name='updateUserAbility'),
    path('getFreqWords/', views.getFreqWords, name='getFreqWords')
    path('recommendedWords/', views.recommendedWords, name='recommendedWords'),
]