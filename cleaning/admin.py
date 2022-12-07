from django.contrib import admin
from .models import Review, Client

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ( )

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ()

# classClientAdmin(admin.ModelAdmin):


admin.site.register(Review, ReviewAdmin)
admin.site.register(Client, ClientAdmin)