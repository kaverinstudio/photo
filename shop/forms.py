from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _


from .models import ShopCardModel, ShopCardPhotos


class ShopAdminForm(forms.ModelForm):
    class Meta:
        model = ShopCardModel
        fields = (
            "name",
            "description",
            "category",
            "price",
        )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("shop_images"):
            validate_image_file_extension(upload)

    def save_photos(self, show):
        """Process each uploaded image."""
        for upload in self.files.getlist("shop_images"):
            photo = ShopCardPhotos(show=show, photo=upload)
            photo.save()
