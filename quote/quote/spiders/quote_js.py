import scrapy
from scrapy_splash import SplashRequest

class QuoteJsSpider(scrapy.Spider):
    name = 'quote_js'
    allowed_domains = ['quotes.toscrape.com']

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(1))
            splash:set_viewport_full()
            return {
                html = splash:html()
            }
        end
        '''

    def start_requests(self):
        yield SplashRequest(url='https://quotes.toscrape.com/js', callback=self.parse, endpoint='execute', args={
            'lua_source': self.script
        })

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote_body': quote.xpath(".//span[@class='text']/text()").get(),
                'quote_author': quote.xpath(".//span[2]/small/text()").get(),
                'tags': quote.xpath(".//div[@class='tags']/a/text()").getall()
            }
        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page:
            yield SplashRequest(url='https://quotes.toscrape.com' + next_page, callback=self.parse, endpoint='execute', args={
                'lua_source': self.script
        })