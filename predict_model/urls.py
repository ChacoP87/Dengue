from django.urls import path, include
from rest_framework import routers
from predict_model.views import predictionView

#router = routers.DefaultRouter()
#router.register(r'predictions', PredictionView, 'predictions')

urlpatterns = [
    #path('api/', include(router.urls)),
    path('api/', predictionView, name='PredictionView'),
]
