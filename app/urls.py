from django.urls import path, include
from app.views import *

urlpatterns = [
    path('dashboard/', include('app.dashboard.urls')),
    path('', Index, name="Home"),
    path('about-us/', AboutUs, name="WAboutUs"),
    path('contact-us/', ContactUs, name="WContactUs"),
    path('terms-and-conditions/', TermsAndConditions, name="WTerms"),
    path('privacy-policy/', PrivacyPolicy, name="WPrivacy"),
    path('faqs/', Faqs, name="WFaq"),
    path('blogs/', Blogs, name="WBlogs"),
    path('blogs/category/<str:name>/', Blogs, name="WBlogs"),
    path('blog-details/<str:name>/', BlogDetails, name="WBlog"),
    path('404/', Error404, name="Error404"),
    path('500/', Error500, name="Error500"),
]
