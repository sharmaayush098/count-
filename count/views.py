import json

from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from count.utils.utility import arithmetic_op, sorting_op
from .models import Count, DataStored


@csrf_exempt
def count_number(request, count_id):

    if request.method == "GET":
        try:
            count_obj = Count.objects.get(id=count_id)
        except:
            count_obj = Count.objects.create(id=count_id)
        records = DataStored.objects.filter(count_id=count_id)
        greater = Count.objects.filter(increment__gte=10)
        lesser = Count.objects.filter(increment__lte=10)
        return render(
            request,
            "increment_page.html",
            {"count_obj": count_obj, "records": records, "greater": greater,
             "lesser": lesser}
        )

    elif request.method == "POST":
        try:
            count_obj = Count.objects.get(id=int(count_id))

        except:
            count_obj = None
        if count_obj:
            count_obj = arithmetic_op(count_obj, "increment", request.user.username)

        else:
            count_obj = Count.objects.create(increment=1)
            counter_val = count_obj.increment
            user = User.objects.get(id=int(count_id))

            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            DataStored.objects.create(username=username, time=current_time,
                                      action_type="increment")
        return HttpResponse(
            content_type="application/json", content=json.dumps({"count": count_obj.increment,
                                                                 }))


@csrf_exempt
def count_decrease(request, count_id):
    if request.method == "GET":
        try:
            count_obj = Count.objects.get(id=count_id)
        except:
            count_obj = Count.objects.create(id=count_id)
        records = DataStored.objects.filter(count_id=count_id)
        return render(
            request,
            "increment_page.html",
            {"count_obj": count_obj, "records": records}
        )

    elif request.method == "POST":
        try:
            count_obj = Count.objects.get(id=int(count_id))

        except:
            count_obj = None
        if count_obj:
            count_obj = arithmetic_op(count_obj, "decrement", request.user.username)
        else:
            count_obj = Count.objects.create(increment=1)
            counter_val = count_obj.increment
            user = User.objects.get(id=int(count_id))

            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            DataStored.objects.create(username=username, time=current_time,
                                      action_type="decrement")

        return HttpResponse(
            content_type="application/json", content=json.dumps({"count": count_obj.increment})
        )


@csrf_exempt
def detail(request, user_id,):
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


@csrf_exempt
def inc_sorting(request):
    result = sorting_op("increment")
    return HttpResponse(content_type='application/json', content=json.dumps({"result": result}))


@csrf_exempt
def dec_sorting(request):
    result = sorting_op("decrement")
    return HttpResponse(content_type='application/json', content=json.dumps({"results": result}))


@csrf_exempt
def arrangement(request):
    if request.method == "POST":
        greater = [{"id": i.id, "value": i.increment} for i in Count.objects.filter(increment__gte=10)]

        lesser = [{"id": i.id, "value": i.increment} for i in Count.objects.filter(increment__lte=10)]

    return HttpResponse(content_type='application/json', content=json.dumps({"greater": greater,
                                                                             "lesser": lesser
                                                                             }))









