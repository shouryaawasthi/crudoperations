from django.contrib import admin
from .models import students
@admin.register(students)
class studentadmin(admin.ModelAdmin):
    list_display=["id","name","email"]

# Register your models here.
