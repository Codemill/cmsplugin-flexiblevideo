from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import FlexibleVideoPlugin
from django.utils.translation import ugettext as _

class CMSFilexibleVideoPlugin(CMSPluginBase):
    model = FlexibleVideoPlugin
    name = _("Flexible Video")
    render_template = "flexiblevideo/video.html"

    def render(self, context, instance, placeholder):
        video_type, video_id = instance.video_id()
        context.update({
            'video_type': video_type,
            'video_id': video_id,
            'cover': instance.cover,
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CMSFilexibleVideoPlugin)
