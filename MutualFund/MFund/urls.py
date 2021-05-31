from django.urls import path
from . import views
urlpatterns = [
    path('',views.Overview,name='overview'),
    path('<int:a>/details/',views.details,name='details'),
    path('<int:b>/short-info/',views.short_info,name='short_info'),
    path('list-view-api',views.Listing_Details.as_view(),name='Listview'),
    # path('list-view-html',views.Overview,name='overview')
]
