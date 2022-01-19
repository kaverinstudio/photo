from django.contrib import admin
from django.db import models
from django.template.loader import get_template
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from main.forms import PortfolioAdminForm
from shop.forms import ShopAdminForm

from shop.models import ShopCardModel, ShopCardPhotos
from .models import ConfirmOrder, MainCardModel, Portfolio, PortfolioPhoto, Services

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField


admin.site.register(Services)


class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    content = RichTextUploadingField(blank=True, null=True)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


class ConfirnOrderView(admin.ModelAdmin):
    list_display = ['name', 'phone', 'delivery',
                    'address', 'comment', 'show_firm_url', ]

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_firm_url.short_description = "Ссылка на заказ"


admin.site.register(ConfirmOrder, ConfirnOrderView)


class MainCardModelPreview(admin.ModelAdmin):
    fields = ['description', 'image', 'preview', 'post_link']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')


admin.site.register(MainCardModel, MainCardModelPreview)


class PortfolioView(admin.TabularInline):
    model = PortfolioPhoto

    readonly_fields = ("showphoto_thumbnail",)

    def showphoto_thumbnail(self, instance):
        tpl = get_template("shop/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})

    showphoto_thumbnail.short_description = _("Фотографии")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioAdminForm
    inlines = [PortfolioView]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


class ShowPhotoInline(admin.TabularInline):
    model = ShopCardPhotos

    readonly_fields = ("showphoto_thumbnail",)

    def showphoto_thumbnail(self, instance):
        tpl = get_template("shop/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})

    showphoto_thumbnail.short_description = _("Фотографии товара")


@admin.register(ShopCardModel)
class ShopAdmin(admin.ModelAdmin):
    form = ShopAdminForm
    inlines = [ShowPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)
