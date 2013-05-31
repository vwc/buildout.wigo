import json
import urllib2
from five import grok

from z3c.form import group, field
from zope import schema

from plone.dexterity.content import Container
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model

from plone.app.textfield import RichText


from wigo.statusapp import MessageFactory as _


class IServerNode(model.Schema, IImageScaleTraversable):
    """
    Server details
    """
    server = schema.TextLine(
        title=-(u"Server Name"),
        required=True
    )


class ServerNode(Container):
    grok.implements(IServerNode)


class View(grok.View):
    """ sample view class """

    grok.context(IServerNode)
    grok.require('zope2.View')
    grok.name('view')

    def update(self):
        self.has_info = len(self.hosted_sites()) > 0

    def hosted_sites(self):
        sn = getattr(self.context, 'server')
        url = 'http://%s.vorwaerts-werbung.de/serverdetails.json' % sn
        response = urllib2.urlopen(url)
        data = json.loads(response.read())
        return data
