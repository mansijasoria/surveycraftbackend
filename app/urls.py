
from django.urls import path
from .views import RegisterView, LoginView, GetUserView

urlpatterns = [
   path('accounts/register', RegisterView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/user', GetUserView.as_view(), name='get_user'),
    # path('survey/create-question',GetquestionrView.as_view(), name='')
]


