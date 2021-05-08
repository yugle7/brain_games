"""braingames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from braingames import settings
from discuss.views import *
from main.views import *
from person.views import *
from poll.views import *
from chat.views import *
from puzzle.views import *
from solution.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', include('person.urls')),
    path('puzzle/', include('puzzle.urls')),
    path('solution/', include('solution.urls')),
    path('discuss/', include('discuss.urls')),
    path('poll/', include('poll.urls')),
    path('chat/', include('chat.urls')),
    path('', include('main.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = urlpatterns + [
        path('__debug__/', include(debug_toolbar.urls))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
