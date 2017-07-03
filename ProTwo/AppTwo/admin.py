from django.contrib import admin
from AppTwo.models import Topic
from AppTwo.models import Webpage
from AppTwo.models import AccessRecord
from AppTwo.models import User
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
