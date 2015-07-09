from django.contrib import admin
from forum.models import *

# Register your models here.

class YourModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, YourModelAdmin)
admin.site.register(UserProfile, YourModelAdmin)
admin.site.register(Category, YourModelAdmin)
admin.site.register(Topic, YourModelAdmin)
admin.site.register(Comment, YourModelAdmin)
admin.site.register(Type, YourModelAdmin)