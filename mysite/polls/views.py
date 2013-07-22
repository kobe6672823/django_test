# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk = poll_id)
    except Poll.DoesNotExist:
        raise Http404
    context = {'poll': poll}
    return render(request, 'polls/detail.html', context)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    request.session["name"] = "abc"

    return HttpResponse("You're voting on poll %s." % poll_id)

@csrf_exempt
def test_req(request):
    if ("id" in request.session):
        request.session["id"] += 1
        return HttpResponse("has session id: %d" % request.session["id"])
    else:
        request.session["id"] = 1
        return HttpResponse("no session id, now session id is set as: %d" % request.session["id"])

@csrf_exempt
def test_json(request):
    #a method to test how to get and return data in json

    req = json.loads(request.raw_post_data)
    result = {'id': req['id'], 'name': "abc"}
    return HttpResponse(json.dumps(result), content_type="application/json")
