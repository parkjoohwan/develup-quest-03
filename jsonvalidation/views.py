from django.shortcuts import *
from django.http import *
from django.views.generic import View
from django.conf import settings
import json

# Create your views here.
class jsonvalid(View):
    def post(self, request):
        input = request.POST.get('user_input')
        
        try:
            json.loads(input)
            res = 'success'
            message = 'json이 맞습니다.'
        except:
            res = 'fail'
            message = 'json이 아닙니다.'
            
        return JsonResponse(
            {
                'Result' : res,
                'Message' : message,
                'Input' : input
            }
            , json_dumps_params={'ensure_ascii': False, 'indent': 4})


    def get(self, request):
        return render(request, 'index.html', {})
    