# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes_proxy_rotation_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # Retrieve all quote sections in the 'quotes' variable
        quotes = response.xpath('//*[@class="quote"]')

        # Loop through each quote and extract data
        for quote in quotes:
            comment = quote.xpath('.//*[@class="text"]/text()').get()
            tags = quote.xpath('.//*[@class="keywords"]/@content').getall()
            author = quote.xpath('.//*[@class="author"]/text()').get()
            author_link = quote.xpath('.//a/@href').get()

            # Visit the author page and call the parse_author_contents method to scrape author information
            yield scrapy.Request(
                response.urljoin(author_link), 
                callback=self.parse_author_contents,
                meta={'Comment': comment, 'Tags': tags, 'Author': author}
            )

        # Retrieve the next page URL and continue scraping until all pages are visited
        next_page_url = response.xpath('//*[@class="next"]/a/@href').get()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url, callback=self.parse)

    def parse_author_contents(self, response):
        # Extract author details
        comment = response.meta['Comment']
        tags = response.meta['Tags']
        author = response.meta['Author']
        author_born_date = response.xpath('//*[@class="author-born-date"]/text()').get()
        author_born_location = response.xpath('//*[@class="author-born-location"]/text()').get()
        author_description = response.xpath('//*[@class="author-description"]/text()').get()

        # Yield the collected information
        yield {
            'Comment': comment,
            'Tags': tags,
            'Author': author,
            'Author Born Date': author_born_date,
            'Author Born Location': author_born_location,
            'Author Description': author_description
        }
