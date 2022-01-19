from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _
from .models import Photo, Portfolio, PortfolioPhoto


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('file', 'format', 'count', 'papier',)


class PortfolioAdminForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = (
            "photo_title",
        )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("images"):
            validate_image_file_extension(upload)

    def save_photos(self, showphoto):
        """Process each uploaded image."""
        for upload in self.files.getlist("images"):
            photo = PortfolioPhoto(showphoto=showphoto, photo=upload)
            photo.save()
