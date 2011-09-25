import os, sys
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect, HttpResponse
from worklog.models import *
from worklog.forms import *

@login_required
def create(request):
    data = {}
    if request.method == 'POST':
        form = CreateWorklogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']

            #save here
            w = Worklog(
                title = title,
                desc = desc,
            )
            w.save()

            return HttpResponseRedirect('/worklog/')
    else:
        form = CreateWorklogForm()
    
    data = {"form": form}

    return render_to_response("worklog/create.html",
           data, context_instance=RequestContext(request))
