# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from fangxun.model import session, ProjectBasic,SaleStatusQuo

class FangxunPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    '''
    中文在控制台显示的为\u77e5\u540d，保持到json文件也是这样
    这个pipe可以帮忙解决这个问题
	'''
    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class DBPipeline(object):
    '''
    中文在控制台显示的为\u77e5\u540d，保持到json文件也是这样
    这个pipe可以帮忙解决这个问题
    '''
    def open_spider(self, spider):
        self.session = session

    def process_item(self, item, spider):
        if 'ProjectBasicItem' == type(item).__name__ :
            pb = ProjectBasic(
                            project_id = item['project_id'],
                            project_name = item['project_name'],
                            project_temp_name = item['project_temp_name'],
                            licence_id = item['licence_id'],
                            approving_authority = item['approving_authority'],
                            developer = item['developer'],
                            developer_id = item['developer_id'],
                            partner  = item['partner'],
                            location = item['location'],
                            district = item['district'],
                            zone = item['zone'],
                            total_building_area = item['total_building_area'],
                            approval = item['approval'],
                            planning_id = item['planning_id'],
                            land_id = item['land_id'],
                            builder_licence = item['builder_licence'],
                            land_licence = item['land_licence'],
                            total_land = item['total_land'],
                            current_used_land = item['current_used_land'],
                            #start_date = item['start_date'],
                            #planning_end_date = item['planning_end_date'],
                            invest = item['invest'],
                            presell_total_area = item['presell_total_area'],
                            public_area = item['public_area'],
                            total_units = item['total_units'],
                            plot_rate = item['plot_rate'],
                            green_rate = item['green_rate'],
                            sale_agent = item['sale_agent'],
                            phone_number = item['phone_number'],
                            sale_location = item['sale_location'],
                            sale_phone_number = item['sale_phone_number'],
                            property_management_company = item['property_management_company'],
                            property_fee_from = item['property_fee_from'],
                            property_fee_to = item['property_fee_to'])
            self.session.add(pb)
            self.session.commit()
        elif 'SaleStatusQuoItem'  == type(item).__name__ :
            ss = SaleStatusQuo(
                    project_id = item['project_id'],
                    purpose = item['purpose'],
                    total_units = item['total_units'],
                    total_area = item['total_area'],
                    sold_units = item['sold_units'],
                    sold_area = item['sold_area'],
                    current_units = item['current_units'],
                    current_area = item['current_area'],
                    restricted_units = item['restricted_units'])
            self.session.add(ss)
            self.session.commit()
    def close_spider(self,spider):
        print 'close------------------------------------'
        self.session.close()