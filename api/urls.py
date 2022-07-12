from django.urls import re_path,include
from rest_framework import routers
from api.v1.views.otp import   SendSmsView, VarifyOtpCodeView
from api.v1.views.session import  SessionViewSet
from api.v1.views.profile import ProfileListViewSet, ProfileUpdateViewSet
from api.v1.views.city import CityViewSet
from api.v1.views.province import ProvinceViewSet
from api.v1.views.login import LoginApiView
from api.v1.views.signup import SignUpApiViewSet



app_name = "api"

router = routers.DefaultRouter()
router.register(r'v1/city', CityViewSet)
router.register(r'v1/province', ProvinceViewSet)
router.register(r'v1/session', SessionViewSet)
router.register(r'v1/users/signup', SignUpApiViewSet)
router.register(r'v1/users/updateuserinformation', ProfileUpdateViewSet)




urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r"^v1/users/sendsms", SendSmsView.as_view(), name = 'sendsms_view'),
    re_path(r"^v1/users/varifycode", VarifyOtpCodeView.as_view(), name = 'varify_code_view'),
    re_path(r"^v1/users/login", LoginApiView.as_view(), name = 'login_view'),
    re_path(r"^v1/users/self", ProfileListViewSet.as_view(), name = 'list_profile'),
   
    

] 
