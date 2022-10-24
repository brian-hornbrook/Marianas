from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated', )

admin.site.register(Review, ReviewAdmin)