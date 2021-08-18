import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def start_requests(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers', callback=self.parse, headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73')

    def parse(self, response):
        for pair in response.xpath(''):
            yield {
                'product_url': response.urljoin(pair.xpath('').get()),
                'product_image_link': pair.xpath('').get(),
                'product_name': pair.xpath('').get(),
                'product_price': pair.xpath('').get()
            }
        next_page = pair.xpath('').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73')
