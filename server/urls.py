
from django.contrib import admin
from django.urls import path
from user.views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('uploaddp/',uploaddp,name='uploaddp'),
    path('',home,name='home')
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)