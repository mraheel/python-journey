from django.contrib import admin
from .models import Category, Event, Template, EventAttachment, Wishlist

admin.site.register(Category)
admin.site.register(Template)
admin.site.register(Wishlist)
admin.site.register(Event)
admin.site.register(EventAttachment)