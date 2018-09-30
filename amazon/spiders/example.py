# -*- coding: utf-8 -*-

import scrapy

from amazon.items import AmazonItem


class Product(scrapy.Item):
    name = scrapy.Field()


class ExampleSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com', 'scrapy.org']
    start_urls = [
        # 'https://doc.scrapy.org/en/latest/_static/selectors-sample1.html'
        'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=laptop'
        # 'https://www.amazon.com/s/ref=sr_pg_1?rh=i%3Aaps%2Ck%3Alaptop&keywords=laptop&ie=UTF8&qid=1537069715'
        # 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=laptop'
    ]

    def parse(self, response):
        # response.
        # li = response.selector.xpath('//title/text()').extract()
        # products = response.css('li[@id="result_0"]')
        # description = response.css('h2::attr(data-attribute)').extract()
        # products = response.css('h2::attr(data-attribute)').extract()
        products = response.css('li[id^="result"]')

        for prod in products:
            prod_url = prod.css('a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal::attr(href)').extract_first()
            prod_name = prod.css('h2::attr(data-attribute)').extract_first()

            item = AmazonItem()
            item['name'] = prod_name
            item['url'] = response.urljoin(prod_url)
            print(item)
            yield item

            # print(prod_list)

        # response.css('span.pagnRA a::attr(href)')
        next_page = response.css('span.pagnRA a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        print(products)
        # response.css('li[id^="result"]')
        pass
