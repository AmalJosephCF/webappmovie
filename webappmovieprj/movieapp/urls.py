from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
app_name='movieapp'

urlpatterns = [

    path('',views.allMovieCat,name='allMovieCat'),
    path('add/',views.addMovie,name='add'),
    path('mymovies/',views.myMovies,name='mymovies'),
    path('<slug:c_slug>/',views.allMovieCat,name='movies_by_category'),
    path('<slug:c_slug>/<slug:p_slug>',views.movDetail,name='movDetail'),
    path('updateMovie/<int:id>/',views.updateMovie,name='updateMovie'),
    path('delete/<int:id>/',views.deleteMovie,name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)