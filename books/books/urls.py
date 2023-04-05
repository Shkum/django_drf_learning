from django.conf import settings
from django.contrib import admin
from django.template.defaulttags import url

from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from store.views import BookViewSet, auth, UserBooksRelationView

router = SimpleRouter()

router.register(r'book', BookViewSet)
router.register(r'book_relation', UserBooksRelationView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('', include('social_django.urls', namespace='social')),
    re_path('', include('social_django.urls', namespace='social')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', auth),
]

urlpatterns += router.urls

if settings.DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    import debug_toolbar
    urlpatterns = [
                    path('__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns

# http://127.0.0.1:8000/book/?format=json
