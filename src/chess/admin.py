from django.contrib import admin
from .models import Board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
	list_display = ['start_date', 'board_status']
	readonly_fields = ['start_date', 'board_status']
	class Meta:
		model = Board

admin.site.register(Board, BoardAdmin)