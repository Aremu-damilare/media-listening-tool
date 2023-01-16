from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from .views import NewEmailConfirmation


urlpatterns = [
    # auths endpoints
    # path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('register/', RegisterView.as_view(), name='account_signup'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('user/', UserDetailsView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',  VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    path('resend-email/', NewEmailConfirmation.as_view(), name='resend_email_confirmation'),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  
    
    # others
    ############

]