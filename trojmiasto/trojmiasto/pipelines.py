# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .validators.trojmiasto_validator import validate_address, validate_city, validate_text_fields, validate_postcode, validate_categories

class TrojmiastoPipeline:
    def process_item(self, item, spider):
        return item


class ValidationPipeline:
    def process_item(self, item, spider):
        try:
            item['name'] = validate_text_fields(item['name'])
            item['address']['city'] = validate_city(item['address']['city'])
            item['address']['postcode'] = validate_postcode(item['address']['postcode'])
            item['address']['street'] = validate_address(item['address']['street'])
            item['categories'] = validate_categories(item['categories'])
        except ValueError as e:
            print(f"Validation error: {e}")
            print(item['url'])
            raise DropItem(f"Validation error: {e}")
        return item