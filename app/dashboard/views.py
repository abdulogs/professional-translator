from django.shortcuts import render, HttpResponseRedirect
from app.decorators import logout_required, superuser_required, staff_required, logout, login_required
from app.helpers import *



@logout_required(logout_url='/dashboard/home/')
def Index(request):
    return render(request, "dashboard/pages/index.html")


@staff_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def Home(request):
    return render(request, "dashboard/pages/home.html")


@superuser_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def UserAdmins(request):
    return render(request, "dashboard/pages/user-admins.html")


@superuser_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def UserStaff(request):
    return render(request, "dashboard/pages/user-staff.html")


@staff_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def Blogs(request):
    return render(request, "dashboard/pages/blogs.html")


@staff_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def BlogCategories(request):
    return render(request, "dashboard/pages/blog-categories.html")


@staff_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def Queries(request):
    return render(request, "dashboard/pages/queries.html")


@staff_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def Faqs(request):
    return render(request, "dashboard/pages/faqs.html")


@staff_required(redirect_url="/dashboard/forbidden")
@login_required(login_url='/dashboard/')
def Profile(request):
    return render(request, "dashboard/pages/profile.html")


@logout_required(logout_url="/dashboard/")
def Login(request):
    return render(request, "dashboard/pages/logout/login.html")


@logout_required(logout_url="/dashboard/")
def ForgotPassword(request):
    return render(request, "dashboard/pages/password-forgot.html")


@logout_required(logout_url="/dashboard/")
def RecoverPassword(request, uid, token):
    data = {"token": token, "uid": uid}
    return render(request, "dashboard/pages/password-recover.html", data)


def Signout(request):
    logout(request)
    return HttpResponseRedirect('/dashboard/')


def forbidden(request):
    return render(request, "dashboard/pages/403.html")


def notfound(request):
    return render(request, "dashboard/pages/404.html")
