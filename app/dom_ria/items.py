import scrapy


class ApartmentItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price_uah = scrapy.Field()
    price_usd = scrapy.Field()
    verified_price = scrapy.Field()
    verified_apartment = scrapy.Field()
    description = scrapy.Field()
    region = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    street = scrapy.Field()
    building_number = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    total_square = scrapy.Field()
    living_square = scrapy.Field()
    kitchen_square = scrapy.Field()
    room_count = scrapy.Field()
    floor = scrapy.Field()
    floor_count = scrapy.Field()
    walls_material = scrapy.Field()
    heating = scrapy.Field()
    construction_year = scrapy.Field()
    apartment_type = scrapy.Field()
    selling_type = scrapy.Field()
    creation_date = scrapy.Field()
    apartment_condition = scrapy.Field()
    centre_distance = scrapy.Field()
    centre_distance_type = scrapy.Field()
    images = scrapy.Field()
