# from session.models import  newstats
import os
import platform
import socket
from django.db.models import F
from http.server import BaseHTTPRequestHandler
from urllib import parse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

class DemoMeddleware(BaseHTTPRequestHandler):
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_request = 0
        self.context_response = {
            "msg": {"warning":"there is no more in the pintres"}
        }
    
    # def stats(self, os_info):

    #     if "windows" in os_info:
    #         newstats.objects.all().update(win =F("win") + 1)

    #     elif "mac" in os_info:
    #         newstats.objects.all().update(mac =F("mac") + 1)

    #     elif "iPhone" in os_info:
    #         newstats.objects.all().update(iph =F("iph") + 1)

    #     elif "Android" in os_info:
    #         newstats.objects.all().update(android =F("android") + 1)

    #     else:
    #         newstats.objects.all().update(oth =F("oth") + 1)
            


  
    def __call__(self, request):
        # print(f"hello man siyamakam:{type(self.stats)}")
        # self.num_request += 1
        # print(f"Request handled :{self.num_request}")
        # print(request.path)
        # print(request.headers['Host'])
        # print(request.headers['Accept_Language'])
        print(request.COOKIES['csrftoken'])
        # if "admin" not in request.path:
        # self.stats(request.META['HTTP_HOST'])
        # print(socket.gethostname())
        # print(socket.gethostbyaddr(socket.gethostname())[0])

        
        # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(',')[0]
        # else:
        #     ip = request.META.get('REMOTE_ADDR')

        # print(ip)


        response = self.get_response(request)
        return response
    
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print(f'view name : {view_func.__dict__}')
    # def process_template_response(self, request, response):
    #     response.context_data["new_data"] = self.context_response
    #     return response

    # def authenticate(self, request):
	# 	token = request.META.get('Authorization')
	# 	if not token:
	# 		return None  # request will be passed to the next class
	# 	token = token.split(' ')[-1]
	# 	try:
	# 		token = Token.objects.get(key=token)
	# 	except Token.DoesNotExist:
	# 		raise AuthenticationFailed('invalid token') #  401 will be returned

	# 	return token.user, None