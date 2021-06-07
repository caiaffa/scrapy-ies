# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QueroItem(scrapy.Item):
    name = scrapy.Field()
    site = scrapy.Field()
    telephone = scrapy.Field()
    student_numbers = scrapy.Field()
    teacher_numbers = scrapy.Field()
    unit_numbers = scrapy.Field()