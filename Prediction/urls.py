from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('home/',views. MammogramBreastCancerUploader,name="MammogramBreastCancerPrediction"),
    path('submit/',views.MammogramBreastCancerPrediction,name="MammogramBreastCancerPrediction"),
    path('breastcancerpredictionPage/',views.MicroscopeBreastCancerPredictionUpload,name="MicroscopeBreastCancerPrediction"),
    path('breastcancerprediction/',views.MicroscopeBreastCancerPrediction,name="MicroscopeBreastCancerPrediction"),
    path('cervicalcancerpredictionPage/',views.cervicalBreastCancerPredictionUpload,name="cervicalBreastCancerPrediction"),
    path('cervicalcancerprediction/',views.cervicalBreastCancerPrediction,name="cervicalBreastCancerPrediction")

] 