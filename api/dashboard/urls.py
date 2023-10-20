from django.urls import path, include
from api.dashboard.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register("blog", BlogApi, basename="DashboardBlogApi")
router.register("blog-category", BlogCategoryApi,
                basename="DashboardBlogCategoryApi")
router.register("user", UserApi, basename="DahsboardUserApi")
router.register("faq", FaqApi, basename="DashboardFaqApi")
router.register("query", QueryApi, basename="DashboardQueryApi")
router.register("subscriber", SubscriberApi, basename="DashboardSubscriberApi")
router.register("newsletter", NewsletterApi, basename="DashboardNewsletterApi")

urlpatterns = [
    path('', include(router.urls), name="DahsboardApi"),
    path('login/', LoginApi.as_view(), name='DahsboardLoginApi'),
    path('register/', RegistrationApi.as_view(), name='DahsboardRegisterApi'),
    path('change-password/', ChangePasswordApi.as_view(),
         name='DahsboardChangePasswordApi'),
    path('send-reset-password-email/', PasswordResetEmailApi.as_view(),
         name='DahsboardsendResetEmailApi'),
    path('reset-password/<uid>/<token>/',
         PasswordResetApi.as_view(), name='DahsboardResetPasswordApi'),
]
