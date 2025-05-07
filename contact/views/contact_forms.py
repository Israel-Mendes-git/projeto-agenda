from typing import Any, Dict
 
from django import forms
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
 
from contact.forms import ContactForm
from contact.models import Contact

def create(request):
     if request.method == 'POST':
         context = {
             'form': ContactForm(request.POST)
         }
 

         return render(
             request,
             'contact/create.html',
             context
         )
 
     context = {
         'form': ContactForm()
     }
 
     return render(
         request,
         'contact/create.html',
     )