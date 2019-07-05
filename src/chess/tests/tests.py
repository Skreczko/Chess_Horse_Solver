from django.test import TestCase
import datetime
from django.urls import reverse
from chess.forms import BoardForm
from chess.models import Board

# Create your tests here.

class FormTestCase(TestCase):
	def test_form(self):
		data = {
			'point': '2,2'
		}
		form = BoardForm(data=data)
		self.assertTrue(form.is_valid())
		self.assertEqual(form.cleaned_data.get('point'), '2,2')

class ModelTestCase(TestCase):
	board = [
		[3,32,5,12,23,26],
		[6,11,2,25,34,13],
		[31,4,33,22,27,24],
		[10,7,18,1,14,35],
		[19,30,9,16,21,28],
		[8,17,20,29,36,15]
	]
	def setUp(self):
		Board.objects.create(board_status=self.board).save()

	def test_board_time(self):
		obj = Board.objects.all().first()
		self.assertEqual(obj.start_date, datetime.date.today())

	def test_board_list(self):
		obj = Board.objects.all().first()
		self.assertEqual(obj.board_status, self.board)


class ViewTestCase(TestCase):
	board = [
		[3,32,5,12,23,26],
		[6,11,2,25,34,13],
		[31,4,33,22,27,24],
		[10,7,18,1,14,35],
		[19,30,9,16,21,28],
		[8,17,20,29,36,15]
	]
	def setUp(self):
		Board.objects.create(board_status=self.board).save()

	def test_board_view_get(self):
		url = reverse('board')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_board_view_post(self):
		data = {
			'point': "0,0"
		}
		url = reverse('board')
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 302)

	def test_board_view_post_follow(self):
		data = {
			'point': "2,2"
		}
		url = reverse('board')
		response = self.client.post(url, data=data, follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['x2y2'], 1)
		self.assertEqual(Board.objects.all().count(), 2)



