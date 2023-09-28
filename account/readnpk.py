from typing import Any
import random as readNpk
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
import json
from django.views.generic import ListView , DetailView ,View,TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView





def read_npk_values(min_value, max_value):
    return readNpk.randint(min_value, max_value)


