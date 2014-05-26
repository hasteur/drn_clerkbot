# -*- coding: utf-8  -*-
import family

__version__ = '$Id: 766bc5635740e5463421e407f6c2e97d916d7dac $'


# The Wikimedia family that is known as Wikibooks
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'wikibooks'

        self.languages_by_size = [
            'en', 'de', 'fr', 'hu', 'ja', 'it', 'es', 'pt', 'nl', 'pl', 'he',
            'vi', 'id', 'sq', 'ca', 'fi', 'ru', 'fa', 'cs', 'zh', 'sv', 'da',
            'hr', 'tr', 'no', 'th', 'sr', 'ar', 'gl', 'ko', 'ta', 'mk', 'tl',
            'ro', 'is', 'ka', 'tt', 'lt', 'az', 'eo', 'uk', 'bg', 'sk', 'sl',
            'el', 'hy', 'ms', 'si', 'li', 'la', 'ml', 'ang', 'ur', 'ia', 'cv',
            'et', 'bn', 'hi', 'mr', 'oc', 'km', 'kk', 'eu', 'fy', 'ie', 'ne',
            'sa', 'te', 'af', 'tg', 'ky', 'bs', 'pa', 'mg', 'be', 'cy',
            'zh-min-nan', 'ku', 'uz',
        ]

        self.langs = dict([(lang, '%s.wikibooks.org' % lang)
                           for lang in self.languages_by_size])

        # Override defaults
        self.namespaces[14]['bn'] = [u'বিষয়শ্রেণী']
        self.namespaces[15]['bn'] = [u'বিষয়শ্রেণী আলোচনা']
        self.namespaces[2]['ca'] = [u'Usuari']
        self.namespaces[3]['ca'] = [u'Usuari Discussió']
        self.namespaces[2]['cs'] = [u'Uživatel', u'Uživatelka']
        self.namespaces[3]['cs'] = [u'Diskuse s uživatelem', u'Diskuse s uživatelkou', u'Uživatel diskuse', u'Uživatelka diskuse']
        self.namespaces[9]['da'] = [u'MediaWiki diskussion', u'MediaWiki-diskussion']
        self.namespaces[13]['da'] = [u'Hjælp diskussion', u'Hjælp-diskussion']
        self.namespaces[14]['en'] = [u'Category', u'CAT']
        self.namespaces[2]['fa'] = [u'کاربر']
        self.namespaces[3]['fa'] = [u'بحث کاربر']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur', u'Discussion utilisatrice']
        self.namespaces[8]['hi'] = [u'मीडियाविकि']
        self.namespaces[9]['hi'] = [u'मीडियाविकि वार्ता']
        self.namespaces[10]['hi'] = [u'साँचा']
        self.namespaces[11]['hi'] = [u'साँचा वार्ता']
        self.namespaces[829]['ja'] = [u'モジュール・トーク']
        self.namespaces[2]['ko'] = [u'사용자']
        self.namespaces[3]['ko'] = [u'사용자토론']
        self.namespaces[2]['pl'] = [u'Wikipedysta', u'Użytkowniczka', u'Użytkownik', u'Wikipedystka']
        self.namespaces[3]['pl'] = [u'Dyskusja wikipedysty', u'Dyskusja użytkowniczki', u'Dyskusja użytkownika', u'Dyskusja wikipedystki']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[9]['ro'] = [u'Discuție MediaWiki', u'Discuţie MediaWiki']
        self.namespaces[14]['tr'] = [u'Kategori', u'KAT']
        self.namespaces[10]['zh'] = [u'Template', u'样板', u'模板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'使用說明', u'帮助', u'幫助']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            'af': u'Wikibooks',
            'ang': u'Wikibooks',
            'ar': [u'ويكي الكتب', u'Wikibooks'],
            'az': [u'Vikikitab', u'Wikibooks'],
            'be': u'Wikibooks',
            'bg': [u'Уикикниги', u'Wikibooks'],
            'bn': [u'উইকিবই', u'WB', u'Wikibooks'],
            'bs': [u'Wikiknjige', u'Wikibooks'],
            'ca': [u'Viquillibres', u'Wikibooks'],
            'cs': [u'Wikiknihy', u'WB', u'WK', u'Wikibooks'],
            'cv': u'Wikibooks',
            'cy': [u'Wicilyfrau', u'Wikibooks'],
            'da': u'Wikibooks',
            'de': u'Wikibooks',
            'el': [u'Βικιβιβλία', u'Wikibooks'],
            'en': [u'Wikibooks', u'WB'],
            'eo': [u'Vikilibroj', u'Wikibooks'],
            'es': [u'Wikilibros', u'Wikibooks'],
            'et': [u'Vikiõpikud', u'Wikibooks'],
            'eu': u'Wikibooks',
            'fa': [u'ویکی‌کتاب', u'Wikibooks', u'وک'],
            'fi': [u'Wikikirjasto', u'Wikibooks'],
            'fr': [u'Wikilivres', u'WL', u'Wikibooks'],
            'fy': u'Wikibooks',
            'gl': u'Wikibooks',
            'he': [u'ויקיספר', u'Wikibooks'],
            'hi': u'Wikibooks',
            'hr': [u'Wikiknjige', u'Wikibooks'],
            'hu': [u'Wikikönyvek', u'Wikibooks'],
            'hy': [u'Վիքիգրքեր', u'Wikibooks'],
            'ia': u'Wikibooks',
            'id': [u'Wikibuku', u'Wikibooks'],
            'ie': u'Wikibooks',
            'is': [u'Wikibækur', u'Wikibooks'],
            'it': [u'Wikibooks', u'WB'],
            'ja': u'Wikibooks',
            'ka': [u'ვიკიწიგნები', u'Wikibooks'],
            'kk': [u'Уикикітап', u'Wikibooks'],
            'km': u'Wikibooks',
            'ko': [u'위키책', u'Wikibooks'],
            'ku': [u'Wîkîpirtûk', u'Wikibooks'],
            'ky': u'Wikibooks',
            'la': [u'Vicilibri', u'Wikibooks'],
            'li': [u'Wikibeuk', u'Wikibooks'],
            'lt': u'Wikibooks',
            'mg': u'Wikibooks',
            'mk': u'Wikibooks',
            'ml': [u'വിക്കിപാഠശാല', u'Wikibooks', u'വിക്കി‌‌ പുസ്തകശാല'],
            'mr': u'Wikibooks',
            'ms': u'Wikibooks',
            'ne': u'Wikibooks',
            'nl': u'Wikibooks',
            'no': [u'Wikibøker', u'Wikibooks'],
            'oc': [u'Wikilibres', u'Wikibooks'],
            'pa': u'Wikibooks',
            'pl': [u'Wikibooks', u'WB'],
            'pt': [u'Wikilivros', u'Wikibooks'],
            'ro': [u'Wikimanuale', u'Wikibooks'],
            'ru': [u'Викиучебник', u'Wikibooks', u'ВУ'],
            'sa': u'Wikibooks',
            'si': [u'විකිපොත්', u'Wikibooks'],
            'sk': [u'Wikiknihy', u'Wikibooks'],
            'sl': [u'Wikiknjige', u'Wikibooks'],
            'sq': u'Wikibooks',
            'sr': [u'Викикњиге', u'Wikibooks'],
            'sv': u'Wikibooks',
            'ta': [u'விக்கிநூல்கள்', u'Wikibooks', u'விக்கிபீடியா'],
            'te': u'Wikibooks',
            'tg': u'Wikibooks',
            'th': [u'วิกิตำรา', u'Wikibooks'],
            'tl': u'Wikibooks',
            'tr': [u'Vikikitap', u'VK', u'Wikibooks'],
            'tt': u'Wikibooks',
            'uk': [u'Вікіпідручник', u'Wikibooks', u'ВП'],
            'ur': [u'وکی کتب', u'Wikibooks'],
            'uz': [u'Vikikitob', u'Wikibooks'],
            'vi': u'Wikibooks',
            'zh': [u'Wikibooks', u'WB', u'維基教科書', u'维基教科书'],
            'zh-min-nan': u'Wikibooks',
        }

        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            'af': u'Wikibooksbespreking',
            'ang': u'Wikibooks talk',
            'ar': u'نقاش ويكي الكتب',
            'az': [u'Vikikitab müzakirəsi', u'Wikibooks müzakirəsi', u'Wikibooks talk'],
            'be': [u'Размовы пра Wikibooks', u'Wikibooks размовы'],
            'bg': u'Уикикниги беседа',
            'bn': [u'উইকিবই আলোচনা', u'উইকিবই আলাপ'],
            'bs': u'Razgovor s Wikiknjigama',
            'ca': u'Viquillibres Discussió',
            'cs': [u'Diskuse k Wikiknihám', u'Wikibooks diskuse', u'Wikibooks talk', u'Wikiknihy diskuse'],
            'cv': u'Wikibooks сӳтсе явмалли',
            'cy': u'Sgwrs Wicilyfrau',
            'da': [u'Wikibooks diskussion', u'Wikibooks-diskussion'],
            'de': u'Wikibooks Diskussion',
            'el': [u'Συζήτηση Βικιβιβλία', u'Βικιβιβλία συζήτηση'],
            'en': u'Wikibooks talk',
            'eo': [u'Vikilibroj-Diskuto', u'Vikilibroj diskuto'],
            'es': u'Wikilibros discusión',
            'et': [u'Vikiõpikute arutelu', u'Vikiõpikud arutelu'],
            'eu': u'Wikibooks eztabaida',
            'fa': u'بحث ویکی‌کتاب',
            'fi': u'Keskustelu Wikikirjastosta',
            'fr': u'Discussion Wikilivres',
            'fy': u'Wikibooks oerlis',
            'gl': u'Conversa Wikibooks',
            'he': u'שיחת ויקיספר',
            'hi': u'Wikibooks वार्ता',
            'hr': u'Razgovor Wikiknjige',
            'hu': [u'Wikikönyvek-vita', u'Wikikönyvek vita'],
            'hy': u'Վիքիգրքերի քննարկում',
            'ia': u'Discussion Wikibooks',
            'id': [u'Pembicaraan Wikibuku', u'Pembicaraan Wikibooks'],
            'ie': u'Wikibooks Discussion',
            'is': u'Wikibækurspjall',
            'it': u'Discussioni Wikibooks',
            'ja': [u'Wikibooks・トーク', u'Wikibooks‐ノート'],
            'ka': u'ვიკიწიგნები განხილვა',
            'kk': [u'Уикикітап талқылауы', u'Уикикітап talqılawı', u'Уикикітап تالقىلاۋى'],
            'km': [u'ការពិភាក្សាអំពីWikibooks', u'Wikibooks ពិភាក្ស'],
            'ko': u'위키책토론',
            'ku': [u'Gotûbêja Wîkîpirtûkê', u'Wîkîpirtûk nîqaş'],
            'ky': u'Wikibooks баарлашуу',
            'la': u'Disputatio Vicilibrorum',
            'li': u'Euverlèk Wikibeuk',
            'lt': u'Wikibooks aptarimas',
            'mg': [u'Dinika amin\'ny Wikibooks', u'Discussion Wikibooks'],
            'mk': u'Разговор за Wikibooks',
            'ml': [u'വിക്കിപാഠശാല സംവാദം', u'Wikibooks talk', u'വിക്കി‌‌ പുസ്തകശാല സംവാദം'],
            'mr': u'Wikibooks चर्चा',
            'ms': [u'Perbincangan Wikibooks', u'Perbualan Wikibooks'],
            'ne': u'Wikibooks वार्ता',
            'nl': u'Overleg Wikibooks',
            'no': u'Wikibøker-diskusjon',
            'oc': u'Discussion Wikilibres',
            'pa': [u'Wikibooks ਗੱਲ-ਬਾਤ', u'Wikibooks ਚਰਚਾ'],
            'pl': u'Dyskusja Wikibooks',
            'pt': [u'Wikilivros Discussão', u'Wikibooks Discussão', u'Wikibooks Talk'],
            'ro': [u'Discuție Wikimanuale', u'Discuţie Wikibooks', u'Discuţie Wikimanuale'],
            'ru': u'Обсуждение Викиучебника',
            'sa': [u'Wikibooksसम्भाषणम्', u'Wikibooksसंभाषणं'],
            'si': [u'විකිපොත් සාකච්ඡාව', u'Wikibooks talk'],
            'sk': [u'Diskusia k Wikiknihám', u'Komentár k Wikipédii', u'Wikibooks talk'],
            'sl': u'Pogovor o Wikiknjigah',
            'sq': u'Wikibooks diskutim',
            'sr': [u'Разговор о викикњигама', u'Razgovor o Викикњиге'],
            'sv': u'Wikibooksdiskussion',
            'ta': [u'விக்கிநூல்கள் பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'te': u'Wikibooks చర్చ',
            'tg': [u'Баҳси Wikibooks', u'Wikibooks talk'],
            'th': [u'คุยเรื่องวิกิตำรา', u'คุยเรื่องWikibooks'],
            'tl': u'Usapang Wikibooks',
            'tr': u'Vikikitap tartışma',
            'tt': [u'Wikibooks бәхәсе', u'Wikibooks bäxäse', u'Обсуждение Wikibooks'],
            'uk': u'Обговорення Вікіпідручника',
            'ur': u'تبادلۂ خیال وکی کتب',
            'uz': [u'Vikikitob munozarasi', u'Vikikitob talk'],
            'vi': u'Thảo luận Wikibooks',
            'zh': [u'Wikibooks talk', u'Wikibooks討論', u'Wikibooks讨论'],
            'zh-min-nan': u'Wikibooks討論',
        }

        self.namespaces[90] = {
            'pt': u'Tópico',
        }

        self.namespaces[91] = {
            'pt': u'Tópico discussão',
        }

        self.namespaces[92] = {
            'pt': u'Resumo',
        }

        self.namespaces[93] = {
            'pt': u'Resumo discussão',
        }

        self.namespaces[100] = {
            'bn': u'উইকিশৈশব',
            'fr': u'Transwiki',
            'he': u'שער',
            'id': u'Resep',
            'it': u'Progetto',
            'ja': u'Transwiki',
            'ml': u'പാചകപുസ്തകം',
            'ms': u'Resipi',
            'ro': u'Raft',
            'ru': u'Полка',
            'tl': u'Pagluluto',
            'tr': u'Yemek',
            'uk': u'Полиця',
            'zh': u'Transwiki',
        }

        self.namespaces[101] = {
            'bn': u'উইকিশৈশব আলাপ',
            'fr': u'Discussion Transwiki',
            'he': u'שיחת שער',
            'id': u'Pembicaraan Resep',
            'it': u'Discussioni progetto',
            'ja': u'Transwiki‐ノート',
            'ml': u'പാചകപുസ്തകസം‌വാദം',
            'ms': u'Perbualan Resipi',
            'ro': u'Discuţie Raft',
            'ru': u'Обсуждение полки',
            'tl': u'Usapang pagluluto',
            'tr': u'Yemek tartışma',
            'uk': u'Обговорення полиці',
            'zh': u'Transwiki talk',
        }

        self.namespaces[102] = {
            'az': u'Resept',
            'bn': u'বিষয়',
            'ca': u'Viquiprojecte',
            'cy': u'Silff lyfrau',
            'de': u'Regal',
            'en': u'Cookbook',
            'fr': u'Wikijunior',
            'hy': u'Եփութուխ',
            'id': u'Wisata',
            'it': u'Ripiano',
            'ml': u'വിഷയം',
            'nl': u'Transwiki',
            'ro': u'Wikijunior',
            'ru': u'Импортировано',
            'sr': u'Кувар',
            'th': u'หัวเรื่อง',
            'uk': u'Рецепт',
            'vi': u'Chủ đề',
        }

        self.namespaces[103] = {
            'az': u'Resept müzakirəsi',
            'bn': u'বিষয় আলাপ',
            'ca': u'Viquiprojecte Discussió',
            'cy': u'Sgwrs Silff lyfrau',
            'de': u'Regal Diskussion',
            'en': u'Cookbook talk',
            'fr': u'Discussion Wikijunior',
            'hy': u'Եփութուխի քննարկում',
            'id': u'Pembicaraan Wisata',
            'it': u'Discussioni ripiano',
            'ml': u'വിഷയസം‌വാദം',
            'nl': u'Overleg transwiki',
            'ro': u'Discuţie Wikijunior',
            'ru': u'Обсуждение импортированного',
            'sr': u'Разговор о кувару',
            'th': u'คุยเรื่องหัวเรื่อง',
            'uk': u'Обговорення рецепта',
            'vi': u'Thảo luận Chủ đề',
        }

        self.namespaces[104] = {
            'az': u'Vikikitab',
            'he': u'מדף',
            'ka': u'თარო',
            'nl': u'Wikijunior',
            'pl': u'Wikijunior',
            'ro': u'Carte de bucate',
            'ru': u'Рецепт',
            'vi': u'Trẻ em',
        }

        self.namespaces[105] = {
            'az': u'Vikikitab müzakirəsi',
            'he': u'שיחת מדף',
            'ka': u'თარო განხილვა',
            'nl': u'Overleg Wikijunior',
            'pl': u'Dyskusja Wikijuniora',
            'ro': u'Discuţie Carte de bucate',
            'ru': u'Обсуждение рецепта',
            'vi': u'Thảo luận Trẻ em',
        }

        self.namespaces[106] = {
            'ru': u'Задача',
            'vi': u'Nấu ăn',
        }

        self.namespaces[107] = {
            'ru': u'Обсуждение задачи',
            'vi': u'Thảo luận Nấu ăn',
        }

        self.namespaces[108] = {
            'en': u'Transwiki',
        }

        self.namespaces[109] = {
            'en': u'Transwiki talk',
        }

        self.namespaces[110] = {
            'az': u'Vikiuşaq',
            'en': u'Wikijunior',
            'hy': u'Վիքիփոքրիկ',
            'tr': u'Vikiçocuk',
            'zh': u'Wikijunior',
        }

        self.namespaces[111] = {
            'az': u'Vikiuşaq müzakirəsi',
            'en': u'Wikijunior talk',
            'hy': u'Վիքիփոքրիկի քննարկում',
            'tr': u'Vikiçocuk tartışma',
            'zh': u'Wikijunior talk',
        }

        self.namespaces[112] = {
            'en': u'Subject',
            'si': u'විෂයය',
            'tr': u'Kitaplık',
            'zh': u'Subject',
        }

        self.namespaces[113] = {
            'en': u'Subject talk',
            'si': u'විෂයය සාකච්ඡාව',
            'tr': u'Kitaplık tartışma',
            'zh': u'Subject talk',
        }

        self.namespaces[114] = {
            'si': u'කණිෂ්ඨ විකි',
        }

        self.namespaces[115] = {
            'si': u'කණිෂ්ඨ විකි සාකච්ඡාව',
        }

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'af', 'ang', 'ca', 'fa', 'fy', 'it', 'nl', 'ru', 'th', 'zh',
        ]

        # Which languages have a special order for putting interlanguage links,
        # and what order is it? If a language is not in interwiki_putfirst,
        # alphabetical order on language code is used. For languages that are in
        # interwiki_putfirst, interwiki_putfirst is checked first, and
        # languages are put in the order given there. All other languages are
        # put after those, in code-alphabetical order.
        self.interwiki_putfirst = {
            'en': self.alphabetic,
            'fi': self.alphabetic,
            'fr': self.alphabetic,
            'he': ['en'],
            'hu': ['en'],
            'pl': self.alphabetic,
            'simple': self.alphabetic
        }

        self.obsolete = {
            'aa': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Afar_Wikibooks
            'ak': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Akan_Wikibooks
            'als': None,  # http://als.wikipedia.org/wiki/Wikipedia:Stammtisch/Archiv_2008-1#Afterwards.2C_closure_and_deletion_of_Wiktionary.2C_Wikibooks_and_Wikiquote_sites
            'as': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Assamese_Wikibooks
            'ast': None,
            'ay': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Aymar_Wikibooks
            'ba': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bashkir_Wikibooks
            'bi': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bislama_Wikibooks
            'bm': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bambara_Wikibooks
            'bo': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tibetan_Wikibooks
            'ch': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Chamorro_Wikibooks
            'co': None,   # https://bugzilla.wikimedia.org/show_bug.cgi?id=28644
            'dk': 'da',
            'ga': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Gaeilge_Wikibooks
            'got': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Gothic_Wikibooks
            'gn': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Guarani_Wikibooks
            'gu': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Gujarati_Wikibooks
            'jp': 'ja',
            'kn': None,   # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'ks': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kashmiri_Wikibooks
            'lb': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_L%C3%ABtzebuergesch_Wikibooks
            'ln': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Lingala_Wikibooks
            'lv': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Latvian_Wikibooks
            'mi': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Maori_Wikibooks
            'minnan': 'zh-min-nan',
            'mn': None,
            'my': None,
            'na': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nauruan_Wikibooks
            'nah': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nahuatl_Wikibooks
            'nb': 'no',
            'nds': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Plattd%C3%BC%C3%BCtsch_Wikibooks
            'ps': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Pashto_Wikibooks
            'qu': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Quechua_Wikibooks
            'rm': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Rumantsch_Wikibooks
            'se': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Sami_Wikibooks
            'simple': 'en',  # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'su': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Basa_Sunda_Wikibooks_(2)
            'sw': None,   # https://bugzilla.wikimedia.org/show_bug.cgi?id=25170
            'tk': None,
            'tokipona': None,
            'ug': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Uyghur_Wikibooks
            'vo': None,   # https://bugzilla.wikimedia.org/show_bug.cgi?id=37413
            'wa': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Walon_Wikibooks
            'xh': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Xhosa_Wikibooks
            'yo': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Yoruba_Wikibooks
            'za': None,   # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'zh-tw': 'zh',
            'zh-cn': 'zh',
            'zu': None,   # https://bugzilla.wikimedia.org/show_bug.cgi?id=25425
        }
