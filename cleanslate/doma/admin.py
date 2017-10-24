from django.contrib import admin
from .models import User
from .models import Home
from .models import Reviews
from .models import Forum
from .models import Topic
from .models import Post
from .models import Village


admin.site.register(User)
admin.site.register(Home)
admin.site.register(Reviews)
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Village)
