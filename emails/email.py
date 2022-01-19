import logging
from emails.models import EmailSendingFact
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.forms.models import model_to_dict

from photo.settings import FROM_EMAIL, FROM_ADMIN

log = logging.getLogger(__name__)


class SendingEmail(object):
    from_email = "Фото №1 <%s>" % FROM_EMAIL
    reply_to_emails = [from_email]
    target_emails = []
    bcc_emails = []

    def sending_email(self, type_id, email=None, order=None, data=None):
        if not email:
            email = FROM_ADMIN

        target_emails = [email]
        vars = dict()

        if type_id == 1:
            subject = "Новый заказ"
            vars['order_fields'] = model_to_dict(order)
            vars['order'] = order
            vars['data'] = data
            message = get_template(
                'emails/order_notification_admin.html').render(vars)

        elif type_id == 2:
            subject = "Ваш заказ получен!"
            vars['data'] = data
            message = get_template(
                'emails/order_notification_customer.html').render(vars)
        msg = EmailMessage(
            subject, message, from_email=self.from_email, to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails)

        msg.content_subtype = 'html'
        msg.mixed_subtype = 'related'
        msg.send()

        kwargs = {
            'type_id': type_id,
            'email': email,

        }
        if order:
            kwargs['order'] = order
        EmailSendingFact.objects.create(**kwargs)

        log.info('Email was send successfully!')
