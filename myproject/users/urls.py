from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('somewhat/', TestAuthView.as_view(), name='some'),

]




#path('register/', RegisterView.as_view(), name='register'),