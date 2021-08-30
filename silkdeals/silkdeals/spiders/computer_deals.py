import scrapy
from scrapy_selenium import SeleniumRequest


class ComputerDealsSpider(scrapy.Spider):
    name = 'computer_deals'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/computer-deals/',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals']/li")
        for product in products:
            yield {
                'name': product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'link': product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/@href").get(),
                'store_name': product.xpath(".//button[@class='itemStore bp-p-storeLink bp-c-linkableButton  bp-c-button js-button bp-c-button--link']/text()").get(),
                'price': product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get()
            }

        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            absolute_url = f'https://slickdeals.net{next_page}'
            print(absolute_url)
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse

            )

