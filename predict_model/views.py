from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PredictionSerializer
from .models import Prediction

from sklearn.linear_model import Perceptron, LogisticRegression
import numpy as np
import joblib

# Create your views here.
@api_view(['GET'])
def predictionView(request):
    
    if request.method == 'GET':
        
        data = request.data
        enviroment = data.get('enviroment')
        
        model = joblib.load('model.joblib')
        
        predict = model.predict([enviroment])
        
        response_data = {
            'clasification': predict[0],
        }
        return Response(data=response_data, status=status.HTTP_200_OK)
        
        
        
        
