import json

from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Count, DataStored


@csrf_exempt
def count_number(request, count_id):
    if request.method == "GET":
        count_obj = Count.objects.get(id=count_id)
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
            count_obj.increment += 1

            count_obj.save()
            counter_val = Count.objects.get(id=int(count_id)).increment
            user = User.objects.get(id=int(count_id))
            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            storage = DataStored.objects.create(username=username, time=current_time,
                                                action_type="increment", count_id=count_obj.id)

            data_stored = str(storage)
            greater = [{"id": i.id, "value": i.increment} for i in Count.objects.filter(increment__gte=10)]
            lesser = str(Count.objects.filter(increment__lte=10))


        else:
            count_obj = Count.objects.create(increment=1)
            counter_val = count_obj.increment
            user = User.objects.get(id=int(count_id))

            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            greater = [{"id": i.id, "value": i.increment} for i in Count.objects.filter(increment__gte=10)]

            lesser = str(Count.objects.filter(increment__lte=10))
            storage = DataStored.objects.create(username=username, time=current_time,
                                                action_type="increment")
            data_stored = str(storage)
        return HttpResponse(
            content_type="application/json", content=json.dumps({"count": counter_val,
                                                                 "greater": greater}))

@csrf_exempt
def count_decrease(request, count_id):
    if request.method == "GET":
        count_obj = Count.objects.get(id=count_id)
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
            count_obj.increment -= 1

            count_obj.save()
            counter_val = Count.objects.get(id=int(count_id)).increment
            user = User.objects.get(id=int(count_id))
            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            storage = DataStored.objects.create(username=username, time=current_time,
                                                action_type="decrement", count_id=count_id)
        else:
            count_obj = Count.objects.create(increment=1)
            counter_val = count_obj.increment
            user = User.objects.get(id=int(count_id))

            username = user.username
            time = datetime.datetime.now().strftime('%H:%M:%S')
            current_time = str(time)
            storage = DataStored.objects.create(username=username, time=current_time,
                                                action_type="decrement")

        return HttpResponse(
            content_type="application/json", content=json.dumps({"count": counter_val})
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
    result = []
    for i in Count.objects.all():
        first_action = 'increment'
        action_val = []
        stored_action = DataStored.objects.filter(count_id=i.id)
        for j in stored_action:
            if not first_action and j.action_type:
                action_val.append(j.action_type)
            elif first_action == j.action_type and j.action_type:
                action_val.append(j.action_type)
            else:
                action_val = []
                break
        if action_val:
            if action_val[0]:
                result.append({"countid": i.id, "action_type": action_val[0]})
    return HttpResponse(content_type='application/json', content=json.dumps({"result": result}))

@csrf_exempt
def dec_sorting(request):
    result = []
    for i in Count.objects.all():
        first_action = 'decrement'
        action_val = []
        stored_action = DataStored.objects.filter(count_id=i.id)
        for j in stored_action:
            if not first_action and j.action_type:
                action_val.append(j.action_type)
            elif first_action == j.action_type and j.action_type:
                action_val.append(j.action_type)
            else:
                action_val = []
                break
        if action_val:
            if action_val[0]:
                result.append({"countid":i.id, "action_type": action_val[0]})
    return HttpResponse(content_type='application/json', content=json.dumps({"results": result}))


@csrf_exempt
def arrangement(request):
    if request.method == "POST":
        greater = [{"id": i.id, "value": i.increment} for i in Count.objects.filter(increment__gte=10)]
        for i in greater:
            data_greater = i
        lesser = [{"id": i.id, "value": i.increment} for i in Count.objects.filter(increment__lte=10)]
        for j in lesser:
            data_lesser = j
    return HttpResponse(content_type='application/json', content=json.dumps({"greater": data_greater,
                                                                             "lesser": data_lesser
                                                                             }))









