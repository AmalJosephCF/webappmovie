from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
app_name='favouritesapp'

urlpatterns = [


    path('add/<int:id>/',views.add_to_favourites,name='add_to_favourites'),
    path('myfavmovies/',views.my_favourite_movies,name='my_favourite_movies'),
    path('removefavmovies/<int:id>/',views.remove_favourites,name='remove_favourites'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)