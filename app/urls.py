from django.contrib import admin
from django.urls import path

from app.views.car import CarView
from app.views.customer import CustomerView
from app.views.sum import (
            home,
            index,
            get_num,
            get_sum,
            get_user,
        )

urlpatterns = [
    path('car/<int:id>',CarView.as_view()),
    path('car/',CarView.as_view()),
    path('customer/',CustomerView.as_view()),
    path('customer/<int:id>',CustomerView.as_view()),
    path('',home),
    path('index/',index),
    path('get-num/',get_num),
    path('get-sum/',get_sum),
    path('get-user/<str:username>',get_user)
]