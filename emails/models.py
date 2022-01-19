from django.db import models
from django.db.models.deletion import CASCADE


class EmailType(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Тип имейла"
        verbose_name_plural = "Тип имейлов"


class EmailSendingFact(models.Model):
    type = models.ForeignKey(EmailType, on_delete=CASCADE)
    order = models.ForeignKey('main.ConfirmOrder', null=True,
                              blank=True, default=None, on_delete=CASCADE)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return self.type.name

    class Meta:
        verbose_name = 'Отправленный имейл'
        verbose_name_plural = 'Отправленные имейлы'
