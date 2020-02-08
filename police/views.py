from django.shortcuts import render
from guardian.models import *
from core import recognize_faces_image
import os
from core import encode_faces
import boto3
import smtplib

# Create your views here.
def get_analysis(request):
	return render(request, 'analyze.html')