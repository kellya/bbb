from django.contrib import admin

from temp.models import Temp

# Register your models here.

class TempAdmin(admin.ModelAdmin):
	pass

admin.site.register(Temp, TempAdmin)
