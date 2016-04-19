from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
import json

def test_ajax(request):
    if request.method == 'POST':
        post_test = request.POST.get('test')
        response_data = {}

        response_data['message'] = 'Some error message'
        response_data['result'] = 'Success!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponseForbidden()

def index(request):
    return render(request, 'index/index.html', {})
