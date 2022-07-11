from django.shortcuts import render
from flask import Flask,render_template,request
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image, ImageOps
import numpy as np
from .models import MyModel
# from .serializers import MyModelSerializer
# from rest_framework import permissions
# from rest_framework.parsers import MultiPartParser, FormParser
# # import cropper
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# app=Flask(__name__)
img_height,img_width=224,224
dic ={'Benign Masses': 0, 'Malignant Masses': 1}

model=load_model("model/breast_cancer_with_mamogram_dataset/breastcancerMammogramModel.h5")

model1=load_model("model/breast_cancer_with_miscroscople_dataset/keras_model.h5")

model2 = load_model('model/keras_model.h5')
model3=load_model('model/cervical_cancer/cervicalkeras_model.h5')
# Create your views here.
def MammogramBreastCancerUploader(request):
    return render(request,"index.html")



# model.make_predict_function()
model1.make_predict_function()
def predict_label(img_test):
    img=image.load_img(img_test,target_size=(224,224))
    i=image.img_to_array(img)/255
    i=np.expand_dims(i,axis=0)
    p=model.predict(i)[0][0]

    
    if p>=0.6 and p<=0.8:
        return ("show the presence of Malignant Masses(Breast Cancer cells)" )
    if p<0.5:
        return ("show the presence of Benign Masses(no cancer cells)")
    else:
        return("no the required image")
    





def MammogramBreastCancerPrediction(request):
    if request.method == 'POST':
        images=request.FILES['my_image']
        imagestorage=FileSystemStorage()
        filePathName=imagestorage.save(images.name,images)
        print(images.name)
        filePathName=imagestorage.url(filePathName)
       
        img_test='.'+filePathName
        print(img_test)

        p=predict_label(img_test)
      
    context={"filePathName":filePathName,'p':p}
    print(filePathName)
    return render(request,'index.html',context)




def MicroscopeBreastCancerPredictionUpload(request):
    return render(request,"microscopeBreastCancer.html")
    
def MicroscopeBreastCancerPrediction(request):
    if request.method == 'POST':
        images=request.FILES['my_image']
        imagestorage=FileSystemStorage()
        filePathName=imagestorage.save(images.name,images)
        print(images.name)
        filePathName=imagestorage.url(filePathName)
       
        img_test='.'+filePathName
        p=prediction(img_test)

    context={"filePathName":filePathName,'p':p}
    print(filePathName)
    return render(request,'microscopeBreastCancer.html',context)  

def prediction(img_test):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(img_test)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
    image_array = np.asarray(image)
# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
    data[0] = normalized_image_array

# run the inference
    prediction = model2.predict(data)
    print(prediction)
    
    for i in prediction:
            
        if i[0]>0.07:
            # if i[0]>i[1]:
            #     if i[0]>i[2]:
            #         if i[0]>i[3]:
            percentage=i[0]*100
            res = "{:.2f}".format(percentage)
            label='Benign Cells'
            return label,res,'%'
        if i[1]>0.7:
        #     print(i[0]>0.7>i[2]>i[3]>i[1])
        # if i[0]< i[1]:
        #         if i[1]>i[2]:
        #             if i[2]>i[3]:
            percentage=i[1]*100
            res = "{:.2f}".format(percentage)
            label='Insitu Cells'
            return label,res,'%'
                # return("InSuti")   

        if i[2]>0.7:
            # if i[2]> i[1]:
            #     if i[2]>i[0]:
            #         if i[2]>i[3]:
            percentage=i[2]*100
            res = "{:.2f}".format(percentage)
            label='Invasive Cells'
            return label,res,'%'
            #  return("Invasive")      


        if i[3]> 0.7:
            # if i[3]>i[2]:
            #     if i[3]>i[1]:
            #         if i[3]>i[0]:
            percentage=i[3]*100
            res = "{:.2f}".format(percentage)
            label='normal Cells'
            return label,res,'%'
    # context={"label":label,"percentage":percentage}
    # return render(request,"index.html",context)


def cervicalBreastCancerPredictionUpload(request):
    return render(request,"cervicalCancer.html")
    
def cervicalBreastCancerPrediction(request):
    if request.method == 'POST':
        images=request.FILES['my_image']
        imagestorage=FileSystemStorage()
        filePathName=imagestorage.save(images.name,images)
        print(images.name)
        filePathName=imagestorage.url(filePathName)
       
        img_test='.'+filePathName
        p=Cervicalprediction(img_test)

    context={"filePathName":filePathName,'p':p}
    print(filePathName)
    return render(request,'cervicalCancer.html',context)  

def Cervicalprediction(img_test):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(img_test)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
    image_array = np.asarray(image)
# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
    data[0] = normalized_image_array

# run the inference
    prediction = model3.predict(data)
    print(prediction)
    
    for i in prediction:
            
        if i[0]>0.07:
            percentage=i[0]*100
            res = "{:.2f}".format(percentage)
            label='TYPE1'
            return label,res,'%'
        if i[1]>0.7:
            percentage=i[1]*100
            res = "{:.2f}".format(percentage)
            label="TYPE2"
            return label,res,"%"
                  

        if i[2]>0.7:
            percentage=i[2]*100
            res = "{:.2f}".format(percentage)
            label='TYPE3'
            return label,res,'%'
          