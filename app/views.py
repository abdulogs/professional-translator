from django.shortcuts import render
from app.models import Blog, Faq
from app.helpers import *
import googletrans


def Index(request):
    languages = googletrans.LANGUAGES
    print(type(languages))
    return render(request, "website/pages/index.html", {"languages": languages})


def AboutUs(request):
    return render(request, "website/pages/about-us.html")


def ContactUs(request):
    return render(request, "website/pages/contact-us.html")


def TermsAndConditions(request):
    return render(request, "website/pages/terms-and-conditions.html")


def PrivacyPolicy(request):
    return render(request, "website/pages/privacy-policy.html")


def Faqs(request):
    faqs = Faq.objects.all()
    return render(request, "website/pages/faqs.html", {"faqs": faqs})


def Blogs(request, name=""):
    category = cleanseparator(name, "-")
    return render(request, "website/pages/blogs.html", {"category": category})


def BlogDetails(request, name):
    try:
        name = cleanseparator(name, "-")
        blog = Blog.objects.get(name=name)
        return render(request, "website/pages/blog-details.html", {"blog": blog})
    except:
        return render(request, "website/pages/404.html")


def Error404(request):
    return render(request, "website/pages/404.html")


def Error500(request):
    return render(request, "website/pages/500.html")


def handler404(request, *args, **argv):
    response = render(request, 'website/pages/404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, 'website/pages/500.html')
    response.status_code = 500
    return response
