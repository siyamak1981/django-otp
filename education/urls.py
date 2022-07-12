
from django.contrib import admin
from django.urls import re_path, include
from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from django.conf.urls.i18n import i18n_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView




admin.autodiscover()

urlpatterns = i18n_patterns(
      re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
      re_path(r'^jet/dashboard', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET URLS
      re_path(r'^admin/', admin.site.urls),
      re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
      re_path(r'^api/', include('api.urls')),
      re_path(r'^api/v1/rest-auth/', include('dj_rest_auth.urls')),
      re_path(r'^api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
      re_path(r'^api/v1/rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$',  ConfirmEmailView.as_view(), name='account_confirm_email'),
      re_path(r'^api/v1/rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
      re_path(r'^api/v1/rest-auth/password/reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
      re_path(r'^api/schema/', SpectacularAPIView.as_view(), name='schema'),
      re_path(r'^api/swagger-ui/$', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
      re_path(r'^api/redoc/$', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
      re_path(r'^rosetta/', include('rosetta.urls')),
     
)





