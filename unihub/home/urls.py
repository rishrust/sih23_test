from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register', views.register, name='register'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('index/upload',views.upload,name='upload'),
    path('index/aboutus',views.aboutus, name='aboutus'),
    path('index/view',views.view, name='aboutus'),
    path('proj/<int:item_id>', views.project_details, name='proj'),
    
]




# for media 
from django.conf import settings

from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)