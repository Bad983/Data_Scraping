import scrapy
import re


class DanteSpider(scrapy.Spider):
    name = "dante"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.TRAD_1_FIORE = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Fiore%20-%20tr.%20Casciani-Kleinhenz',
            'NAME': 'TRAD_1_FIORE',
            'TAG': 'td.t11.indenta',
            'PATH': '../../Opere/Dante/Traduzione/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': None,
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
        self.TRAD_1_RIME = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Dante%27s%20Lyric%20Poetry%20-%20tr.%20Foster-Boyde',
            'NAME': 'TRAD_1_RIME',
            'TAG': 'td.tprosa',
            'PATH': '../../Opere/Dante/Traduzione/',
            'OPEN_FILE_MODE': 'w',
            'MULTIPLE_PAGES': None,
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
            'OPEN_FILE_MODE': 'a'
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
            'OPEN_FILE_MODE': 'a'
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
            'OPEN_FILE_MODE': 'a'
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
            'OPEN_FILE_MODE': 'a'
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
            'OPEN_FILE_MODE': 'a'
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
            'OPEN_FILE_MODE': 'a'
        }

    def start_requests(self):
        opere = [
            # self.TRAD_1_FIORE,
            # self.TRAD_1_DETTO_AMORE,
            # self.TRAD_1_RIME,
            # self.ORIG_CACCIA_DIANA,
            self.ORIG_DIVINA_COMMEDIA_INFERNO,
            self.TRAD_2_DIVINA_COMMEDIA_INFERNO
            self.ORIG_DIVINA_COMMEDIA_PURGATORIO,
            self.TRAD_2_DIVINA_COMMEDIA_PURGATORIO
            self.ORIG_DIVINA_COMMEDIA_PARADISO,
            self.TRAD_2_DIVINA_COMMEDIA_PARADISO
            # self.TRAD_1_CONVIVIO,
            # self.TRAD_2_CONVIVIO
        ]
        for opera in opere:
            print(opera['URL'])
            multiple_pages = opera['MULTIPLE_PAGES']
            if multiple_pages is not None:
                for pages in multiple_pages:
                    url = opera['URL'].replace('numpages', pages)
                    yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(opera=opera))
                    if pages == "II":
                        break
            else:
                yield scrapy.Request(url=opera['URL'], callback=self.parse, cb_kwargs=dict(opera=opera))

    def parse(self, response, opera, **kwargs):
        page = opera['NAME']
        path = opera['PATH']
        tag = opera['TAG']
        pattern = opera['RE-PATTERN']
        open_file_mode = opera['OPEN_FILE_MODE']
        filename = path + f'{page}.txt'

        print(response.css(tag + "::text").getall())
        with open(filename, open_file_mode) as f:

            for resp in response.css(tag + "::text").getall():
                if pattern is not None:
                    resp = re.sub(pattern, '', resp)

                f.write(resp)

        self.log(f'Saved file {filename}')
