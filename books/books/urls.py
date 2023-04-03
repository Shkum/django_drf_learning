from django.contrib import admin
from django.template.defaulttags import url

from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from store.views import BookViewSet, auth

router = SimpleRouter()

router.register(r'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('', include('social_django.urls', namespace='social')),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth)
]

urlpatterns += router.urls

# http://127.0.0.1:8000/book/?format=json
