import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating/']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'

    def start_requests(self):


    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get().replace('\xa0', ' ').strip(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration': response.xpath("(//time)[1]/text()").get().strip(' \n\t'),
            'genre': response.xpath("//div[@class='subtext']/a[1]/span/text()").get(),
            'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'movie_url': response.url
        }


# normalize-space() could replace duration issues
