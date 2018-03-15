import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Count, Count


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

        else:
            count_obj = Count.objects.create(increment=1)
            counter_val = count_obj.increment
        return HttpResponse(
            content_type="application/json", content=json.dumps({"count": counter_val})
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





