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
        ailments = data.get('ailments')
        
        model = joblib.load('model.joblib')
        
        '''
        model = Perceptron()
        model.t_= 490153.0
        model.coef_= np.array([2, 4, 1, -10, 11, 5, 3])
        model.coef_.T = np.array([2, 4, 1, -10, 11, 5, 3])
        model.intercept_ = np.array([-4])
        '''
        
        predict = model.predict([ailments])
        
        response_data = {
            'prediction': predict[0],
        }
        return Response(data=response_data, status=status.HTTP_200_OK)
        
        
        
        
