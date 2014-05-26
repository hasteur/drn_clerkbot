# -*- coding: utf-8 -*-

__version__ = '$Id: dfd9b637d39e3d080dc18f1156d9b4f62c234f72 $'

# The new wikivoyage family that is hosted at wikimedia

import family


class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'wikivoyage'
        self.languages_by_size = [
            'en', 'de', 'pt', 'fr', 'it', 'nl', 'pl', 'ru', 'es', 'vi', 'sv',
            'he', 'zh', 'ro', 'uk', 'el',
        ]

        self.langs = dict([(lang, '%s.wikivoyage.org' % lang)
                           for lang in self.languages_by_size])

        # Override defaults
        self.namespaces[2]['de'] = [u'Benutzer', u'BN', u'Benutzerin']
        self.namespaces[3]['de'] = [u'Benutzer Diskussion', u'BD', u'Benutzerin Diskussion']
        self.namespaces[12]['de'] = [u'Hilfe', u'H']
        self.namespaces[13]['de'] = [u'Hilfe Diskussion', u'HD']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur', u'Discussion utilisatrice']
        self.namespaces[2]['pl'] = [u'Użytkownik', u'Użytkowniczka']
        self.namespaces[3]['pl'] = [u'Dyskusja użytkownika', u'Dyskusja użytkowniczki']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[9]['ro'] = [u'Discuție MediaWiki', u'Discuţie MediaWiki']
        self.namespaces[12]['uk'] = [u'Довідка', u'Д']
        self.namespaces[14]['uk'] = [u'Категорія', u'К']
        self.namespaces[10]['zh'] = [u'Template', u'样板', u'模板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'使用說明', u'帮助', u'幫助']
        self.namespaces[14]['zh'] = [u'Category', u'分类', u'分類']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            'de': u'Wikivoyage',
            'el': u'Βικιταξίδια',
            'en': u'Wikivoyage',
            'es': u'Wikiviajes',
            'fr': u'Wikivoyage',
            'he': u'ויקימסע',
            'it': u'Wikivoyage',
            'nl': u'Wikivoyage',
            'pl': u'Wikipodróże',
            'pt': u'Wikivoyage',
            'ro': u'Wikivoyage',
            'ru': u'Wikivoyage',
            'sv': u'Wikivoyage',
            'uk': u'Вікімандри',
            'vi': u'Wikivoyage',
            'zh': u'Wikivoyage',
        }

        self.namespaces[5] = {
            'de': u'Wikivoyage Diskussion',
            'el': u'Συζήτηση Βικιταξίδια',
            'en': u'Wikivoyage talk',
            'es': u'Wikiviajes discusión',
            'fr': u'Discussion Wikivoyage',
            'he': u'שיחת ויקימסע',
            'it': u'Discussioni Wikivoyage',
            'nl': u'Overleg Wikivoyage',
            'pl': u'Dyskusja Wikipodróży',
            'pt': u'Wikivoyage Discussão',
            'ro': u'Discuție Wikivoyage',
            'ru': u'Обсуждение Wikivoyage',
            'sv': u'Wikivoyagediskussion',
            'uk': u'Обговорення Вікімандри',
            'vi': u'Thảo luận Wikivoyage',
            'zh': u'Wikivoyage talk',
        }

        self.namespaces[100] = {
            'de': u'Portal',
            'it': u'Portale',
            'uk': u'Портал',
        }

        self.namespaces[101] = {
            'de': u'Portal Diskussion',
            'it': u'Discussioni portale',
            'uk': u'Обговорення порталу',
        }

        self.namespaces[102] = {
            'de': u'Wahl',
        }

        self.namespaces[103] = {
            'de': u'Wahl Diskussion',
        }

        self.namespaces[104] = {
            'de': u'Thema',
            'it': u'Tematica',
        }

        self.namespaces[105] = {
            'de': u'Thema Diskussion',
            'it': u'Discussioni tematica',
        }

        self.namespaces[106] = {
            'de': u'Nachrichten',
        }

        self.namespaces[107] = {
            'de': u'Nachrichten Diskussion',
        }

        self.namespaces[108] = {
            'he': u'ספר',
        }

        self.namespaces[109] = {
            'he': u'שיחת ספר',
        }

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = ['es', 'ru', ]

    def shared_data_repository(self, code, transcluded=False):
        return ('wikidata', 'wikidata')
