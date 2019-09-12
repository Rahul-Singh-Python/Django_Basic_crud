from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.index,name='index'),
    path('register/', views.registerpage),
    path('save/', views.save),
    path('fetch/', views.fetch),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)