from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Board,Topic,Post
import json
from django.contrib.auth.models import User

def home(request):
	boards = Board.objects.all().values()
	return render(request, 'index.html', {'boards': boards})

def board_topics(request, pk):
	board = Board.objects.get(pk=pk)

	return render(request, 'index.html', {'board': board})	

def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'index.html', {'board': board})


 # REST full api parts
def get_blog(request):
	boards = Board.objects.all().values()
	boards_list=list(boards)
	return JsonResponse(boards_list,safe=False)


def get_add_new_topic(request):

	if request.method == 'POST':
		# subject = request.POST['subject']
		# message = request.POST['message']
		data=json.loads(request.body)
		topicId=data['id']
		subject=data['subject']
		message=data['message']
		board = get_object_or_404(Board, pk=topicId)

		user = User.objects.first()  # TODO: get the currently logged in user

		topic = Topic.objects.create(
			subject=subject,
			board=board,
			starter=user
		)

		post = Post.objects.create(
			message=message,
			topic=topic,
			created_by=user
		)

		return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

	return render(request, 'new_topic.html', {'board': board})
   