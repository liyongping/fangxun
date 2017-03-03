
# --*-- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.selector import Selector
from fangxun.items import ProjectBasicItem,SaleStatusQuoItem
from fangxun.utility import *

class WuxiSpider(CrawlSpider):
    name = "wuxi"
    allowed_domains = ["wxhouse.com"]
    start_urls = [
        "http://www.wxhouse.com:9098/buildpub/"
    ]

    rules = [
        Rule(sle(allow=("/buildpub/\?page=\d{1,}")), 
         follow=True,
         callback='parse_item')
    ]

    # for CrawlSpider, the callback should be named parse_item
    def parse_item(self, response):
        #yield scrapy.Request(r"http://www.wxhouse.com:9098/buildpub/ifrm_BuildStat.pub?blid=100584", 
        #                   callback=self.parse_build_stat_contents2)
        # maybe need to improve the performance here
        for licencebox in response.xpath("//td[@id='licencebox']").extract():
            developerUrl = Selector(text=licencebox).xpath('//@href').extract()
            # + BuildInfo.pub?blid=102699
            url = response.urljoin(developerUrl[0]) 
            yield scrapy.Request(url, callback=self.parse_project_contents)

    def parse_project_contents(self, response):
        info_url_list = []
        # 楼盘详情
        for sel in response.xpath("//span[@onclick]"):
            # fetch the value in onclick
            onclick = sel.xpath("@onclick").extract()[0]
            value_list = onclick.split("'")
            if len(value_list) == 3:
                info_url_list.append(value_list[1])
            else:
                # couldn't find correct object, log it, need to check further
                pass
        '''
        [u'ifrm_BuildBasic.pub?blid=102711', 
        u'ifrm_HouseList.pub?blid=102711', 
        u'ifrm_BuildProfile.pub?blid=102711', 
        u'ifrm_BuildStat.pub?blid=102711']
        ''' 
        if len(info_url_list) == 4:
            if info_url_list[0].find("ifrm_BuildBasic") == 0:
                url = response.urljoin(info_url_list[0]) 
                yield scrapy.Request(url, callback=self.parse_build_basic_contents)
            '''
            if info_url_list[1].find("ifrm_HouseList") == 0:
                url = response.urljoin(info_url_list[1]) 
                yield scrapy.Request(url, callback=self.parse_house_list_contents)
            if info_url_list[2].find("ifrm_BuildProfile") == 0:
                url = response.urljoin(info_url_list[2]) 
                yield scrapy.Request(url, callback=self.parse_build_profile_contents)
            '''
            if info_url_list[3].find("ifrm_BuildStat") == 0:
                url = response.urljoin(info_url_list[3]) 
                yield scrapy.Request(url, callback=self.parse_build_stat_contents2)

    def parse_build_basic_contents(self, response):
        '''楼盘概况 ifrm_BuildBasic.pub?blid=102699'''
        content_list = response.xpath("//table[@id='info']")
        if len(content_list) == 1:
            table_content = content_list[0].extract()
            #key = [k.extract() for k in Selector(text=table_content).xpath("//td[@align='right']/text()")]
            #value = [v.extract() for v in Selector(text=table_content).xpath("//td[@align='left']")]
            value = Selector(text=table_content).xpath("//td[@align='left']//text()")
            #kv = dict(zip(key,value))
            

            item = ProjectBasicItem()
            # get 102699 from ifrm_BuildBasic.pub?blid=102699
            project_id = response.url.split("=")[1]
            # get ProvInfo.pub?prid=100498
            provinfo_href = Selector(text=table_content).xpath("//td[@align='left']/a[@href]//@href").extract()[0]
            developer_id = provinfo_href.split("=")[1]
            item['project_id'] = project_id
            item['developer_id'] = developer_id
            item['project_name'] = value[0].extract() #kv[u'项目现定名：']
            item['project_temp_name'] = value[1].extract() #kv[u'项目暂定名：']
            item['licence_id'] = value[2].extract()# kv[u'预(销)售许可证号：']
            item['approving_authority'] = value[3].extract() #kv[u'预(销)售批准机关：']
            item['developer'] = value[4].extract().strip() #kv[u'开 发 商：']
            item['partner'] = strip_null(value[5].extract()) #kv[u'合 作 方：']
            item['location'] = value[6].extract() #kv[u'坐　　落：']
            item['district'] = value[7].extract() #kv[u'行 政 区：']
            item['zone'] = value[8].extract() #kv[u'区　　位：']
            item['total_building_area'] = float(value[9].extract().split()[0]) #kv[u'总建筑面积：']
            item['approval'] = value[10].extract() #kv[u'立项批文：']
            item['planning_id'] = value[11].extract() #kv[u'规划许可证号：']
            item['land_id'] = value[12].extract() #kv[u'土地证号：']
            item['builder_licence'] = value[13].extract() #kv[u'施工许可证号；']
            item['land_licence'] = value[14].extract() #kv[u'用地许可证号：']
            item['total_land'] = float(value[15].extract().split()[0]) #kv[u'总 用 地：']
            item['current_used_land'] = float(value[16].extract().split()[0]) #kv[u'当期用地：']
            item['start_date'] = value[17].extract() #kv[u'开工日期：']
            item['planning_end_date'] = value[18].extract() #kv[u'预计竣工日期：']
            item['invest'] = float(value[19].extract().split()[0]) #kv[u'项目投资：']
            item['presell_total_area'] = float(value[20].extract().split()[0]) #kv[u'预售总面积：']

            #kv[u'公建配套面积：']
            public_area = value[21].extract().split()[0]
            item['public_area'] = float(public_area)
            item['total_units'] = int(value[22].extract()) #kv[u'总 套 数：']
            item['plot_rate'] = float(value[23].extract()) #kv[u'容 积 率：']
            item['green_rate'] = float(strip_null(value[24].extract()).split()[0]) #kv[u'绿 化 率：']
            item['sale_agent'] = strip_null(value[25].extract()) #kv[u'代销公司：']
            item['phone_number'] = strip_null(value[26].extract()) #kv[u'电　　话： ']
            item['sale_location'] = strip_null(value[27].extract()) #kv[u'项目销售地点：']
            item['sale_phone_number'] = strip_null(value[28].extract()) #kv[u'销售电话：']
            item['property_management_company'] = strip_null(value[29].extract()) #kv[u'物业公司：']

            fee_str = format_property_fee(value[30].extract())
            fee = fee_str.split("-")
            item['property_fee_from'] = float(fee[0]) #kv[u'物 管 费：']
            item['property_fee_to'] = float(fee[1])

            yield item

    def parse_house_list_contents(self, response):
        pass

    def parse_build_profile_contents(self, response):
        pass

    def parse_build_stat_contents(self, response):
        '''销售现状'''
        content_list = [c.extract() for c in response.xpath("//td[@id='table_content']/table/tr/td/text()")]

        item = SaleStatusQuoItem()
        project_id = ""
        param = url_parse_parameter(response.url)
        project_id = param['blid'][0]
        item['project_id'] = project_id
        item['purpose'] = content_list[7]
        item['total_units'] = int(content_list[8])
        item['total_area'] = float(content_list[9].split()[0])
        item['sold_units'] = int(content_list[10])
        item['sold_area'] = float(content_list[11].split()[0])
        item['current_units'] = int(content_list[12])
        item['current_area'] = float(content_list[13].split()[0])
        #item['date'] = content_list[0]
        yield item

    def parse_build_stat_contents2(self, response):
        '''销售现状'''
        data_list = response.xpath("//td[@id='table_content']/table/tr")
        if len(data_list) > 1:
            for i in range(1,len(data_list)):
                content_list = [d.extract() for d in data_list[i].xpath("td/text()")]
                item = SaleStatusQuoItem()
                project_id = ""
                param = url_parse_parameter(response.url)
                project_id = param['blid'][0]
                item['project_id'] = project_id
                item['purpose'] = content_list[0]

                total_units = int(content_list[1])
                item['total_units'] = total_units

                item['total_area'] = float(content_list[2].split()[0])

                sold_units = int(content_list[3])
                item['sold_units'] = sold_units
                item['sold_area'] = float(content_list[4].split()[0])

                current_units = int(content_list[5])
                item['current_units'] = current_units
                item['current_area'] = float(content_list[6].split()[0])

                restricted_units = total_units - sold_units - current_units
                item['restricted_units'] = restricted_units
                #item['date'] = content_list[0]
                yield item