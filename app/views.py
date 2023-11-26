from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Car
from django.core.exceptions import ObjectDoesNotExist
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


def to_dict(car: Car) -> dict:

    return{
            "id":car.pk,
            "name":car.name,
            "url":car.url,
            "description":car.description,
            "price":car.price,
            "color":car.color,
            "model":car.model,
            "years":car.years,
            "motors":car.motors,

            "creates_at":car.created_at,
            "updated_at":car.updated_at
        }


def car(request:HttpRequest,id = None) -> JsonResponse:

    if request.method == "GET":
        if id is not None:
            try:
                car = Car.objects.get(id = id)
                return JsonResponse(to_dict(car))
            except ObjectDoesNotExist:
                return JsonResponse({'result':'object does not exist!'})
            
        else:
            cars_all = Car.objects.all()
            result = [to_dict(car) for car in cars_all]
            return JsonResponse({'result':result})
        
    elif request.method == 'POST':
        data_json = request.body.decode()
        data = json.loads(data_json)

        if not data.get('name'):
            return JsonResponse({'status': 'name is required!'})
        elif not data.get('url'):
            return JsonResponse({'status': 'url is required!'})
        elif not data['url'].startswith('https://'):
            return JsonResponse({'status': 'url is invalid!'})
        elif not data.get('price'):
            return JsonResponse({'status': 'price is required!'})
        elif not data.get('color'):
            return JsonResponse({'status': 'color is required!'})
        elif not data.get('model'):
            return JsonResponse({'status': 'model is required!'})
        elif not data.get('years'):
            return JsonResponse({'status': 'years is required!'})
        elif not data.get('motors'):
            return JsonResponse({'status': 'motors is required!'})
        
        car = Car.objects.create(
            name = data['name'],
            url  = data['url'],
            description = data.get('description',''),
            price = data['price'],
            color = data['color'],
            model = data['model'],
            years = data['years'],
            motors = data['motors']
        )

        car.save()

        return JsonResponse(to_dict(car))
    
    elif request.method == 'PUT':
        try:
            car = Car.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('name'):
            car.name = data['name']
        if data.get('url'):
            car.url = data['url']
        if data.get('description'):
            car.description = data['description']
        if data.get('price'):
            car.price = data['price']
        if data.get('color'):
            car.color = data['color']
        if data.get('model'):
            car.model = data['model']
        if data.get('years'):
            car.years = data['years']
        if data.get('motors'):
            car.motors = data['motors']

        car.save()

        return JsonResponse(to_dict(car=car))
    
    elif request.method == 'DELETE':
        try:
            car = Car.objects.get(id = id)

        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        car.delete()

        return JsonResponse({'status':'ok'})
    return JsonResponse({'status': 'method not allowed!'})
        
