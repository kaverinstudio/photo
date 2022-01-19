from emails.models import EmailSendingFact, EmailType
from django.contrib import admin

admin.site.register(EmailType)


class EmailSendingFactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmailSendingFact._meta.fields]
    list_filter = ['email', 'type']
    search_fields = ['email', 'type']

    class Meta:
        model = EmailSendingFact


admin.site.register(EmailSendingFact, EmailSendingFactAdmin)
