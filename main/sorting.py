import shutil
import os


from . models import Photo


def moveFiles(request):

    list = Photo.get_user_photos(request)

    for photo in list:

        moveFrom = os.path.dirname(photo.file.path)

        moveTo = moveFrom + "\\\\" + photo.format + \
            "\\\\" + photo.papier + "\\\\" + str(photo.count) + " шт"

        print(moveTo)

        needToMove = os.listdir(moveFrom)

        if not needToMove:
            return

        if os.path.exists(moveTo) != True:
            os.makedirs(moveTo)

        if os.path.isdir(photo.file.name) == False:
            photo_name = photo.file.name
            name_photo = ''.join(photo_name.split('/')[-1])

            shutil.copyfile(moveFrom + "\\" + name_photo,
                            moveTo + "\\\\" + name_photo)
            os.remove(moveFrom + "\\" + name_photo)
