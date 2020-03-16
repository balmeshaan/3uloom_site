from django.contrib import admin

# Register your models here.
from newsletter.models import ContactFormInfo, TutorContactFormInfo,MessageContactFormInfo

admin.site.register(ContactFormInfo)
admin.site.register(TutorContactFormInfo)
admin.site.register(MessageContactFormInfo)