from django.urls import path
from . import views
urlpatterns=[
    # path('',views.Index,name='home'),
    path('',views.Overview,name='overview'),
    path('app-read',views.list_,name='read'),
    path('app-create',views.create,name='create'),
    path('app-update/<int:id>',views.update,name='update'),
    path('app-delete/<int:id>',views.delete,name='delete'),
]