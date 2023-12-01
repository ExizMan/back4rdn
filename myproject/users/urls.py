from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView,TokenRefreshSlidingView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('somewhat/', TestAuthView.as_view(), name='some'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('token/refresh/2', TokenRefreshSlidingView.as_view(), name='token_refresh2'),
]




#path('register/', RegisterView.as_view(), name='register'),