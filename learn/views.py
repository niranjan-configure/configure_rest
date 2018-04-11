from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

	def home(request):

	    # boards = Board.objects.all()
	    # boards_names = list()

	    # for board in boards:
	    #     boards_names.append(board.name)

	    # response_html = '<br>'.join(boards_names)

	    # return HttpResponse(response_html)
	    boards = Board.objects.all()
        return render(request, 'home.html', {'boards': boards})