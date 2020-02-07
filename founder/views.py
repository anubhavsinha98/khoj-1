from django.shortcuts import render
from guardian.models import *
from core import recognize_faces_image
import os
from core import encode_faces

# Create your views here.
def get_upload_found_person_image_form(request):
	return render(request, 'upload_found_person_image_form.html')


def upload_found_person_image_form(request):
	images = request.FILES.getlist('images')
	addhar_card_number = request.POST['addhar_card_number']
	try:
		os.mkdir("media/images/founder/" + str(addhar_card_number))
	except FileExistsError:
		pass

	files=[]
	file_num=0
	for image in images:
		extension=str(image).split(".")[-1]
		file_not_created=True
		while file_not_created:
			try:
				file_name = str(file_num)+"."+extension
				file_loc = "media/images/founder/"+str(addhar_card_number)+"/"+file_name
				with open(file_loc, 'wb+') as destination:
					destination.write(image.read())
				file_not_created=False
				files.append(file_name)
				file_num+=1
			except FileExistsError:
				file_num+=1
	# print(files)
	args= {'image' : "media/images/founder/" + str(addhar_card_number) + "/" +file_name}
	addhar_num,img_path=recognize_faces_image.recognize_person(args)
	# import pdb;pdb.set_trace()
	if addhar_num!="Unknown":
		person_name=MissingPerson.objects.get(addhar_card_number=addhar_num).name
		status="Found"
	else:
		person_name="Unknown"
		status="Not Found!"
	return render(request, 'base.html',{'name': person_name,'status' : status,'img_path' : img_path})