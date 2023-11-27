from django.http import HttpRequest, HttpResponse, JsonResponse
import json

def index(request:HttpRequest) -> JsonResponse:
    return JsonResponse({'username':200})

def home(request:HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Hello</h1>')


def get_sum(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        params = request.GET

        a = params.get('a', 0)
        b = params.get('b', 0)

        return JsonResponse({'sum': int(a) + int(b)})

    elif request.method == 'POST':
        data = request.body.decode()
        data_json = json.loads(data)

        a = data_json.get('a', 0)
        b = data_json.get('b', 0)

        result = {'sum': int(a) + int(b)}
        return JsonResponse(result)

    return JsonResponse({'error': 'Invalid HTTP method'})

def get_num(request:HttpRequest) -> JsonResponse:
    params = request.GET
    number = params.get('number')
    return JsonResponse({"Number":number})

def get_user(request:HttpRequest, username:str) -> JsonResponse:
    return JsonResponse({'username':username})


