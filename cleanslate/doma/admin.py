from django.contrib import admin
from .models import User
from .models import Home
from .models import Topic
from .models import Village


admin.site.register(User)
admin.site.register(Home)
admin.site.register(Topic)
admin.site.register(Village)
