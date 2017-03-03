# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangxunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DeveloperItem(scrapy.Item):
    '''开发商信息'''
    pass

class ProjectBasicItem(scrapy.Item):
    '''楼盘概况'''
    project_id = scrapy.Field()
    #开发商ID
    developer_id = scrapy.Field()

    #项目现定名
    project_name = scrapy.Field()
    #项目暂定名
    project_temp_name = scrapy.Field()
    #预(销)售许可证号
    licence_id = scrapy.Field()
    #预(销)售批准机关
    approving_authority = scrapy.Field()
    #开 发 商
    developer = scrapy.Field()
    #合 作 方
    partner  = scrapy.Field()
    #坐　　落
    location = scrapy.Field()
    #行 政 区
    district = scrapy.Field()
    #区　　位
    zone = scrapy.Field()
    #总建筑面积
    total_building_area = scrapy.Field()
    #立项批文
    approval = scrapy.Field()
    #规划许可证号
    planning_id = scrapy.Field()
    #土地证号
    land_id = scrapy.Field()
    #施工许可证号
    builder_licence = scrapy.Field()
    #用地许可证号
    land_licence = scrapy.Field()
    #总 用 地
    total_land = scrapy.Field()
    #当期用地
    current_used_land = scrapy.Field()
    #开工日期
    start_date = scrapy.Field()
    #预计竣工日期
    planning_end_date = scrapy.Field()
    #项目投资
    invest = scrapy.Field()
    #预售总面积
    presell_total_area = scrapy.Field()
    #公建配套面积
    public_area = scrapy.Field()
    #总 套 数
    total_units = scrapy.Field()
    #容 积 率
    plot_rate = scrapy.Field()
    #绿 化 率
    green_rate = scrapy.Field()
    #代销公司
    sale_agent = scrapy.Field()
    #电　　话
    phone_number = scrapy.Field()
    #项目销售地点
    sale_location = scrapy.Field()
    #销售电话
    sale_phone_number = scrapy.Field()
    #物业公司
    property_management_company = scrapy.Field()
    #物 管 费
    property_fee_from = scrapy.Field()
    property_fee_to = scrapy.Field()


class SaleStatusQuoItem(scrapy.Item):
    '''销售现状'''
    project_id = scrapy.Field()
    # 用途
    purpose = scrapy.Field()
    # 总套数
    total_units = scrapy.Field()
    # 销售总面积
    total_area = scrapy.Field()
    # 已售数
    sold_units = scrapy.Field()
    # 已售面积
    sold_area = scrapy.Field()
    # 可售数
    current_units = scrapy.Field()
    # 可售面积
    current_area = scrapy.Field()
    # 限售数
    restricted_units = scrapy.Field()

    date = scrapy.Field()