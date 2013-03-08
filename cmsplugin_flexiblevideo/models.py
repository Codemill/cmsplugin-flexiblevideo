from django.db import models
from cms.models import CMSPlugin
from urlparse import parse_qs, urlparse

class FlexibleVideoPlugin(CMSPlugin):
    video_link = models.URLField()
    cover = models.ImageField(upload_to='video_covers')
    
    def video_id(self):
        video_type = ''
        if 'youtube' in self.video_link:
            video_type = 'youtube'

            url = urlparse(self.video_link)
            params = parse_qs(url.query)
            video_id = params['v'][0]
           
        elif 'vimeo' in self.video_link:
            video_type = 'vimeo'

            url = urlparse(self.video_link)
            video_id = url.path

        else:
            return None, None

        return video_type, video_id
