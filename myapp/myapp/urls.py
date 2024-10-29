from django.contrib import admin
from django.urls import path
from app.views import post_list, post_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list),
    path('view/', post_list_view),
]
