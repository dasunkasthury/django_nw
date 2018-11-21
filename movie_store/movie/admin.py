from django.contrib import admin

from.models import Movies
from.models import Director
from.models import Genres


admin.site.register(Director)
admin.site.register(Movies)
admin.site.register(Genres)





