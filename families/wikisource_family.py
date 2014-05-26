# -*- coding: utf-8  -*-
import family

__version__ = '$Id: 69010e155cc2c6894b8105133541b8e31463aa73 $'


# The Wikimedia family that is known as Wikisource
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'wikisource'

        self.languages_by_size = [
            'fr', 'en', 'de', 'ru', 'it', 'pl', 'zh', 'he', 'es', 'sv', 'pt',
            'ca', 'cs', 'fa', 'hu', 'ar', 'ml', 'ko', 'sl', 'ro', 'te', 'fi',
            'vi', 'sa', 'sr', 'el', 'hr', 'no', 'th', 'hy', 'is', 'bn', 'nl',
            'la', 'gu', 'ja', 'vec', 'br', 'uk', 'eo', 'tr', 'mk', 'yi', 'ta',
            'id', 'be', 'da', 'az', 'li', 'et', 'as', 'mr', 'bg', 'bs', 'sah',
            'gl', 'kn', 'lt', 'cy', 'sk', 'zh-min-nan', 'fo',
        ]

        self.langs = dict([(lang, '%s.wikisource.org' % lang)
                           for lang in self.languages_by_size])
        self.langs['-'] = 'wikisource.org'

        # Override defaults
        self.namespaces[14]['as'] = [u'শ্ৰেণী', u'श्रेणी', u'শ্রেণী']
        self.namespaces[14]['bn'] = [u'বিষয়শ্রেণী']
        self.namespaces[15]['bn'] = [u'বিষয়শ্রেণী আলোচনা']
        self.namespaces[2]['ca'] = [u'Usuari']
        self.namespaces[3]['ca'] = [u'Usuari Discussió']
        self.namespaces[2]['cs'] = [u'Uživatel', u'Uživatelka']
        self.namespaces[3]['cs'] = [u'Diskuse s uživatelem', u'Diskuse s uživatelkou', u'Uživatel diskuse', u'Uživatelka diskuse']
        self.namespaces[9]['da'] = [u'MediaWiki diskussion', u'MediaWiki-diskussion']
        self.namespaces[13]['da'] = [u'Hjælp diskussion', u'Hjælp-diskussion']
        self.namespaces[2]['fa'] = [u'کاربر']
        self.namespaces[3]['fa'] = [u'بحث کاربر']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur', u'Discussion utilisatrice']
        self.namespaces[829]['ja'] = [u'モジュール・トーク']
        self.namespaces[2]['ko'] = [u'사용자']
        self.namespaces[3]['ko'] = [u'사용자토론']
        self.namespaces[12]['ml'] = [u'സഹായം', u'H', u'സ']
        self.namespaces[2]['pl'] = [u'Wikiskryba', u'Użytkowniczka', u'Użytkownik']
        self.namespaces[3]['pl'] = [u'Dyskusja wikiskryby', u'Dyskusja użytkowniczki', u'Dyskusja użytkownika']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[9]['ro'] = [u'Discuție MediaWiki', u'Discuţie MediaWiki']
        self.namespaces[6]['vec'] = [u'File', u'Imagine']
        self.namespaces[2]['zh'] = [u'User', u'用戶', u'用户']
        self.namespaces[3]['zh'] = [u'User talk', u'用戶對話', u'用戶討論', u'用户对话', u'用户讨论']
        self.namespaces[10]['zh'] = [u'Template', u'样板', u'模板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'帮助', u'幫助']
        self.namespaces[13]['zh'] = [u'Help talk', u'帮助对话', u'帮助讨论', u'幫助對話', u'幫助討論']
        self.namespaces[14]['zh'] = [u'Category', u'分类', u'分類']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            '-': u'Wikisource',
            'ar': [u'ويكي مصدر', u'Wikisource', u'وم'],
            'as': [u'ৱিকিউৎস', u'Wikisource'],
            'az': [u'VikiMənbə', u'Wikisource'],
            'be': [u'Вікікрыніцы', u'Wikisource', u'ВК'],
            'bg': [u'Уикиизточник', u'Wikisource'],
            'bn': [u'উইকিসংকলন', u'WS', u'Wikisource'],
            'br': [u'Wikimammenn', u'Wikisource'],
            'bs': [u'Wikizvor', u'Wikisource'],
            'ca': [u'Viquitexts', u'Wikisource'],
            'cs': [u'Wikizdroje', u'WS', u'WZ', u'Wikisource'],
            'cy': [u'Wicidestun', u'Wicitestun', u'Wikisource'],
            'da': u'Wikisource',
            'de': [u'Wikisource', u'WS'],
            'el': [u'Βικιθήκη', u'Wikisource'],
            'en': [u'Wikisource', u'WS'],
            'eo': [u'Vikifontaro', u'Wikisource'],
            'es': u'Wikisource',
            'et': [u'Vikitekstid', u'Wikisource'],
            'fa': [u'ویکی‌نبشته', u'Wikisource', u'ون'],
            'fi': [u'Wikiaineisto', u'Wikisource'],
            'fo': [u'Wikiheimild', u'Wikisource'],
            'fr': u'Wikisource',
            'gl': u'Wikisource',
            'gu': [u'વિકિસ્રોત', u'Wikisource'],
            'he': [u'ויקיטקסט', u'Wikisource'],
            'hr': [u'Wikizvor', u'Wikisource'],
            'hu': [u'Wikiforrás', u'Wikisource'],
            'hy': [u'Վիքիդարան', u'Wikisource'],
            'id': u'Wikisource',
            'is': [u'Wikiheimild', u'Wikisource'],
            'it': u'Wikisource',
            'ja': u'Wikisource',
            'kn': u'Wikisource',
            'ko': [u'위키문헌', u'Wikisource'],
            'la': [u'Vicifons', u'Wikisource'],
            'li': [u'Wikibrónne', u'Wikisource'],
            'lt': [u'Vikišaltiniai', u'Wikisource'],
            'mk': u'Wikisource',
            'ml': [u'വിക്കിഗ്രന്ഥശാല', u'WS', u'Wikisource'],
            'mr': [u'विकिस्रोत', u'Wikisource'],
            'nl': u'Wikisource',
            'no': [u'Wikikilden', u'Wikisource'],
            'pl': [u'Wikiźródła', u'WS', u'Wikisource'],
            'pt': u'Wikisource',
            'ro': u'Wikisource',
            'ru': [u'Викитека', u'Wikisource'],
            'sa': u'Wikisource',
            'sah': [u'Бикитиэкэ', u'Wikisource'],
            'sk': [u'Wikizdroje', u'Wikisource'],
            'sl': [u'Wikivir', u'Wikisource'],
            'sr': [u'Викизворник', u'Wikisource'],
            'sv': u'Wikisource',
            'ta': [u'விக்கிமூலம்', u'Wikisource', u'விக்கிபீடியா'],
            'te': [u'వికీసోర్స్', u'Wikisource'],
            'th': [u'วิกิซอร์ซ', u'Wikisource'],
            'tr': [u'Vikikaynak', u'VikiKaynak', u'Wikisource'],
            'uk': [u'Вікіджерела', u'Wikisource', u'ВД'],
            'vec': u'Wikisource',
            'vi': u'Wikisource',
            'yi': [u'װיקיביבליאָטעק', u'Wikisource', u'וויקיביבליאטעק'],
            'zh': u'Wikisource',
            'zh-min-nan': u'Wikisource',
        }
        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            '-': u'Wikisource talk',
            'ar': [u'نقاش ويكي مصدر', u'نو'],
            'as': [u'ৱিকিউ স বাৰ্তা', u'ৱিকিউৎস वार्ता', u'ৱিকিউৎস বার্তা'],
            'az': u'VikiMənbə müzakirəsi',
            'be': [u'Размовы пра Вікікрыніцы', u'Вікікрыніцы размовы'],
            'bg': u'Уикиизточник беседа',
            'bn': [u'উইকিসংকলন আলোচনা', u'উইকিসংকলন আলাপ'],
            'br': u'Kaozeadenn Wikimammenn',
            'bs': u'Razgovor s Wikizvor',
            'ca': u'Viquitexts Discussió',
            'cs': [u'Diskuse k Wikizdrojům', u'Wikisource diskuse', u'Wikisource talk', u'Wikizdroje diskuse'],
            'cy': [u'Sgwrs Wicidestun', u'Sgwrs Wicitestun'],
            'da': [u'Wikisource diskussion', u'Wikisource-diskussion'],
            'de': u'Wikisource Diskussion',
            'el': [u'Συζήτηση Βικιθήκη', u'Βικιθήκη συζήτηση'],
            'en': [u'Wikisource talk', u'WT'],
            'eo': u'Vikifontaro diskuto',
            'es': u'Wikisource discusión',
            'et': [u'Vikitekstide arutelu', u'Vikitekstid arutelu'],
            'fa': u'بحث ویکی‌نبشته',
            'fi': u'Keskustelu Wikiaineistosta',
            'fo': [u'Wikiheimild-kjak', u'Wikiheimild kjak'],
            'fr': u'Discussion Wikisource',
            'gl': u'Conversa Wikisource',
            'gu': u'વિકિસ્રોત ચર્ચા',
            'he': u'שיחת ויקיטקסט',
            'hr': u'Razgovor o Wikizvoru',
            'hu': [u'Wikiforrás-vita', u'Wikiforrás vita'],
            'hy': u'Վիքիդարանի քննարկում',
            'id': u'Pembicaraan Wikisource',
            'is': u'Wikiheimildspjall',
            'it': u'Discussioni Wikisource',
            'ja': [u'Wikisource・トーク', u'Wikisource‐ノート'],
            'kn': u'Wikisource ಚರ್ಚೆ',
            'ko': [u'위키문헌토론', u'Wikisource talk'],
            'la': u'Disputatio Vicifontis',
            'li': u'Euverlèk Wikibrónne',
            'lt': u'Vikišaltiniai aptarimas',
            'mk': u'Разговор за Wikisource',
            'ml': u'വിക്കിഗ്രന്ഥശാല സംവാദം',
            'mr': u'विकिस्रोत चर्चा',
            'nl': u'Overleg Wikisource',
            'no': u'Wikikilden-diskusjon',
            'pl': u'Dyskusja Wikiźródeł',
            'pt': u'Wikisource Discussão',
            'ro': [u'Discuție Wikisource', u'Discuţie Wikisource'],
            'ru': u'Обсуждение Викитеки',
            'sa': [u'Wikisourceसम्भाषणम्', u'Wikisourceसंभाषणं'],
            'sah': u'Бикитиэкэ Ырытыы',
            'sk': [u'Diskusia k Wikizdrojom', u'Komentár k Wikipédii', u'Wikisource talk'],
            'sl': u'Pogovor o Wikiviru',
            'sr': [u'Разговор о Викизворнику', u'Razgovor o Викизворник'],
            'sv': u'Wikisourcediskussion',
            'ta': [u'விக்கிமூலம் பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'te': u'వికీసోర్స్ చర్చ',
            'th': u'คุยเรื่องวิกิซอร์ซ',
            'tr': [u'Vikikaynak tartışma', u'Oluşturuluyor VikiKaynak tartışma'],
            'uk': [u'Обговорення Вікіджерел', u'Обговорення Wikisource'],
            'vec': u'Discussion Wikisource',
            'vi': u'Thảo luận Wikisource',
            'yi': [u'װיקיביבליאָטעק רעדן', u'וויקיביבליאטעק רעדן'],
            'zh': [u'Wikisource talk', u'Wikisource討論', u'Wikisource讨论'],
            'zh-min-nan': u'Wikisource討論',
        }

        self.namespaces[90] = {
            'sv': u'Tråd',
        }

        self.namespaces[91] = {
            'sv': u'Tråddiskussion',
        }

        self.namespaces[92] = {
            'sv': u'Summering',
        }

        self.namespaces[93] = {
            'sv': u'Summeringsdiskussion',
        }

        self.namespaces[100] = {
            'ar': u'بوابة',
            'az': u'Portal',
            'bg': u'Автор',
            'bn': u'লেখক',
            'br': u'Meneger',
            'cs': u'Autor',
            'el': u'Σελίδα',
            'en': u'Portal',
            'fa': [u'درگاه', u'Portal'],
            'fr': u'Transwiki',
            'he': u'קטע',
            'hr': u'Autor',
            'hu': u'Szerző',
            'hy': u'Հեղինակ',
            'id': u'Pengarang',
            'is': u'Gátt',
            'kn': u'ಸಂಪುಟ',
            'ko': u'저자',
            'ml': u'രചയിതാവ്',
            'mr': u'दालन',
            'nl': u'Hoofdportaal',
            'pl': u'Strona',
            'pt': u'Portal',
            'sl': u'Stran',
            'sr': u'Аутор',
            'te': u'ద్వారము',
            'tr': u'Kişi',
            'vec': u'Autor',
            'vi': u'Chủ đề',
        }

        self.namespaces[101] = {
            'ar': u'نقاش البوابة',
            'az': u'Portal müzakirəsi',
            'bg': u'Автор беседа',
            'bn': u'লেখক আলাপ',
            'br': u'Kaozeadenn meneger',
            'cs': u'Diskuse k autorovi',
            'el': u'Συζήτηση σελίδας',
            'en': u'Portal talk',
            'fa': [u'بحث درگاه', u'Portal talk'],
            'fr': u'Discussion Transwiki',
            'he': u'שיחת קטע',
            'hr': u'Razgovor o autoru',
            'hu': u'Szerző vita',
            'hy': u'Հեղինակի քննարկում',
            'id': u'Pembicaraan Pengarang',
            'is': u'Gáttarspjall',
            'kn': u'ಸಂಪುಟ ಚರ್ಚೆ',
            'ko': u'저자토론',
            'ml': u'രചയിതാവിന്റെ സംവാദം',
            'mr': u'दालन चर्चा',
            'nl': u'Overleg hoofdportaal',
            'pl': u'Dyskusja strony',
            'pt': u'Portal Discussão',
            'sl': u'Pogovor o strani',
            'sr': u'Разговор о аутору',
            'te': u'ద్వారము చర్చ',
            'tr': u'Kişi tartışma',
            'vec': u'Discussion autor',
            'vi': u'Thảo luận Chủ đề',
        }

        self.namespaces[102] = {
            'ar': u'مؤلف',
            'az': u'Müəllif',
            'be': u'Аўтар',
            'bn': u'নির্ঘণ্ট',
            'br': u'Pajenn',
            'ca': u'Pàgina',
            'da': u'Forfatter',
            'de': u'Seite',
            'el': u'Βιβλίο',
            'en': u'Author',
            'eo': u'Aŭtoro',
            'es': u'Página',
            'et': u'Lehekülg',
            'fa': [u'پدیدآورنده', u'Author'],
            'fr': u'Auteur',
            'hr': u'Stranica',
            'hy': u'Պորտալ',
            'id': u'Indeks',
            'is': u'Höfundur',
            'it': u'Autore',
            'kn': u'ಕರ್ತೃ',
            'la': u'Scriptor',
            'mk': u'Автор',
            'ml': u'കവാടം',
            'mr': [u'साहित्यिक', u'Author'],
            'nb': u'Forfatter',
            'nl': u'Auteur',
            'no': u'Forfatter',
            'pl': u'Indeks',
            'pt': u'Autor',
            'ro': u'Autor',
            'sr': u'Додатак',
            'te': u'రచయిత',
            'uk': u'Автор',
            'vec': u'Pagina',
            'vi': u'Tác gia',
            'zh': u'Author',
        }

        self.namespaces[103] = {
            'ar': u'نقاش المؤلف',
            'az': u'Müəllif müzakirəsi',
            'be': u'Размовы пра аўтара',
            'bn': u'নির্ঘণ্ট আলাপ',
            'br': u'Kaozeadenn pajenn',
            'ca': u'Pàgina Discussió',
            'da': u'Forfatterdiskussion',
            'de': u'Seite Diskussion',
            'el': u'Συζήτηση βιβλίου',
            'en': u'Author talk',
            'eo': u'Aŭtoro-Diskuto',
            'es': u'Página Discusión',
            'et': u'Lehekülje arutelu',
            'fa': [u'گفتگو پدیدآورنده', u'Author talk'],
            'fr': u'Discussion Auteur',
            'hr': u'Razgovor o stranici',
            'hy': u'Պորտալի քննարկում',
            'id': u'Pembicaraan Indeks',
            'is': u'Höfundarspjall',
            'it': u'Discussioni autore',
            'kn': u'ಕರ್ತೃ ಚರ್ಚೆ',
            'la': u'Disputatio Scriptoris',
            'mk': u'Разговор за автор',
            'ml': u'കവാടത്തിന്റെ സംവാദം',
            'mr': [u'साहित्यिक चर्चा', u'Author talk'],
            'nb': u'Forfatterdiskusjon',
            'nl': u'Overleg auteur',
            'no': u'Forfatterdiskusjon',
            'pl': u'Dyskusja indeksu',
            'pt': u'Autor Discussão',
            'ro': u'Discuție Autor',
            'sr': u'Разговор о додатку',
            'te': u'రచయిత చర్చ',
            'uk': u'Обговорення автора',
            'vec': u'Discussion pagina',
            'vi': u'Thảo luận Tác gia',
            'zh': u'Author talk',
        }

        self.namespaces[104] = {
            '-': u'Page',
            'ar': u'صفحة',
            'as': u'পৃষ্ঠা',
            'be': u'Старонка',
            'bn': u'পাতা',
            'br': [u'Oberour', u'Author'],
            'ca': [u'Llibre', u'Index'],
            'cy': u'Tudalen',
            'da': u'Side',
            'de': u'Index',
            'en': u'Page',
            'eo': u'Paĝo',
            'es': u'Índice',
            'et': [u'Register', u'Index'],
            'fa': [u'برگه', u'Page'],
            'fr': u'Page',
            'gu': u'પૃષ્ઠ',
            'he': u'עמוד',
            'hr': [u'Sadržaj', u'Index'],
            'hu': u'Oldal',
            'hy': u'Էջ',
            'id': u'Halaman',
            'it': u'Progetto',
            'kn': u'ಪುಟ',
            'la': u'Pagina',
            'ml': [u'സൂചിക', u'Index'],
            'mr': u'पान',
            'nl': u'Pagina',
            'no': u'Side',
            'pl': [u'Autor', u'Author'],
            'pt': [u'Galeria', u'Index'],
            'ro': u'Pagină',
            'ru': u'Страница',
            'sa': u'पुटम्',
            'sl': [u'Kazalo', u'Index'],
            'sv': u'Sida',
            'te': [u'పుట', u'పేజీ', u'Page'],
            'vec': [u'Indice', u'Index'],
            'vi': u'Trang',
            'zh': u'Page',
        }

        self.namespaces[105] = {
            '-': u'Page talk',
            'ar': u'نقاش الصفحة',
            'as': u'পৃষ্ঠা আলোচনা',
            'be': u'Размовы пра старонку',
            'bn': u'পাতা আলাপ',
            'br': [u'Kaozeadenn oberour', u'Author talk'],
            'ca': [u'Llibre Discussió', u'Index talk'],
            'cy': u'Sgwrs Tudalen',
            'da': u'Sidediskussion',
            'de': [u'Index Diskussion', u'Index talk'],
            'en': u'Page talk',
            'eo': u'Paĝo-Diskuto',
            'es': u'Índice Discusión',
            'et': [u'Registri arutelu', u'Index talk'],
            'fa': u'گفتگوی برگه',
            'fr': u'Discussion Page',
            'gu': u'પૃષ્ઠ ચર્ચા',
            'he': u'שיחת עמוד',
            'hr': [u'Razgovor o sadržaju', u'Index talk'],
            'hu': u'Oldal vita',
            'hy': u'Էջի քննարկում',
            'id': u'Pembicaraan Halaman',
            'it': u'Discussioni progetto',
            'kn': u'ಪುಟ ಚರ್ಚೆ',
            'la': u'Disputatio Paginae',
            'ml': [u'സൂചികയുടെ സംവാദം', u'Index talk'],
            'mr': u'पान चर्चा',
            'nl': u'Overleg pagina',
            'no': u'Sidediskusjon',
            'pl': [u'Dyskusja autora', u'Author talk'],
            'pt': [u'Galeria Discussão', u'Index talk'],
            'ro': u'Discuție Pagină',
            'ru': u'Обсуждение страницы',
            'sa': u'पुटसंवाद',
            'sl': [u'Pogovor o kazalu', u'Index talk'],
            'sv': u'Siddiskussion',
            'te': [u'పుట చర్చ', u'పేజీ చర్చ', u'Page talk'],
            'vec': [u'Discussion indice', u'Index talk'],
            'vi': u'Thảo luận Trang',
            'zh': u'Page talk',
        }

        self.namespaces[106] = {
            '-': u'Index',
            'ar': u'فهرس',
            'as': u'সূচী',
            'be': u'Індэкс',
            'bn': u'প্রবেশদ্বার',
            'ca': u'Autor',
            'cy': u'Indecs',
            'da': u'Indeks',
            'en': u'Index',
            'eo': u'Indekso',
            'et': u'Autor',
            'fa': u'فهرست',
            'fr': u'Portail',
            'gu': u'સૂચિ',
            'he': u'ביאור',
            'hu': u'Index',
            'hy': u'Ինդեքս',
            'id': u'Portal',
            'it': u'Portale',
            'kn': u'ಪರಿವಿಡಿ',
            'la': u'Liber',
            'ml': u'താൾ',
            'mr': [u'अनुक्रमणिका', u'Index'],
            'nl': u'Index',
            'no': u'Indeks',
            'pt': u'Página',
            'ro': u'Index',
            'ru': u'Индекс',
            'sa': u'अनुक्रमणिका',
            'sv': u'Författare',
            'te': u'సూచిక',
            'vi': u'Mục lục',
            'zh': u'Index',
        }

        self.namespaces[107] = {
            '-': u'Index talk',
            'ar': u'نقاش الفهرس',
            'as': u'সূচী আলোচনা',
            'be': u'Размовы пра індэкс',
            'bn': u'প্রবেশদ্বার আলাপ',
            'ca': u'Autor Discussió',
            'cy': u'Sgwrs Indecs',
            'da': u'Indeksdiskussion',
            'en': u'Index talk',
            'eo': u'Indekso-Diskuto',
            'et': u'Autori arutelu',
            'fa': u'گفتگوی فهرست',
            'fr': u'Discussion Portail',
            'gu': u'સૂચિ ચર્ચા',
            'he': u'שיחת ביאור',
            'hu': u'Index vita',
            'hy': u'Ինդեքսի քննարկում',
            'id': u'Pembicaraan Portal',
            'it': u'Discussioni portale',
            'kn': u'ಪರಿವಿಡಿ ಚರ್ಚೆ',
            'la': u'Disputatio Libri',
            'ml': u'താളിന്റെ സംവാദം',
            'mr': [u'अनुक्रमणिका चर्चा', u'Index talk'],
            'nl': u'Overleg index',
            'no': u'Indeksdiskusjon',
            'pt': u'Página Discussão',
            'ro': u'Discuție Index',
            'ru': u'Обсуждение индекса',
            'sa': u'अनुक्रमणिकासंवाद',
            'sv': u'Författardiskussion',
            'te': u'సూచిక చర్చ',
            'vi': u'Thảo luận Mục lục',
            'zh': u'Index talk',
        }

        self.namespaces[108] = {
            '-': u'Author',
            'gu': u'સર્જક',
            'he': u'מחבר',
            'it': u'Pagina',
            'pt': u'Em Tradução',
            'sv': u'Index',
            'zh': u'Transwiki',
        }

        self.namespaces[109] = {
            '-': u'Author talk',
            'gu': u'સર્જક ચર્ચા',
            'he': u'שיחת מחבר',
            'it': u'Discussioni pagina',
            'pt': u'Discussão Em Tradução',
            'sv': u'Indexdiskussion',
            'zh': u'Transwiki talk',
        }

        self.namespaces[110] = {
            'he': u'תרגום',
            'it': u'Indice',
            'pt': u'Anexo',
        }

        self.namespaces[111] = {
            'he': u'שיחת תרגום',
            'it': u'Discussioni indice',
            'pt': u'Anexo Discussão',
        }

        self.namespaces[112] = {
            'fr': u'Livre',
            'he': u'מפתח',
        }

        self.namespaces[113] = {
            'fr': u'Discussion Livre',
            'he': u'שיחת מפתח',
        }
        self.namespaces[114] = {
            'en': u'Translation',
            'uk': u'Переклад',
        }
        self.namespaces[115] = {
            'en': u'Translation talk',
            'uk': u'Обговорення перекладу',
        }

        self.namespaces[250] = {
            'az': u'Page',
            'bg': u'Page',
            'bs': u'Page',
            'cs': u'Stránka',
            'fi': u'Sivu',
            'fo': u'Page',
            'gl': u'Page',
            'is': u'Blaðsíða',
            'ja': u'Page',
            'ko': u'Page',
            'li': u'Page',
            'lt': u'Page',
            'mk': u'Page',
            'sah': u'Page',
            'sk': u'Page',
            'sr': u'Page',
            'ta': u'Page',
            'th': u'หน้า',
            'tr': u'Page',
            'uk': u'Сторінка',
            'yi': u'Page',
            'zh-min-nan': u'Page',
        }

        self.namespaces[251] = {
            'az': u'Page talk',
            'bg': u'Page talk',
            'bs': u'Page talk',
            'cs': u'Diskuse ke stránce',
            'fi': u'Keskustelu sivusta',
            'fo': u'Page talk',
            'gl': u'Page talk',
            'is': u'Blaðsíðuspjall',
            'ja': u'Page talk',
            'ko': u'Page talk',
            'li': u'Page talk',
            'lt': u'Page talk',
            'mk': u'Page talk',
            'sah': u'Page talk',
            'sk': u'Page talk',
            'sr': u'Page talk',
            'ta': u'Page talk',
            'th': u'คุยเรื่องหน้า',
            'tr': u'Page talk',
            'uk': u'Обговорення сторінки',
            'yi': u'Page talk',
            'zh-min-nan': u'Page talk',
        }

        self.namespaces[252] = {
            'az': u'Index',
            'bg': u'Index',
            'bs': u'Index',
            'cs': u'Index',
            'fi': u'Hakemisto',
            'fo': u'Index',
            'gl': u'Index',
            'is': u'Frumrit',
            'ja': u'Index',
            'ko': u'Index',
            'li': u'Index',
            'lt': u'Index',
            'mk': u'Index',
            'sah': u'Index',
            'sk': u'Index',
            'sr': u'Index',
            'ta': u'Index',
            'th': u'ดัชนี',
            'tr': u'Index',
            'uk': u'Індекс',
            'yi': u'Index',
            'zh-min-nan': u'Index',
        }

        self.namespaces[253] = {
            'az': u'Index talk',
            'bg': u'Index talk',
            'bs': u'Index talk',
            'cs': u'Diskuse k indexu',
            'fi': u'Keskustelu hakemistosta',
            'fo': u'Index talk',
            'gl': u'Index talk',
            'is': u'Frumritsspjall',
            'ja': u'Index talk',
            'ko': u'Index talk',
            'li': u'Index talk',
            'lt': u'Index talk',
            'mk': u'Index talk',
            'sah': u'Index talk',
            'sk': u'Index talk',
            'sr': u'Index talk',
            'ta': u'Index talk',
            'th': u'คุยเรื่องดัชนี',
            'tr': u'Index talk',
            'uk': u'Обговорення індексу',
            'yi': u'Index talk',
            'zh-min-nan': u'Index talk',
        }

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'ca', 'el', 'fa', 'it', 'ko', 'no', 'pl', 'vi', 'zh',
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
            'ang': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Old_English_Wikisource
            'dk': 'da',
            'ht': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Haitian_Creole_Wikisource
            'jp': 'ja',
            'minnan': 'zh-min-nan',
            'nb': 'no',
            'tokipona': None,
            'zh-tw': 'zh',
            'zh-cn': 'zh'
        }

        self.authornamespaces = {
            '_default': [0],
            'ar': [102],
            'be': [102],
            'bg': [100],
            'ca': [106],
            'cs': [100],
            'da': [102],
            'en': [102],
            'eo': [102],
            'et': [106],
            'fa': [102],
            'fr': [102],
            'he': [108],
            'hr': [100],
            'hu': [100],
            'hy': [100],
            'it': [102],
            'ko': [100],
            'la': [102],
            'nl': [102],
            'no': [102],
            'pl': [104],
            'pt': [102],
            'ro': [102],
            'sv': [106],
            'tr': [100],
            'vi': [102],
            'zh': [102],
        }

        for key, values in self.authornamespaces.iteritems():
            for item in values:
                self.crossnamespace[item].update({key: self.authornamespaces})
    def shared_data_repository(self, code, transcluded=False):
        return ('wikidata', 'wikidata')
