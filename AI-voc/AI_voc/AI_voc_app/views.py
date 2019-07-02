from django.shortcuts import render

from django.contrib.auth.models import User, Group 
from rest_framework import viewsets 
from AI_voc_app.serializers import UserSerializer, GroupSerializer 

from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy 
from django.views import generic 

class SignUp(generic.CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer 

class GroupViewSet (viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer 
