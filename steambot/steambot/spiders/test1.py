import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers/']

    def parse(self, response):
        for game in response.xpath("//div[@id='search_resultsRows']/a"):
            yield {
                'title': game.xpath(".//div[@class='responsive_search_name_combined']/div[1]/span/text()").get(),
                #'price': game.xpath(".//div[contains(@class, 'col') and contains(@class, 'search_price') and contains(@class, 'responsive_secondrow')]/@data-price-final/text()").get()
                'price': game.xpath(".//div[@class='col search_price_discount_combined responsive_secondrow']/@data-price-final").get()

            }


# https://store.steampowered.com/search/results/?query&start=100&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_7000_7&filter=topsellers&infinite=1
