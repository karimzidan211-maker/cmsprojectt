from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _, get_language
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from allauth.socialaccount.models import SocialAccount
from .models import GoogleLoginPluginModel



@plugin_pool.register_plugin
class GoogleLoginCMSPlugin(CMSPluginBase):
    model = GoogleLoginPluginModel
    name = _("Google Login Button")
    render_template = "memo/google_login.html"
    cache = False
    

    def render(self, context, instance, placeholder):
        return context