from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

import django_rq

from .models import Task
from .tasks import run_boogie

def index(request):
    return render(request, 'django_hice/index.html')

@require_http_methods(["GET"])
def run(request):

    # Get input data
    data = request.GET.get('input', None)
    inference = request.GET.get('inference', None)
    trace = request.GET.get('trace', None)

    # Check data
    if data == None or not inference in dict(Task.INFERENCE_CHOICES) or trace == None:
        json_response = {
          'status' : 'Error',
          'result': 'No valid input',
        }
        return JsonResponse(json_response)

    # Get default queue
    queue = django_rq.get_queue('hice')

    # Create task (only with data)
    task = Task.objects.create(
        data = data,
        inference = inference,
        trace = (trace == 'true') # Everything except 'true' is considered false
    )

    # Create and queue job
    job = queue.enqueue(run_boogie, args=[task])

    # Generate response
    json_response = {
        'task_id': task.task_id,
    }

    return JsonResponse(json_response)

@require_http_methods(["GET"])
def result(request):
    # Get job ID
    job_id = request.GET.get('task_id', None)

    # Query task in database
    tasks = Task.objects.filter(task_id=job_id)
    print(tasks)

    # Task has already started executing or is finished
    if len(tasks) == 1:
        json_response = {
          'status' : tasks[0].status,
          'result': tasks[0].result,
        }
        return JsonResponse(json_response)

    # Task does not exist or is queued
    else:
        json_response = {
          'status' : 'unknown',
          'result': None,
        }

        return JsonResponse(json_response)
