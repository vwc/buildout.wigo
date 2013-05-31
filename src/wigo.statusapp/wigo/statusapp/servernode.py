from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model

from plone.app.textfield import RichText


from wigo.statusapp import MessageFactory as _


class IServerNode(model.Schema, IImageScaleTraversable):
    """
    Server details
    """


class ServerNode(Container):
    grok.implements(IServerNode)


class View(grok.View):
    """ sample view class """

    grok.context(IServerNode)
    grok.require('zope2.View')
    grok.name('view')

    def hosted_sites(self):
        return dict()
