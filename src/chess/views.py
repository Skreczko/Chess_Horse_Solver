from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.views.generic.edit import FormMixin
from .models import Board
from .forms import BoardForm
from solving_chess import get_chess_solution

# Create your views here.

class BoardView(FormMixin, View):
	form_class = BoardForm

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def get(self, request, *args, **kwargs):
		return render(request, 'base5x5.html')															#range board

	def form_valid(self, form):
		x, y = form.cleaned_data.get('point').split(',')
		Board.objects.create(board_status=get_chess_solution(int(x), int(y), 5)).save()					#range board
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_success_url(self):
		return reverse('detail', kwargs={'pk': Board.objects.all().last().id})


class BoardResultDetailView(DetailView):
	model = Board
	template_name = 'base5x5.html'																		#range board

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		for x in range(5):																				#range board
			for y in range(5):																			#range board
				context['x{}y{}'.format(x,y)] = Board.objects.all().last().board_status[x][y]
		context['my_context'] = 'True'
		return context