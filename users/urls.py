from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user/', views.GetUserView.as_view(), name='user'),
    path('update/', views.UpdateUserView.as_view(), name='update'),
    path('changePassword/', views.ChangePasswordView.as_view(), name='changePassword'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]