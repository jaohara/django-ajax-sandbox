from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Record



# IMPORTANT FOR AJAX

from django.http import JsonResponse
from django.core import serializers

import json

# /IMPORTANT FOR AJAX


from .models import Record

from random import randrange

def homepage(request):
    return render(request, 'as/base.html', {})

def buttonpage(request):
    return render(request, 'as/buttonpage.html', {})

def formpage(request):
    return render(request, 'as/formpage.html', {})

def recordpage(request):
    return render(request, 'as/recordpage.html', {})

# AJAX database views

def create_record(request):
    record_string = None
    record_int = None

    if 'record_string' in request.POST:
        record_string = request.POST.get("record_string")

    if 'record_int' in request.POST:
        record_int = int(request.POST.get("record_int"))

    message = "Error when creating record."
    result_type = "failure"
    record_pk = None

    if 'record_string' is not None and 'record_int' is not None:
        record = Record.objects.create(my_string=record_string, my_int=record_int)
        record_pk = record.id
        message = "Record created successfully"
        result_type = "success"

    data = {
        'result_type': result_type,
        'result_message': message,
        'record_string': record_string,
        'record_int': record_int,
        'record_pk': record_pk,
    }

    return JsonResponse(data)

def delete_record(request, pk):

    try:
        record = Record.objects.get(pk=pk)
        record.delete()
        result_type = "success"
        result_message = "Record successfully deleted."
    except Record.DoesNotExist:
        result_type = "failure"
        result_message = "The selected record doesn't exist."

    data = {
        'result_type': result_type,
        'result_message': result_message,
    }

    return JsonResponse(data)

def list_records(request):
    record_values = list(Record.objects.all().values_list())

    return JsonResponse({'records': record_values})

def list_single_record(request, pk):
    record = Record.objects.get(pk=pk)

    """
        Alright, so what's going on here? what seems to be happening is that we're returning
        a JSON string representation of the record in response.record.

        When we hit the javascript portion of the page, we're going to use jQuery's $.parseJSON()
        method to parse this into a JSON object.

        The object is going to come out looking like this:

            {
                "model": "ajax_sandbox.record", 
                "pk": 9, 
                "fields": {
                    "my_string": "record 2", 
                    "my_int": 23456, 
                    "created": "2017-03-03T19:22:54.681Z"
                }
            }

        From there, we can access the record's fields like this:

        jsonVarName.fields.my_string    // "record 2"
    """

    return JsonResponse({'record': serializers.serialize("json", [record])[1:-1]})

def list_latest_record(request):
    record = Record.objects.latest("created")

    return JsonResponse({'record': record})

# AJAX return views
def random_word(request):
    words = ["Hello", "Banana", "Orange", "Racecar", "Bird", "Baseball", "Rock", "Anteater",]

    data = {
        'word': words[randrange(len(words))],
    }

    return JsonResponse(data)



def random_int(request, max_range=1024):

    error = None

    if "max_range" in request.GET:
        try:
            max_range = int(request.GET['max_range'])
        except ValueError:
            error = "Please enter an integer."

    data = {
        'int': randrange(max_range),
        'max_range': max_range,
        'error': error,
    }

    return JsonResponse(data)

