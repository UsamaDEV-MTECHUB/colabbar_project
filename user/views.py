from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import userData
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


# for registration of user

def register(request) :
    if request.method == 'POST' :
        csrf_token = request.POST['csrfmiddlewaretoken']
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        password = request.POST['password']
        hash_pass = pbkdf2_sha256.hash(password, rounds=12000, salt_size=32)
        userdata = userData(username=username, fullname=fullname, email=email, phoneno=phoneno, password=hash_pass,
                            verify_link=csrf_token)
        userdata.save();

        # send one email
        # send_mail(
        #   'this is the subject',
        #  'thisi s email ocntar ',
        # settings.EMAIL_HOST_USER,
        # [email],
        # fail_silently=False,
        # )

        html_content = render_to_string('user/email_template.html',
                                        {'title' : 'Colabbar Accout Verification', 'link' : csrf_token,
                                         'email_sentto' : email, 'passw' : password})
        text_content = strip_tags(html_content)

        emails = EmailMultiAlternatives(
            # subject
            'Colabbar Accout Verification',
            # content
            text_content,
            # from_email
            settings.EMAIL_HOST_USER,
            # rec list
            [email]
        )
        emails.attach_alternative(html_content, "text/html")
        emails.send()
        print('data inserted')
        return redirect('verify-user')
    else :
        return render(request, 'user/register.html')


# for checking usernmae exist

@csrf_exempt
def check_username_exist(request) :
    username = request.GET['username']

    user_name = userData.objects.filter(username=username)
    if user_name :
        return HttpResponse(True)
    else :
        return HttpResponse(False)


# for checking email already  exist
@csrf_exempt
def check_checkemail_exist(request) :
    email = request.GET['email']

    user_email = userData.objects.filter(email=email)
    if user_email :
        return HttpResponse(True)
    else :
        return HttpResponse(False)


# for move page after verifying user

def verify_user(request) :
    return render(request, 'user/verify_user.html')


# for make user veriifed after email link
def user_verified(request) :
    user_email = request.GET['email_sentto']
    link = request.GET['link']
    passw = request.GET['passw']
    check_if_email_already_verify = userData.objects.filter(email__exact=user_email, verify_status=True)

    if check_if_email_already_verify :
        return redirect('home')
    else :
        verifys_email = userData.objects.filter(email__exact=user_email, verify_link__exact=link)
        print_pass = userData.objects.get(email__exact=user_email)

        # hash_rpassword = hashlib.md5(print_pass.password.decode())
        # print(hash_rpassword)
        userData.objects.filter(email__exact=user_email).update(verify_status=True, login_first=False)
        if verifys_email :
            return render(request, 'user/user_verified.html')
        else :
            return redirect('home')


# -------------------  LOGIN WORK AREA  ---------------------
def login(request) :
    if request.method == 'POST' :
        email = request.POST['email']
        password_check = request.POST['password']
        u_email = userData.objects.filter(email__exact=email)
        if u_email :
            u_pass = userData.objects.all().first()
            if pbkdf2_sha256.verify(password_check, u_pass.password) :
                print('password same')
                request.session['is_logged'] = True
                return redirect('feed')
            else :
                print('error  pass')
        else :
            print('no email found')
        #return render(request, 'index.html')
    else :
        if request.session.has_key('is_logged') :
            return redirect('feed')
        else:
            return render(request, 'user/login.html')


def check_checkpassword_exist(request) :
    if request.method == 'GET' :
        email = request.GET['email']
        password_check = request.GET['password']
        u_email = userData.objects.filter(email__exact=email)
        if u_email :
            u_pass = userData.objects.all().first()
            if pbkdf2_sha256.verify(password_check, u_pass.password) :
                print('password same')
                return HttpResponse(True)
            else :
                print('password same no')
                return HttpResponse(False)
        else :
            return HttpResponse(False)


# ------------------- FORGET PASWORD ----------------

def forgetPass_link(request) :
    if request.method == 'POST' :
        csrf_token = request.POST['csrfmiddlewaretoken']
        email = request.POST['email_verify']
        userData.objects.filter(email__exact=email).update(verify_status=False, verify_link=csrf_token)

        # send email verify
        html_content = render_to_string('user/forgetpass_template.html',
                                        {'title' : 'Colabbar Account Password Reset', 'link' : csrf_token,
                                         'email_sentto' : email})
        text_content = strip_tags(html_content)

        emails = EmailMultiAlternatives(
            # subject
            'Colabbar Accout Verification',
            # content
            text_content,
            # from_email
            settings.EMAIL_HOST_USER,
            # rec list
            [email]
        )
        emails.attach_alternative(html_content, "text/html")
        emails.send()
        print('data inserted')
        return redirect('verify-forgetpassword')


# for move page after verifying user

def verify_forgetpassword(request) :
    return render(request, 'user/verify_forgetpassword.html')


# for make user veriifed after email link
def verified_forgetpassword(request) :
    user_email = request.GET['email_sentto']
    link = request.GET['link']
    check_if_email_already_verify = userData.objects.filter(email__exact=user_email, verify_status=True)

    if check_if_email_already_verify :
        return redirect('home')
    else :
        verify_link = userData.objects.filter(email__exact=user_email, verify_link__exact=link)
        if verify_link :
            userData.objects.filter(email__exact=user_email).update(verify_status=True)
        return render(request, 'user/type_newpass.html', {'email' : user_email})


# update passwrod
def password_updated(request) :
    fp_email = request.GET['fp_email']
    fp_password = request.GET['fp_password']

    check_if_email_already_verify = userData.objects.filter(email__exact=fp_email, verify_status=True)

    if check_if_email_already_verify :
        hash_pass = pbkdf2_sha256.hash(fp_password, rounds=12000, salt_size=32)
        userData.objects.filter(email__exact=fp_email).update(password=hash_pass)
        return HttpResponse(True)
    else :
        return HttpResponse(False)
