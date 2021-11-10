from django.contrib import admin
from .models import TT
from .models import Guard
from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Guard)
admin.site.register(TT)
