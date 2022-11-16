from django.contrib import admin
from .models import Review, Client

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated', )

# classClientAdmin(admin.ModelAdmin):


admin.site.register(Review, ReviewAdmin)
admin.site.register(Client)