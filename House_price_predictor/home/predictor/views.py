from django.shortcuts import render
from .models import *
from django.views.generic.base import View


# Create your views here.
# views.py
# from .predictor import predict_house_price  # Import your prediction function


def house_price_prediction(request):
    predicted_price = None

    if request.method == 'POST':
        num_rooms = int(request.POST['num_rooms'])
        num_bathrooms = int(request.POST['num_bathrooms'])
        num_kitchens = int(request.POST['num_kitchens'])
        area = float(request.POST['area'])

        # Call your prediction function to get the predicted price
        # predicted_price = predict_house_price(num_rooms, num_bathrooms, num_kitchens, area)

    return render(request, 'index.html', {'predicted_price': predicted_price})


def IndexView(request):
    data = CarouselImages.objects.all()
    context = {"data": data}
    return render(request, 'predictor/index.html', context)


def BaseView(request):
    return render(request, 'predictor/base.html')
