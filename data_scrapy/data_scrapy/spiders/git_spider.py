from scrapy.item import Item, Field
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class GitSpider(scrapy.Spider):
    name = "git"
    allowed_domains = ["github.com"]
    start_urls = ["https://www.github.com/login"]

    def parse(self, response):
        formdata = {'login': 'username',
                'password': 'password' }
        yield FormRequest.from_response(response,
                                        formdata=formdata,
                                        clickdata={'name': 'commit'},
                                        callback=self.parse1)

    def parse1(self, response):
        open_in_browser(response)