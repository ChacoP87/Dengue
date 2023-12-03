
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('predictions/', include('predict_model.urls')),
    path('admin/', admin.site.urls),
]
