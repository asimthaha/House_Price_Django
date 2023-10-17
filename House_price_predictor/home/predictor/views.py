from django.shortcuts import render
import numpy as np
from .models import *
from django.views.generic.base import View

# Create your views here.
# views.py
# from .predictor import predict_house_price  # Import your prediction function

def IndexView(request):
    data = CarouselImages.objects.all()
    context = {"data": data}
    return render(request, 'predictor/index.html', context)


import joblib
from django.shortcuts import render
from django.http import HttpResponse

def predict_price(request):
    model = joblib.load("C:\\Users\\hp\\PycharmProjects\\House_price_predictor\\home\\predictor\\model.pkl")  # Load your saved model
    predicted_price = None

    if request.method == 'POST':
        try:
            # Get user input from the form and convert to integers
            overall_qual = int(request.POST.get('overall_qual'))
            grliv_area = int(request.POST.get('grliv_area'))
            garage_cars = int(request.POST.get('garage_cars'))
            total_bsmt_sf = int(request.POST.get('total_bsmt_sf'))
            first_flr_sf = int(request.POST.get('first_flr_sf'))
            full_bath = int(request.POST.get('full_bath'))
            tot_rms_abv_grd = int(request.POST.get('tot_rms_abv_grd'))
            year_built = int(request.POST.get('year_built'))

            # Predict the price
            user_input = [overall_qual, grliv_area, garage_cars, total_bsmt_sf, first_flr_sf, full_bath, tot_rms_abv_grd, year_built]
            predicted_price = model.predict([user_input])[0]
        except (ValueError, TypeError):
            # Handle invalid input gracefully, e.g., by setting predicted_price to None
            predicted_price = None

    return render(request, 'predictor/predict.html', {'predicted_price': predicted_price})

def BaseView(request):
    return render(request, 'predictor/base.html')

def PredictView(request):
    return render(request, 'predictor/predict.html')