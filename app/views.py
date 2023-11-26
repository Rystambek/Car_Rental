from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Car
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

def cars_all(request:HttpRequest) -> JsonResponse:
    cars_all = Car.objects.all()

    results = []
    for car in cars_all:
        results.append({
            "id":car.pk,
            "name":car.name,
            "price":car.price,
            "color":car.color,
            "model":car.model,
            "years":car.years,
            "motors":car.motors
        })
    return JsonResponse({"result":results})

def add_car(request:HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        data = request.body.decode()
        data_json = json.loads(data)

        car = Car(
            name = data_json['name'],
            price = data_json['price'],
            color = data_json['color'],
            model = data_json['model'],
            years = data_json['years'],
            motors = data_json['motors']
        )
        car.save()
        return JsonResponse({'result':200})
    
def car_id(request:HttpRequest,id) -> JsonResponse:
    cars = Car.objects.all()

    for car in cars:
        if car.id == id:
            result = ({
                "id":car.pk,
                "name":car.name,
                "price":car.price,
                "color":car.color,
                "model":car.model,
                "years":car.years,
                "motors":car.motors
            })
    return JsonResponse({'result':result})

def car_del(request: HttpRequest,id) -> JsonResponse:
    cars = Car.objects.all()

    for car in cars:
        if car.id == id:
            car.delete()

            return JsonResponse({'result':200})

    return JsonResponse({'result':'not found'})

def car_upd(request:HttpRequest, id) -> JsonResponse:
    if request.method == 'POST':
        data = request.body.decode()
        data_json = json.loads(data)

        cars = Car.objects.all()
        for car in cars:
            if car.id == id:
                car.name = data_json.get('name',car.name)
                car.price = data_json.get('price',car.price)
                car.color = data_json.get('color',car.color)
                car.model = data_json.get('model',car.model)
                car.years = data_json.get('years',car.years)
                car.motors = data_json.get('motors',car.years)

                car.save()

                result = ({
                    "id":car.pk,
                    "name":car.name,
                    "price":car.price,
                    "color":car.color,
                    "model":car.model,
                    "years":car.years,
                    "motors":car.motors
                })
    
            
                return JsonResponse({'result':result})
        return JsonResponse({'result':'not found'})
        