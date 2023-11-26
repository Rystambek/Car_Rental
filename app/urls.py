from django.contrib import admin
from django.urls import path

from .views import (
            home,
            index,
            get_num,
            get_sum,
            get_user,
            cars_all,
            add_car,
            car_id,
            car_del,
            car_upd
        )

urlpatterns = [
    path('cars-all/',cars_all),
    path('add-car/',add_car),
    path('car-id/<int:id>',car_id),
    path('car-del/<int:id>',car_del),
    path('car-upd/<int:id>',car_upd),
    path('',index),
    path('home/',home),
    path('get-num/',get_num),
    path('get-sum/',get_sum),
    path('get-user/<str:username>',get_user)
]