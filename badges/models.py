from django.db import models
from django.utils.translation import ugettext_lazy as _

class Badge(models.Model):
    title = models.CharField(_(u'Title'), max_length=255)

    def __unicode__(self):
        return self.title

class UserBadge(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_(u'User'), related_name='badges')
    badge = models.ForeignKey(Badge, verbose_name=_(u'Badge'))
    year = models.PositiveSmallIntegerField(_(u'Year'), null=True, blank=True)
    description = models.TextField(_(u'Description'))
