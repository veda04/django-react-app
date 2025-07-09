from django.contrib import admin

# Register your models here.
from .models import Todo

# create a class for admin-model integration
class TodoAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ('title', 'description', 'completed')    

# register the model with the admin site using register method of admin.site class
admin.site.register(Todo, TodoAdmin)