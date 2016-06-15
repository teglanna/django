import json
from config.settings.base import DJANGO_ROOT
from django.shortcuts import render
# from .models import Message


def home(request):
	# messages = Message.objects.order_by('order')
	filepath = DJANGO_ROOT + '/content.JSON'

	with open(filepath) as data_file:
		content_data = json.load(data_file)
	messages = content_data['mess']


	context_dict = {
		'messages': messages
	}
	return render(request, 'starter_app/home.html', context_dict)
