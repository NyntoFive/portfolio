from django.db import models

# START
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
# END

class SkillIcon(models.Model):
    # START
    image = models.ImageField(default='',
                              blank=True,
                              upload_to='images')
    image_medium = ImageSpecField(source='image',
                                     processors=[ResizeToFill(250, 150)],
                                     format='JPEG',
                                     options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})
    # END
    title = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title