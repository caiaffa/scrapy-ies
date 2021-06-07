import scrapy

from ies.items.quero_item import QueroItem


class QueroSpider(scrapy.Spider):
    name = 'quero'
    allowed_domains = ['quero.com']
    start_urls = ['https://www.quero.com/faculdades/']

    def parse(self, response):
        for links in response.css('#lista-faculdades li'):
            link = links.css('a ::attr(href)').extract_first()
            yield response.follow(link, self.parse_info)

    def parse_info(self, response):
        school_detail = response.css('.info-faculdade .col-md-3')

        name = response.css('div.title-principal h1::text').extract_first()
        site = school_detail[0].css('span.d-block::text').extract_first()
        telephone = school_detail[1].css('span.d-block::text').extract_first()
        student_numbers = school_detail[3].css('span.d-block p span strong::text').extract_first()
        teacher_numbers = school_detail[4].css('span strong::text').extract_first()
        unit_numbers = school_detail[5].css('span p strong::text').extract_first()

        print(name)

        quero_item = QueroItem(
            name=name,
            site=site,
            telephone=telephone,
            student_numbers=student_numbers,
            teacher_numbers=teacher_numbers,
            unit_numbers=unit_numbers
        )

        yield quero_item
