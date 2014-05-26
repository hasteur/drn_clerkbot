# -*- coding: utf-8  -*-

__version__ = '$Id: 64f70d5029ad70c54d0e0276ae79626df395b544 $'

import family

# The wikidata family


class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'wikidata'
        self.langs = {
            'wikidata': 'www.wikidata.org',
            'test': 'test.wikidata.org',
        }

        # Override defaults
        self.namespaces[0]['test'] = [u'', u'Item']
        self.namespaces[1]['test'] = [u'Talk', u'Item talk']
        self.namespaces[0]['wikidata'] = [u'', u'Item']
        self.namespaces[1]['wikidata'] = [u'Talk', u'Item talk']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': [u'Wikidata', u'WD', 'Project'],
        }

        self.namespaces[5] = {
            '_default': [u'Wikidata talk', u'WT', 'Project talk'],
        }

        self.namespaces[120] = {
            '_default':[u'Property', u'P'],
        }

        self.namespaces[121] = {
            '_default': u'Property talk',
        }

        self.namespaces[122] = {
            '_default': u'Query',
        }

        self.namespaces[123] = {
            '_default': u'Query talk',
        }

        self.namespaces[1198] = {
            '_default': u'Translations',
        }

        self.namespaces[1199] = {
            '_default': u'Translations talk',
        }

    def shared_data_repository(self, code, transcluded=False):
        """Always return a repository tupe. This enables testing whether
        the site object is the repository itself, see Site.is_data_repository()

        """
        if transcluded:
            return (None, None)
        else:
            return (code, self.name)
