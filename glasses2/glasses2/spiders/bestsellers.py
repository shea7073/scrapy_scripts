import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for pair in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']"):
            yield {
                'product_url': pair.xpath(".//div[@class='product-img-outer']/a[1]/@href").get(),
                'product_image_link': pair.xpath(".//div[@class='product-img-outer']/a[1]/img[1]/@data-src").get(),
                'product_name': pair.xpath(".//div[@class='p-title-block']/div[2]/div/div/div/a[1]/@title").get(),
                'product_price': pair.xpath(".//div[@class='p-title-block']/div[2]/div/div[2]/div[@class='p-price']/div[1]/span/text()").get()
            }
        next_page = response.xpath("//ul[@class='pagination']/li[@class='page-item active']//following-sibling::li/a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)


