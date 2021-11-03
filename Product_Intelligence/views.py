import os
import random, hashlib
from django.shortcuts import render, redirect
from django.contrib import messages
from django import template
from . import models
from django.db import connections, transaction
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

def admin_dashboard(request) :
    return render(request, 'AdminDashboard.html')

def homepage(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'HomePage.html')

def loginpage(request) :
    if request.method == 'POST' :
        email = request.POST['email']
        password_received = request.POST['user_password']
        cursor = connections['default'].cursor()
        cursor.execute("SELECT saltvalue, password FROM Product_Intelligence_user_details_db WHERE (email = '{}')".format(email))
        saltvalue_sql = cursor.fetchall()
        saltvalue = saltvalue_sql[0][0]
        password_db = saltvalue_sql[0][1]
        enc_password = encryption(saltvalue, password_received)
        if password_db == enc_password :
            cursor.execute("SELECT firstname, lastname FROM Product_Intelligence_user_details_db WHERE email = '{}'".format(email))
            username_tuple = cursor.fetchall()
            username = username_tuple[0][0] + ' ' + username_tuple[0][1]
            request.session['username'] = username
            request.session['email'] = email
            if 'next' in request.POST :
                return redirect(request.POST.get('next'))
        else :
            return render(request, 'LoginPage.html')
    return render(request, 'LoginPage.html')

def logout(request) :
    if request.session['username'] :
        del request.session['username']
        del request.session['email']
    elif request.POST.get('redirect_url') :
        return redirect(request.POST.get('redirect_url'))
    else :
        return redirect('homepage')

def signuppage(request) :
    if request.method == 'POST' :
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        mobilenumber = request.POST['mobilenumber']
        plain_password = request.POST['user_password']
        plain_confirmpassword = request.POST['confirm_password']
        saltvalue = os.urandom(random.randint(1, 100))
        password = encryption(saltvalue, plain_password)
        signup = models.user_details_db(firstname= firstname, lastname = lastname, email = email, mobilenumber = mobilenumber, password = password, saltvalue= saltvalue)
        signup.save()
        return redirect(signupsuccess)
    else:
        return render(request, 'SignUpPage.html')

def encryption(saltvalue, password) :
    keyvalue = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'),
        saltvalue,
        100000
    )
    return keyvalue

def signupsuccess(request) :
    signup_success_template = loader.get_template('SignUpSuccess.html')
    return HttpResponse(signup_success_template.render())

def user_accounts(request) :
    cursor = connections['default'].cursor()
    cursor.execute("SELECT firstname, lastname, email, mobilenumber from Product_Intelligence_user_details_db WHERE email = '{}'".format(request.session['email']))
    user_details = cursor.fetchall()[0]
    context = {'firstname' : user_details[0], 'lastname' : user_details[1], 'email' : user_details[2], 'mobilenumber' : user_details[3]}
    return render(request, 'UserAccounts.html', context)

def edit_user_accounts(request) :
    cursor = connections['default'].cursor()
    cursor.execute("SELECT firstname, lastname, email, mobilenumber from Product_Intelligence_user_details_db WHERE email = '{}'".format(request.session['email']))
    user_details = cursor.fetchall()[0]
    user_email = request.session['email']
    if request.method == 'POST' :
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        mobilenumber = request.POST['mobilenumber']
        cursor = connections['default'].cursor()
        cursor.execute("UPDATE Product_Intelligence_user_details_db SET firstname = '{}', lastname = '{}', email = '{}', mobilenumber = '{}' WHERE email = '{}'".format(firstname, lastname, email, mobilenumber, user_email))
        cursor.execute("SELECT firstname, lastname, email from Product_Intelligence_user_details_db WHERE email = '{}'".format(email))
        sql_value = cursor.fetchall()[0]
        request.session['username'] = sql_value[0] + ' ' + sql_value[1]
        request.session['email'] = sql_value[2]
        return redirect(request.POST.get('redirect_url'))
    context = {'firstname' : user_details[0], 'lastname' : user_details[1], 'email' : user_details[2], 'mobilenumber' : user_details[3]}
    return render(request, 'EditUserAccounts.html', context)

def edit_user_password(request) :
    if request.method == 'POST' :
        plain_password = request.POST['user_password']
        plain_confirmpassword = request.POST['confirm_password']
        if plain_password == plain_confirmpassword :
            saltvalue = os.urandom(random.randint(1, 100))
            password = encryption(saltvalue, plain_password)
            confirmpassword = password
            sql_update = models.user_details_db.objects.get(email = request.session['email'])
            sql_update.saltvalue = saltvalue
            sql_update.password = password
            sql_update.save()
            return redirect(request.POST.get('redirect_url'))
    return render(request, 'UpdateUserPassword.html')

def customization_page(request) :
    return render(request, 'CustomizerPage.html')

def clothing(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'Clothing.html')

def electronics(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'Electronics.html')

def business_promotions(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'BusinessPromotions.html')

def menstshirts(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, "Men'sT-Shirts.html")

def womenstshirts(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, "Women'sT-Shirts.html")

def officewearstore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'OfficeWears.html')

def laptopsstore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'LaptopsConfigurations.html')

def tabletsstore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'TabletsConfigurations.html')

def flyerstore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'Flyers.html')

def brochurestore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'Brochures.html')

def letterheadstore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'LetterHeads.html')

def visitingcardstore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'VisitingCards.html')

def postalcoverstore(request) :
    if request.POST.get('signout') :
        logout(request)
    return render(request, 'PostalCovers.html')