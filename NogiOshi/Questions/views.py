from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

def show_questions(request):
    if request.method == 'GET':
        color_question_pair = [
            ("#43501e", "Are you a fan of anime/manga?"),
            ("#640064", "Do you like to eat?"),
            ("#f9c75e", "Do you like to draw/design?"),
            ("#661419", "Do you like to listen to music (in general)?"),
            ("#36a230", "Do you like to travel?"),
            ("#5665b5", "Are you athletic?"),
            ("#48b47e", "Do you like animals?"),
            ("#c47b75", "Do you like to care for others?"),
            ("#938fbb", "Do you like to read?"),
            ("#0e524d", "Do you like to cook?"),
        ]

        return render(request, 'questions.html', {'color_question_pair': color_question_pair})
    return HttpResponse(status=403)

def analyze(request):
    if request.is_ajax() and request.method == "POST":
        ml_json_req = json.loads(request.body)
        print(request.body)

        return HttpResponse(status=200)
    return HttpResponse(status=403)

def get_result(request):
    if request.is_ajax() and request.method == 'GET':
        return HttpResponse("http://stage48.net/wiki/images/7/74/HoriKaerimichi.jpg", status=200)
    return HttpResponse(status=403)

def show_result(request):
    return render(request, 'results.html')

def test_redis(request):
    from django_redis import get_redis_connection
    get_redis_connection("default").flushall()
    return HttpResponse(status=200)