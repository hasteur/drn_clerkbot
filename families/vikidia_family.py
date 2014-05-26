# -*- coding: utf-8  -*-

__version__ = '$Id: 799989bb7a697e5f75e30f40c9d6d5f36140ba53 $'

import family


class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'vikidia'

        self.langs = {
            'en': 'en.vikidia.org',
            'es': 'es.vikidia.org',
            'fr': 'fr.vikidia.org',
            'it': 'it.vikidia.org',
            'ru': 'ru.vikidia.org',
        }

        self.namespaces[1] = {
            'fr': [u'Discussion', u'Discuter'],
            'es': u'Conversación acerca de',
        }
        self.namespaces[3] = {
            'fr': [u'Discussion utilisateur', u'Discussion Utilisateur'],
            'es': [u'Mensajes de usuario', u'Usuario Discusión'],
        }
        self.namespaces[4] = {
            '_default': [u'Vikidia', self.namespaces[4]['_default']],
            'fr': [u'Vikidia', u'VD'],
        }
        self.namespaces[5] = {
            '_default': [u'Discussion Vikidia', self.namespaces[5]['_default']],
            'es': u'Conversación acerca de Vikidia',
            'it': u'Discussioni Vikidia',
            'ru': u'Обсуждение Vikidia',
        }
        self.namespaces[6] = {
            'fr': [u'Fichier', u'Image'],
            'es': [u'Archivo', u'Image', u'Imagen'],
        }
        self.namespaces[7] = {
            'fr': [u'Discussion fichier', u'Image talk', u'Discussion Fichier',
                   u'Discussion Image'],
            'es': [u'Conversación acerca de imagen', u'Image talk', u'Imagen Discusión'],
        }
        self.namespaces[11] = {
            'fr': [u'Discussion modèle', u'Discussion Modèle'],
            'es': u'Conversación acerca de plantilla'
        }
        self.namespaces[13] = {
            'fr': [u'Discussion aide', u'Discussion Aide'],
            'es': u'Conversación acerca de ayuda',
        }
        self.namespaces[15] = {
            'fr': [u'Discussion catégorie', u'Discussion Catégorie'],
            'es': u'Conversación acerca de categor�a'
        }
        self.namespaces[100] = {
            'fr': u'Projet',
            'es': u'Proyecto',
        }
        self.namespaces[101] = {
            'fr': u'Discussion Projet',
            'es': u'Conversación de proyecto',
        }
        self.namespaces[102] = {
            'es': u'Portal',
            'fr': u'Portail',
            'it': u'Portale',
        }
        self.namespaces[103] = {
            'es': u'Conversación acerca de portal',
            'fr': u'Discussion Portail',
            'it': u'Discussioni portale',
        }
        self.namespaces[104] = {
            'fr': u'Quiz',
            'es': u'Quiz',
        }
        self.namespaces[105] = {
            'fr': u'Discussion Quiz',
            'es': u'Conversación acerca de quiz',
        }

        # Wikimedia wikis all use "bodyContent" as the id of the <div>
        # element that contains the actual page content; change this for
        # wikis that use something else (e.g., mozilla family)
        self.content_id = "bodyContent"

    def scriptpath(self, code):
        """The prefix used to locate scripts on this wiki.

        This is the value displayed when you enter {{SCRIPTPATH}} on a
        wiki page (often displayed at [[Help:Variables]] if the wiki has
        copied the master help page correctly).

        The default value is the one used on Wikimedia Foundation wikis,
        but needs to be overridden in the family file for any wiki that
        uses a different value.

        """
        return '/w'

    # Which version of MediaWiki is used? REQUIRED
    def version(self, code):
        # Replace with the actual version being run on your wiki
        return '1.22.2'

    def code2encoding(self, code):
        """Return the encoding for a specific language wiki"""
        # Most wikis nowadays use UTF-8, but change this if yours uses
        # a different encoding
        return 'utf-8'
