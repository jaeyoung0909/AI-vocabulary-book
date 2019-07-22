from django.urls import path

from . import views 

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('initUserAbility/', views.initUserAbility, name='initUserAbility'),
    path('updateUserAbility/', views.updateUserAbility, name='updateUserAbility'),
    path('getFreqWords/', views.getFreqWords, name='getFreqWords'),
<<<<<<< HEAD
    path('getRecommands/', views.svdRecommandation, name='svdRecommandation')
]
=======
    path('recommendedWords/', views.recommendedWords, name='recommendedWords'),
]
>>>>>>> ca3f9bd4769c09f299fd98185fa0a1418def9aaa
