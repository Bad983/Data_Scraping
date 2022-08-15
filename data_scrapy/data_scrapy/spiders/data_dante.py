import scrapy
import re


class DanteSpider(scrapy.Spider):
    name = "dante"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ORIG_FIORE = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Fiore%20-%20ed.%20Contini&livello1=numpages',
            'NAME': 'ORIG_FIORE',
            'TAG': 'td.t01.indenta',
            'PATH': '../../Opere/Dante/Originale/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII',
                               'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII',
                               'XXIX', 'XXX',
                               'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL',
                               'XLI', 'XLII',
                               'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L', 'LI', 'LII', 'LIII',
                               'LIV', 'LV', 'LVI',
                               'LVII', 'LVIII', 'LIX', 'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII',
                               'LXVIII', 'LXIX',
                               'LXX', 'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII', 'LXXVIII', 'LXXIX',
                               'LXXX',
                               'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI', 'LXXXVII', 'LXXXVIII',
                               'LXXXIX', 'XC',
                               'XCI', 'XCII', 'XCIII', 'XCIV', 'XCV', 'XCVI', 'XCVII', 'XCVIII', 'XCIX', 'C', 'CI',
                               'CII', 'CIII', 'CIV',
                               'CV', 'CVI', 'CVII', 'CVIII', 'CIX', 'CX', 'CXI', 'CXII', 'CXIII', 'CXIV', 'CXV', 'CXVI',
                               'CXVII',
                               'CXVIII', 'CXIX', 'CXX', 'CXXI', 'CXXII', 'CXXIII', 'CXXIV', 'CXXV', 'CXXVI', 'CXXVII',
                               'CXXVIII',
                               'CXXIX', 'CXXX', 'CXXXI', 'CXXXII', 'CXXXIII', 'CXXXIV', 'CXXXV', 'CXXXVI', 'CXXXVII',
                               'CXXXVIII',
                               'CXXXIX', 'CXL', 'CXLI', 'CXLII', 'CXLIII', 'CXLIV', 'CXLV', 'CXLVI', 'CXLVII',
                               'CXLVIII', 'CXLIX',
                               'CL', 'CLI', 'CLII', 'CLIII', 'CLIV', 'CLV', 'CLVI', 'CLVII', 'CLVIII', 'CLIX', 'CLX',
                               'CLXI', 'CLXII',
                               'CLXIII', 'CLXIV', 'CLXV', 'CLXVI', 'CLXVII', 'CLXVIII', 'CLXIX', 'CLXX', 'CLXXI',
                               'CLXXII', 'CLXXIII',
                               'CLXXIV', 'CLXXV', 'CLXXVI', 'CLXXVII', 'CLXXVIII', 'CLXXIX', 'CLXXX', 'CLXXXI',
                               'CLXXXII',
                               'CLXXXIII', 'CLXXXIV', 'CLXXXV', 'CLXXXVI', 'CLXXXVII', 'CLXXXVIII', 'CLXXXIX', 'CXC',
                               'CXCI',
                               'CXCII', 'CXCIII', 'CXCIV', 'CXCV', 'CXCVI', 'CXCVII', 'CXCVIII', 'CXCIX', 'CC', 'CCI',
                               'CCII',
                               'CCIII', 'CCIV', 'CCV', 'CCVI', 'CCVII', 'CCVIII', 'CCIX', 'CCX', 'CCXI', 'CCXII',
                               'CCXIII', 'CCXIV',
                               'CCXV', 'CCXVI', 'CCXVII', 'CCXVIII', 'CCXIX', 'CCXX', 'CCXXI', 'CCXXII', 'CCXXIII',
                               'CCXXIV',
                               'CCXXV', 'CCXXVI', 'CCXXVII', 'CCXXVIII', 'CCXXIX', 'CCXXX', 'CCXXXI', 'CCXXXII'],
            'RE-PATTERN': None
        }

        self.TRAD_1_FIORE = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Fiore%20-%20tr.%20Casciani-Kleinhenz&livello1=numpages',
            'NAME': 'TRAD_1_FIORE',
            'TAG': 'td.t11.indenta',
            'PATH': '../../Opere/Dante/Traduzione/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII',
                               'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII',
                               'XXIX', 'XXX',
                               'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL',
                               'XLI', 'XLII',
                               'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L', 'LI', 'LII', 'LIII',
                               'LIV', 'LV', 'LVI',
                               'LVII', 'LVIII', 'LIX', 'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII',
                               'LXVIII', 'LXIX',
                               'LXX', 'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII', 'LXXVIII', 'LXXIX',
                               'LXXX',
                               'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI', 'LXXXVII', 'LXXXVIII',
                               'LXXXIX', 'XC',
                               'XCI', 'XCII', 'XCIII', 'XCIV', 'XCV', 'XCVI', 'XCVII', 'XCVIII', 'XCIX', 'C', 'CI',
                               'CII', 'CIII', 'CIV',
                               'CV', 'CVI', 'CVII', 'CVIII', 'CIX', 'CX', 'CXI', 'CXII', 'CXIII', 'CXIV', 'CXV', 'CXVI',
                               'CXVII',
                               'CXVIII', 'CXIX', 'CXX', 'CXXI', 'CXXII', 'CXXIII', 'CXXIV', 'CXXV', 'CXXVI', 'CXXVII',
                               'CXXVIII',
                               'CXXIX', 'CXXX', 'CXXXI', 'CXXXII', 'CXXXIII', 'CXXXIV', 'CXXXV', 'CXXXVI', 'CXXXVII',
                               'CXXXVIII',
                               'CXXXIX', 'CXL', 'CXLI', 'CXLII', 'CXLIII', 'CXLIV', 'CXLV', 'CXLVI', 'CXLVII',
                               'CXLVIII', 'CXLIX',
                               'CL', 'CLI', 'CLII', 'CLIII', 'CLIV', 'CLV', 'CLVI', 'CLVII', 'CLVIII', 'CLIX', 'CLX',
                               'CLXI', 'CLXII',
                               'CLXIII', 'CLXIV', 'CLXV', 'CLXVI', 'CLXVII', 'CLXVIII', 'CLXIX', 'CLXX', 'CLXXI',
                               'CLXXII', 'CLXXIII',
                               'CLXXIV', 'CLXXV', 'CLXXVI', 'CLXXVII', 'CLXXVIII', 'CLXXIX', 'CLXXX', 'CLXXXI',
                               'CLXXXII',
                               'CLXXXIII', 'CLXXXIV', 'CLXXXV', 'CLXXXVI', 'CLXXXVII', 'CLXXXVIII', 'CLXXXIX', 'CXC',
                               'CXCI',
                               'CXCII', 'CXCIII', 'CXCIV', 'CXCV', 'CXCVI', 'CXCVII', 'CXCVIII', 'CXCIX', 'CC', 'CCI',
                               'CCII',
                               'CCIII', 'CCIV', 'CCV', 'CCVI', 'CCVII', 'CCVIII', 'CCIX', 'CCX', 'CCXI', 'CCXII',
                               'CCXIII', 'CCXIV',
                               'CCXV', 'CCXVI', 'CCXVII', 'CCXVIII', 'CCXIX', 'CCXX', 'CCXXI', 'CCXXII', 'CCXXIII',
                               'CCXXIV',
                               'CCXXV', 'CCXXVI', 'CCXXVII', 'CCXXVIII', 'CCXXIX', 'CCXXX', 'CCXXXI', 'CCXXXII'],
            'RE-PATTERN': None
        }

        self.TRAD_1_DETTO_AMORE = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Detto%20d%27Amore%20-%20tr.%20Casciani-Kleinhenz',
            'NAME': 'TRAD_1_DETTO_AMORE',
            'TAG': 'td.t10.nonindentare',
            'PATH': '../../Opere/Dante/Traduzione/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': None,
            'RE-PATTERN': None
        }

        self.ORIG_DETTO_AMORE = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Detto%20d%27Amore%20-%20ed.%20Allegretti',
            'NAME': 'ORIG_DETTO_AMORE',
            'TAG': 'td.t08.nonindentare',
            'PATH': '../../Opere/Dante/Originale/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': None,
            'RE-PATTERN': None
        }

        self.ORIG_RIME = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Rime%20-%20ed.%20Barbi&livello1=numpages',
            'NAME': 'ORIG_RIME',
            'TAG': 'td.t01.indenta',
            'PATH': '../../Opere/Dante/Originale/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI',
                               'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI',
                               'XLVII', 'XLVIII', 'XLIX', 'L', 'LI', 'LII', 'LIII', 'LIV', 'LV', 'LVI', 'LVII',
                               'LVIII', 'LIX', 'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII',
                               'LXVIII', 'LXIX', 'LXX', 'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII',
                               'LXXVIII', 'LXXIX', 'LXXX', 'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI',
                               'LXXXVII', 'LXXXVIII', 'LXXXIX'],
            'RE-PATTERN': None
        }

        self.TRAD_1_RIME = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Dante%27s%20Lyric%20Poetry%20-%20tr.%20Foster-Boyde&livello1=numpages',
            'NAME': 'TRAD_1_RIME',
            'TAG': 'td.tprosa',
            'PATH': '../../Opere/Dante/Traduzione/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI',
                               'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI',
                               'XLVII', 'XLVIII', 'XLIX', 'L', 'LI', 'LII', 'LIII', 'LIV', 'LV', 'LVI', 'LVII',
                               'LVIII', 'LIX', 'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII',
                               'LXVIII', 'LXIX', 'LXX', 'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII',
                               'LXXVIII', 'LXXIX', 'LXXX', 'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI',
                               'LXXXVII', 'LXXXVIII', 'LXXXIX'],
            'RE-PATTERN': None
        }

        self.ORIG_CACCIA_DIANA = {
            'URL': 'http://boccaccio.letteraturaoperaomnia.org/boccaccio_caccia_di_diana.html',
            'NAME': 'ORIG_CACCIA_DIANA',
            'TAG': 'blockquote',
            'PATH': '../../Opere/Dante/Originale/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': None,
            'RE-PATTERN': None
        }

        self.ORIG_DIVINA_COMMEDIA_INFERNO = {
            'URL': 'https://divinacommedia.weebly.com/inferno-canto-numpages.html',
            'NAME': 'ORIG_DIVINA_COMMEDIA_INFERNO',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV'],
            'TAG': 'td.wsite-multicol-col div.paragraph',
            'PATH': '../../Opere/Dante/Originale/',
            'RE-PATTERN': r'[0-9]',
            'OPEN_FILE_MODE': 'w'
        }

        self.TRAD_2_DIVINA_COMMEDIA_INFERNO = {
            'URL': 'https://divinacommedia.weebly.com/inferno-canto-numpages.html',
            'NAME': 'TRAD_2_DIVINA_COMMEDIA_INFERNO',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV'],
            'TAG': 'td.wsite-multicol-col div.paragraph em span',
            'PATH': '../../Opere/Dante/Traduzione/',
            'RE-PATTERN': r'[0-9]',
            'OPEN_FILE_MODE': 'w'
        }

        self.TRAD_3_DIVINA_COMMEDIA_INFERNO_EN = {
            'URL': 'http://dantelab.dartmouth.edu/reader?reader%5Bcantica%5D=1&reader%5Bcanto%5D=numpages',
            'NAME': 'TRAD_3_DIVINA_COMMEDIA_INFERNO_EN',
            'MULTIPLE_PAGES': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                               '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                               '31', '32', '33', '34'],
            'TAG': 'div.well.tab-pane.active div.translation-section div.row-fluid div.canto div.canto_text.span9 p',
            'PATH': '../../Opere/Dante/Traduzione/',
            'RE-PATTERN': None,
            'OPEN_FILE_MODE': 'w'
        }

        self.TRAD_4_DIVINA_COMMEDIA_INFERNO_DE = {
            'URL': 'http://dantelab.dartmouth.edu/reader?reader%5Bcantica%5D=1&reader%5Bcanto%5D=numpages',
            'NAME': 'TRAD_4_DIVINA_COMMEDIA_INFERNO_DE',
            'MULTIPLE_PAGES': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                               '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                               '31', '32', '33', '34'],
            'TAG': 'div.well.tab-pane.active div.translation-section div.row-fluid div.canto div.canto_text.span9 p',
            'PATH': '../../Opere/Dante/Traduzione/',
            'RE-PATTERN': None,
            'OPEN_FILE_MODE': 'w'
        }

        self.ORIG_DIVINA_COMMEDIA_PURGATORIO = {
            'URL': 'https://divinacommedia.weebly.com/purgatorio-canto-numpages.html',
            'NAME': 'ORIG_DIVINA_COMMEDIA_PURGATORIO',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII'],
            'TAG': 'td.wsite-multicol-col div.paragraph',
            'PATH': '../../Opere/Dante/Originale/',
            'RE-PATTERN': r'[0-9]',
            'OPEN_FILE_MODE': 'w'
        }

        self.TRAD_2_DIVINA_COMMEDIA_PURGATORIO = {
            'URL': 'https://divinacommedia.weebly.com/purgatorio-canto-numpages.html',
            'NAME': 'TRAD_2_DIVINA_COMMEDIA_PURGATORIO',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII'],
            'TAG': 'td.wsite-multicol-col div.paragraph em span',
            'PATH': '../../Opere/Dante/Traduzione/',
            'RE-PATTERN': r'[0-9]',
            'OPEN_FILE_MODE': 'w'
        }

        self.ORIG_DIVINA_COMMEDIA_PARADISO = {
            'URL': 'https://divinacommedia.weebly.com/paradiso-canto-numpages.html',
            'NAME': 'ORIG_DIVINA_COMMEDIA_PARADISO',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII'],
            'TAG': 'td.wsite-multicol-col div.paragraph',
            'PATH': '../../Opere/Dante/Originale/',
            'RE-PATTERN': r'[0-9]',
            'OPEN_FILE_MODE': 'w'
        }

        self.TRAD_2_DIVINA_COMMEDIA_PARADISO = {
            'URL': 'https://divinacommedia.weebly.com/paradiso-canto-numpages.html',
            'NAME': 'TRAD_2_DIVINA_COMMEDIA_PARADISO',
            'MULTIPLE_PAGES': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV',
                               'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
                               'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII'],
            'TAG': 'td.wsite-multicol-col div.paragraph em span',
            'PATH': '../../Opere/Dante/Traduzione/',
            'RE-PATTERN': r'[0-9]',
            'OPEN_FILE_MODE': '3'
        }

    def start_requests(self):
        opere = [
            # self.ORIG_FIORE,
            # self.TRAD_1_FIORE,
            # self.TRAD_1_DETTO_AMORE,
            # self.ORIG_DETTO_AMORE,
            # self.ORIG_RIME,
            # self.TRAD_1_RIME,
            # self.ORIG_CACCIA_DIANA,
            # self.ORIG_DIVINA_COMMEDIA_INFERNO,
            # self.TRAD_2_DIVINA_COMMEDIA_INFERNO,
            # self.ORIG_DIVINA_COMMEDIA_PURGATORIO,
            # self.TRAD_2_DIVINA_COMMEDIA_PURGATORIO,
            # self.ORIG_DIVINA_COMMEDIA_PARADISO,
            # self.TRAD_2_DIVINA_COMMEDIA_PARADISO,
            # self.TRAD_3_DIVINA_COMMEDIA_INFERNO_EN,
            self.TRAD_4_DIVINA_COMMEDIA_INFERNO_DE
        ]
        for opera in opere:
            print(opera['URL'])
            multiple_pages = opera['MULTIPLE_PAGES']
            if multiple_pages is not None:
                for pages in multiple_pages:
                    # print(pages)
                    url = opera['URL'].replace('numpages', pages)
                    # print(url)
                    yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(opera=opera, pages=pages))
                    if pages == "1":
                        break
            else:
                yield scrapy.Request(url=opera['URL'], callback=self.parse, cb_kwargs=dict(opera=opera))

    def parse(self, response, opera, pages='1', **kwargs):
        name = opera['NAME']
        path = opera['PATH']
        tag = opera['TAG']
        pattern = opera['RE-PATTERN']
        open_file_mode = opera['OPEN_FILE_MODE']
        filename = path + f'{name}_{pages}.txt'
        # print("******************************")
        # print(response.url)
        # print("******************************")

        with open(filename, open_file_mode) as f:

            for resp in response.css(tag + "::text").getall():
                # print(resp)
                if pattern is not None:
                    resp = re.sub(pattern, '', resp)

                f.write(resp + '\n')

        self.log(f'Saved file {filename}')
