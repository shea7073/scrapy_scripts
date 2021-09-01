import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_7000_7&filter=topsellers&infinite=0']
    counter = 0

    def parse(self, response):
        for game in response.xpath("//div[@id='search_resultsRows']/a"):
            yield {
                'title': game.xpath(".//div[@class='responsive_search_name_combined']/div[1]/span/text()").get(),
                'current_price': game.xpath(".//div[@class='col search_price_discount_combined responsive_secondrow']/@data-price-final").get(),
                'discount': game.xpath(".//div[@class='col search_discount responsive_secondrow']/span/text()").get(),
                'original_price': game.xpath(".//div[@class='responsive_search_name_combined']/div[4]/div[2]/span/strike/text()").get()
            }
        self.counter += 50
        if self.counter <= 300:
             yield scrapy.Request(url=f'https://store.steampowered.com/search/results/?query&start={self.counter}&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_7000_7&filter=topsellers&infinite=0', callback=self.parse)
