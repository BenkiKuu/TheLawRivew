from django.contrib import admin
from .models import Profile, Affidavit, DemandLetter, LawFirms

# Register your models here.
admin.site.register(Profile)
admin.site.register(Affidavit)
admin.site.register(DemandLetter)
admin.site.register(LawFirms)
