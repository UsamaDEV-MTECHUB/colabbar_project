from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import feeddata
# HTML EMAIL
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# convert strign to hash md5
from passlib.hash import pbkdf2_sha256
import bcrypt
# truncate
from django.utils.text import Truncator
#   Django sessions
from django.contrib.sessions.models import Session


# for move page after verifying user

def feed(request) :
    if request.session.has_key('is_logged'):
        print('welcome')
        return render(request, 'feed/index.html')
    else :
        return redirect('home')

def logout(request) :
    del request.session['is_logged']
    return redirect('home')
