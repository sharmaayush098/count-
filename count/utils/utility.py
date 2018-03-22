import datetime

from count.models import Count, DataStored


def arithmetic_op(count_obj, op_type, username):
    if op_type == "increment":
        count_obj.increment += 1
    elif op_type == "decrement":
        count_obj.increment -= 1
    else:
        return None
    count_obj.save()
    time = datetime.datetime.now().strftime('%H:%M:%S')
    current_time = str(time)
    DataStored.objects.create(username=username, time=current_time,
                              action_type=op_type, count_id=count_obj.id)
    return Count.objects.get(id=count_obj.id)


def sorting_op(first_action):
    result = []
    for i in Count.objects.all():
        action_val = []
        stored_action = DataStored.objects.filter(count_id=i.id)
        if first_action == "increment":
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
        elif first_action == "decrement":
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
    return result
