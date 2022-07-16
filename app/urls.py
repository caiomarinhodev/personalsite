from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app.views.site import IndexView

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', IndexView.as_view(), name='index'),
]
