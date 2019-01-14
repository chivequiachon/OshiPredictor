from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import IdolInformation

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

        ### FIRST PASS
        ################
        anime_manga_fan_score = int(ml_json_req['q1'])
        if anime_manga_fan_score > 40:
            result_q1 = IdolInformation.objects.filter(anime_manga_fan_score__gt=40)
        else:
            result_q1 = IdolInformation.objects.filter(anime_manga_fan_score__lt=50)

        eat_score = int(ml_json_req['q2'])
        if eat_score > 40:
            result_q2 = IdolInformation.objects.filter(eat_score__gt=40)
        else:
            result_q2 = IdolInformation.objects.filter(eat_score__lt=50)

        artistic_score = int(ml_json_req['q3'])
        if artistic_score > 40:
            result_q3 = IdolInformation.objects.filter(artistic_score__gt=40)
        else:
            result_q3 = IdolInformation.objects.filter(artistic_score__lt=50)

        music_fan_score = int(ml_json_req['q4'])
        if music_fan_score > 40:
            result_q4 = IdolInformation.objects.filter(music_fan_score__gt=40)
        else:
            result_q4 = IdolInformation.objects.filter(music_fan_score__lt=50)

        travel_score = int(ml_json_req['q5'])
        if travel_score > 40:
            result_q5 = IdolInformation.objects.filter(travel_score__gt=40)
        else:
            result_q5 = IdolInformation.objects.filter(travel_score__lt=50)

        athletic_score = int(ml_json_req['q6'])
        if athletic_score > 40:
            result_q6 = IdolInformation.objects.filter(athletic_score__gt=40)
        else:
            result_q6 = IdolInformation.objects.filter(athletic_score__lt=50)

        animal_like_score = int(ml_json_req['q7'])
        if animal_like_score > 40:
            result_q7 = IdolInformation.objects.filter(animal_like_score__gt=40)
        else:
            result_q7 = IdolInformation.objects.filter(animal_like_score__lt=50)

        caring_score = int(ml_json_req['q8'])
        if caring_score > 40:
            result_q8 = IdolInformation.objects.filter(caring_score__gt=40)
        else:
            result_q8 = IdolInformation.objects.filter(caring_score__lt=50)

        read_score = int(ml_json_req['q9'])
        if read_score > 40:
            result_q9 = IdolInformation.objects.filter(read_score__gt=40)
        else:
            result_q9 = IdolInformation.objects.filter(read_score__lt=50)

        cook_score = int(ml_json_req['q10'])
        if cook_score > 40:
            result_q10 = IdolInformation.objects.filter(cook_score__gt=40)
        else:
            result_q10 = IdolInformation.objects.filter(cook_score__lt=50)

        result = ((((((((result_q1 | result_q2) | result_q3) | result_q4) | result_q5) | result_q6) | result_q7) | result_q8) | result_q9) | result_q10

        ## SECOND PASS
        ###############

        least_sum_of_distance = -1
        corresponding_idol_info = None
        for idol_info in result:
            summation = 0
            summation += abs(anime_manga_fan_score - idol_info.anime_manga_fan_score)
            summation += abs(eat_score - idol_info.eat_score)
            summation += abs(artistic_score - idol_info.artistic_score)
            summation += abs(music_fan_score - idol_info.music_fan_score)
            summation += abs(travel_score - idol_info.travel_score)
            summation += abs(athletic_score - idol_info.athletic_score)
            summation += abs(animal_like_score - idol_info.animal_like_score)
            summation += abs(caring_score - idol_info.caring_score)
            summation += abs(read_score - idol_info.read_score)
            summation += abs(cook_score - idol_info.cook_score)

            if least_sum_of_distance < 0 or summation < least_sum_of_distance:
                least_sum_of_distance = summation
                corresponding_idol_info = idol_info

        # Set cookie to the actual image saved in the db
        request.session['corresponding_idol'] = {
            "idol_romaji_name": corresponding_idol_info.romaji_name,
            "idol_kanji_name": corresponding_idol_info.kanji_name,
            "generation": corresponding_idol_info.generation + " Generation",
            "img_url": corresponding_idol_info.image_url
        }

        return HttpResponse(status=200)
    return HttpResponse(status=403)

def get_result(request):
    if request.is_ajax() and request.method == 'GET':
        idol_info = request.session['corresponding_idol']
        del request.session['corresponding_idol']
        #return HttpResponse("http://stage48.net/wiki/images/7/74/HoriKaerimichi.jpg", status=200)
        return JsonResponse(idol_info, status=200)
    return HttpResponse(status=403)

def test_redis(request):
    from django_redis import get_redis_connection
    get_redis_connection("default").flushall()
    return HttpResponse(status=200)