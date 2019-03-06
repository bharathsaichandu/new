from django.contrib import admin
from .models import question,Images,Profile,shared_room,share_room_Images,private_room,private_room_Images,entire_house,entire_house_Images
# Register your models here.

class sharedroomModelAdmin(admin.ModelAdmin):
    #list_display = []
    pass

class questionModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ['updated',"timestamp"]
    search_fields = ["title","description"]

    class Meta:
        model=question

class imageModelAdmin(admin.ModelAdmin):
    list_display = ["image","questionn"]

    class Meta:
        model=Images

class shareroomModelAdmin(admin.ModelAdmin):
    list_display = ["City","updated","timestamp"]
    list_display_links = ["updated"]
    list_editable = ["City"]
    list_filter = ['updated',"timestamp"]
    search_fields = ["City","area"]

    class Meta:
        model=shared_room
admin.site.register(question,questionModelAdmin)
admin.site.register(Images,imageModelAdmin)
admin.site.register(Profile)
admin.site.register(shared_room,shareroomModelAdmin)
admin.site.register(share_room_Images)
admin.site.register(private_room)
admin.site.register(private_room_Images)
admin.site.register(entire_house_Images)
admin.site.register(entire_house)