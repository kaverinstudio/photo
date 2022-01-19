import logging
from emails.email import SendingEmail
import os
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from datetime import datetime

from user.models import UserModel


from .models import MainCardModel, Photo, Orders, Portfolio, PortfolioPhoto, Services, ConfirmOrder
from .forms import PhotoForm
from .sorting import moveFiles


log = logging.getLogger(__name__)


def index(request):
    card = MainCardModel.objects.all()
    context = {
        'card': card
    }
    return render(request, 'main/index.html', context)


def servises(request):
    card = MainCardModel.objects.all()
    context = {
        'card': card
    }
    return render(request, 'main/servises.html', context)


def portfolio(request):
    photo_cat = Portfolio.objects.all()
    photos = PortfolioPhoto.objects.all()
    return render(request, 'main/portfolio.html', {'photo_cat': photo_cat, 'photos': photos})


class OrderView(View):
    def get(request):
        photo_list = Photo.get_user_photos(request)
        order_session_key = request.session.session_key
        order = Orders.get_order_photos(request)
        order.delete()
        temp_order = []

        for photo in photo_list:
            temp_order_photo = []
            order_format = photo.format
            order_papier = photo.papier
            order_session_key = photo.session_key
            order_user_id = photo.user
            temp_order_photo.append(order_format)
            temp_order_photo.append(order_papier)
            temp_order_photo.append(order_session_key)
            temp_order_photo.append(order_user_id)
            temp_order_count = photo.count
            if temp_order_photo not in temp_order:
                temp_order.append(temp_order_photo)
                order = Orders(order_format=order_format,
                               order_papier=order_papier, order_count=temp_order_count, order_session_key=order_session_key, user=order_user_id)
                order.save()
            else:
                temp = Photo.get_user_photos(request).filter(
                    format=temp_order_photo[0], papier=temp_order_photo[1], session_key=temp_order_photo[2], user=temp_order_photo[3])
                temp_count = 0
                for i in temp:
                    temp_count += i.count
                order = Orders.objects.filter(
                    order_format=temp_order_photo[0], order_papier=temp_order_photo[1], order_session_key=temp_order_photo[2], user=temp_order_photo[3])
                order.update(order_count=temp_count)


def delete_photo(request, id):
    temp_photo = Photo.get_user_photos(request).filter(id=id)

    if not temp_photo.exists():
        log.info('Can`t find your photo with this id')
        return HttpResponseNotFound('Can`t find your photo with this id')

    log.info('Photo "%s" was deleted to order', temp_photo[0])

    temp_photo.delete()
    OrderView.get(request)

    return HttpResponse('Photo deleted')


def edit_upload_form(request):
    temp_photo = Photo.get_user_photos(request).filter(id=request.POST['id'])
    if 'format' in request.POST:
        format_edit = request.POST['format']

        temp_photo.update(format=format_edit)
        OrderView.get(request)

        log.info('Photo "%s" was changed to order', temp_photo[0])
        return HttpResponse('Photo updated')

    if 'count' in request.POST:
        count_edit = request.POST['count']

        temp_photo.update(count=count_edit)
        OrderView.get(request)

        log.info('Photo "%s" was changed to order', temp_photo[0])
        return HttpResponse('Photo updated')

    if 'papier' in request.POST:
        papier_edit = request.POST['papier']

        temp_photo.update(papier=papier_edit)
        OrderView.get(request)

        log.info('Photo "%s" was changed to order', temp_photo[0])
        return HttpResponse('Photo updated')


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.get_user_photos(request).order_by('-uploaded_at')
        OrderView.get(request)
        return render(self.request, 'main/order.html', {
            'photos': photos_list,
            'service_data': Services.to_json(),
        })

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            if request.user.is_anonymous:
                photo.session_key = request.session.session_key
            else:
                photo.user = request.user
            photo.session_key = request.session.session_key
            photo.save()

            log.info('Photos added to order for user:" %s"', photo.user)

            OrderView.get(request)

            data = {
                'is_valid': True,
                'name': photo.file.name,
                'url': photo.file.url,
                'id': photo.id,
                'count': photo.count,
                'papier': photo.papier,
                'format': photo.FORMATS,
                'service_data': Services.to_json(),
            }
        else:
            data = {'is_valid': False, 'errors': form.errors.as_text()}
        return JsonResponse(data)


class OrderComplite(View):
    def get(self, request):
        order_list = Orders.get_order_photos(
            request).values('order_format', 'order_count', 'order_papier')
        cost_list = Services.objects.all().values('name', 'cost')
        # user_info = UserModel.get_user_info(
        #     request).values('first_name', 'phone', 'city')
        user_info = UserModel.objects.all().filter(id=request.user.id)

        price = 0
        for i in order_list:
            for x in cost_list:
                if x['name'] == i['order_format']:
                    costs = i['order_count'] * x['cost']
                    price += costs
        return render(self.request, 'main/complite.html', {
            'orders': order_list,
            'cost': cost_list,
            'price': price,
            'user_info': user_info,
        })


def confirm_order(request):
    added_order = None

    if request.method == 'POST':
        order = ConfirmOrder(
            name=request.POST['name'],
            phone=request.POST['phone'],
            delivery=request.POST['delivery'],
            address=request.POST.get('address'),
            comment=request.POST.get('comment'),
        )
        moveFiles(request)
        order.save()
        added_order = order
        date_time = datetime.now().strftime("%m-%d-%Y %H:%M")
        photos_list = Photo.get_user_photos(request)
        for photo in photos_list:
            photo_path = os.path.dirname(photo.file.path)
            client_path = photo.file.name
            client_name = ''.join(client_path.split('/')[1])
            order_file = photo_path + '\\' + client_name + '.txt'

        order_log = open(order_file, mode="a", encoding="utf-8")
        order = ConfirmOrder.objects.all()
        order.update(link=photo_path)
        order_data = ''
        order_data += "Время заказа - " + date_time + '\n'
        order_data += "Клиент - " + added_order.name + '\n'
        order_data += "Телефон - " + added_order.phone + '\n'
        order_data += "Способ доставки - " + added_order.delivery + '\n'
        order_data += "Адрес доставки - " + str(added_order.address) + '\n'
        order_data += "Комментарии - " + added_order.comment + '\n\n'

        order_list = Orders.get_order_photos(request)

        mail_data = []

        for order in order_list:
            order_data += order.order_format + " " + \
                order.order_papier + " " + \
                str(order.order_count) + " шт" '\n'

            mail_data.append(order)

        email = SendingEmail()
        if request.user.is_authenticated:
            user_email = request.user.email
            email.sending_email(type_id=2, email=user_email,
                                order=added_order, data=mail_data)
        email.sending_email(type_id=1, order=added_order, data=mail_data)

        order_log.write(order_data)
        order_log.close()
        photos_list.delete()

        log.info('Order was confirmed for user:" %s"', photo.user)

        order_list.delete()
    return render(request, 'main/added-order.html', {'order': added_order, 'successful_submit': True})
