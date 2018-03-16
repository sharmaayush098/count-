import json

from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Count, DataStored


@csrf_exempt
def count_number(request, count_id=None):
    if request.method == "GET":
        count_obj = Count.objects.latest("id")
        return render(
            request,
            "increment_page.html",
            {"count_obj": count_obj}
        )

    elif request.method == "POST":
        try:
            count_obj = Count.objects.get(id=int(count_id))
        except:
            count_obj = None
        if count_obj:
            count_obj.increment += 1
            count_obj.save()
            counter_val = Count.objects.get(id=int(count_id)).increment
            user = User.objects.get(id=int(count_id))
            position = user
            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            storage = DataStored.objects.create(username=username, time=current_time, count_id=position,
                                                action_type="increment")


        else:
            count_obj = Count.objects.create(increment=1)
            counter_val = count_obj.increment
            user = User.objects.get(id=int(count_id))
            position = user
            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            storage = DataStored.objects.create(username=username, time=current_time, count_id=position,
                                                action_type="increment")
            storage.save()
        return HttpResponse(
            content_type="application/json", content=json.dumps({"count": counter_val, "time": current_time,
                                                                 "count_id": position,
                                                                 "user": username, "action": "increment"})
        )


@csrf_exempt
def count_decrease(request, count_id=None):
    if request.method == "GET":
        count_obj = Count.objects.latest("id")
        return render(request, "increment_page.html", {"count_obj": count_obj})
    elif request.method == "POST":
        try:
            count_obj = Count.objects.get(id=int(count_id))

        except:
            count_obj = None
        if count_obj:
            count_obj.increment -= 1
            count_obj.save()
            count_value = Count.objects.get(id=int(count_id)).increment
        else:
            count_obj = Count.objects.create(increment=-1)
            count_value = count_obj.increment
        return HttpResponse(
            content_type='application/json', content=json.dumps({"count": count_value})
        )


@csrf_exempt
def detail(request, user_id=None,):
    if request.method == "GET":
        user = User.objects.get(id=int(user_id))

        return render(request, "increment_page.html", {"user": user})
    elif request.method == "POST":
        user = User.objects.get(id=int(user_id))
        username = user.username

        time = datetime.datetime.now().strftime('%H:%M:%S')
        current_time = str(time)

        return HttpResponse(content_type='application/json', content=json.dumps({"user": username,
                                                                                 "time": current_time}))









