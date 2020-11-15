from django.contrib import admin
from psave.models import Host, Data

# Register your models here.

admin.site.register([Host, Data])
