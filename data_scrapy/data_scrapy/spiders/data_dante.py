import scrapy

class DanteSpider(scrapy.Spider):
    name = "dante"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.TRAD_1_FIORE = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Fiore%20-%20tr.%20Casciani-Kleinhenz',
            'NAME': 'TRAD_1_FIORE',
            'TAG': 'td.t11.indenta',
            'PATH': '../../Opere/Dante/Traduzione/'
        }
        self.TRAD_1_DETTO_AMORE = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Detto%20d%27Amore%20-%20tr.%20Casciani-Kleinhenz',
            'NAME': 'TRAD_1_DETTO_AMORE',
            'TAG': 'td.t10.nonindentare',
            'PATH': '../../Opere/Dante/Traduzione/'
        }
        self.TRAD_1_RIME = {
            'URL': 'https://www.danteonline.it/opere/index.php?opera=Dante%27s%20Lyric%20Poetry%20-%20tr.%20Foster-Boyde',
            'NAME': 'TRAD_1_RIME',
            'TAG': 'td.tprosa',
            'PATH': '../../Opere/Dante/Traduzione/'
        }


        self.TRAD_1_CONVIVIO = 'https://www.danteonline.it/opere/index.php?opera=The%20Banquet%20-%20tr.%20Ryan'
        self.TRAD_2_CONVIVIO = 'https://www.danteonline.it/opere/index.php?opera=Dante%27s%20%22Il%20Convivio%22%20-%20tr.%20Lansing'
        self.path = "/Traduzioni/"

    def start_requests(self):
        opere = [
            self.TRAD_1_FIORE,
            self.TRAD_1_DETTO_AMORE,
            self.TRAD_1_RIME,
            # self.TRAD_1_CONVIVIO,
            # self.TRAD_2_CONVIVIO
        ]
        for opera in opere:
            print(opera['URL'])
            yield scrapy.Request(url=opera['URL'], callback=self.parse, cb_kwargs=dict(opera=opera))

    def parse(self, response, opera, **kwargs):
        page = opera['NAME']
        path = opera['PATH']
        tag = opera['TAG']
        filename = path + f'{page}.txt'

        with open(filename, 'w') as f:
            for resp in response.css(tag + "::text").getall():
                f.write(resp)

        self.log(f'Saved file {filename}')
