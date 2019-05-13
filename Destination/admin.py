from django.contrib import admin
from .models import Destination, Type,Camp
# Register your models here.
class ChoiceInline(admin.StackedInline):
	model = Camp
	extra = 1

class TypeInline(admin.StackedInline):
	model = Type
	extra = 1

class MovieeAdmin(admin.ModelAdmin):
  fieldsets = [
		(None, {'fields': ['name', 'image']}),
		
	]
	 
  inlines = [ChoiceInline,TypeInline]
	# list_display_links =('name','Place','originalprice')
	# list_display = ('id','name','Place','originalprice')
	# list_filter = ['name','Place','originalprice']
	# search_fields = ['name','Place']
    #date_hierarchy = ['pub_date']


admin.site.register(Destination, MovieeAdmin)