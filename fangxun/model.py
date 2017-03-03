# --*-- coding: utf-8 -*-

from sqlalchemy import Column, Integer, SmallInteger, String, Date, Time,\
    Text, DateTime, create_engine, func, Table, NUMERIC
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class ProjectBasic(Base):
#    '''楼盘概况'''
    __tablename__ = 'ProjectBasic'
    
    #id = Column(Integer(11), primary_key=True, autoincrement=True)
    '''楼盘概况'''
    project_id = Column(String(64), primary_key=True, default='')

    #项目现定名
    project_name = Column(String(128), default='')
    #项目暂定名
    project_temp_name = Column(String(128), default='')
    #预(销)售许可证号
    licence_id = Column(String(128), default='')
    #预(销)售批准机关
    approving_authority = Column(String(128), default='')
    #开 发 商
    developer = Column(String(128), default='')
    #开发商ID
    developer_id = Column(String(64), default='')
    #合 作 方
    partner  = Column(String(128), default='')
    #坐　　落
    location = Column(String(256), default='')
    #行 政 区
    district = Column(String(64), default='')
    #区　　位
    zone = Column(String(128), default='')
    #总建筑面积
    total_building_area = Column(NUMERIC, default=0.0)
    #立项批文
    approval = Column(String(128), default='')
    #规划许可证号
    planning_id = Column(String(128), default='')
    #土地证号
    land_id = Column(String(128), default='')
    #施工许可证号
    builder_licence = Column(String(128), default='')
    #用地许可证号
    land_licence = Column(String(128), default='')
    #总 用 地
    total_land = Column(NUMERIC, default=0.0)
    #当期用地
    current_used_land = Column(NUMERIC, default=0.0)
    #开工日期
    start_date = Column(DateTime)
    #预计竣工日期
    planning_end_date = Column(DateTime)
    #项目投资
    invest = Column(NUMERIC, default=0.0)
    #预售总面积
    presell_total_area = Column(NUMERIC, default=0.0)
    #公建配套面积
    public_area = Column(NUMERIC, default=0.0)
    #总 套 数
    total_units = Column(Integer, default=0)
    #容 积 率
    plot_rate = Column(NUMERIC, default=0.0)
    #绿 化 率
    green_rate = Column(NUMERIC, default=0.0)
    #代销公司
    sale_agent = Column(String(128), default='')
    #电　　话
    phone_number = Column(String(128), default='')
    #项目销售地点
    sale_location = Column(String(256), default='')
    #销售电话
    sale_phone_number = Column(String(64), default='')
    #物业公司
    property_management_company = Column(String(128), default='')
    #物 管 费
    property_fee_from = Column(NUMERIC, default='')
    property_fee_to = Column(NUMERIC, default='')

class SaleStatusQuo(Base):
    '''销售现状'''
    __tablename__ = 'SaleStatusQuo'

    project_id = Column(String(64), primary_key=True, default='')
    # 用途
    purpose = Column(String(128), primary_key=True, default='')
    # 总套数
    total_units = Column(Integer, default=0)
    # 销售总面积
    total_area = Column(NUMERIC, default=0.0)
    # 已售数
    sold_units = Column(Integer, default=0)
    # 已售面积
    sold_area = Column(NUMERIC, default=0.0)
    # 可售数
    current_units = Column(Integer, default=0)
    # 可售面积
    current_area = Column(NUMERIC, default=0.0)
    # 限售数
    restricted_units = Column(Integer, default=0)

    date = Column(DateTime, default=func.now(), nullable=False)


#engine = create_engine(DB_CONNECT_STRING, encoding=DB_ENCODING, echo=DB_ECHO)
engine=create_engine('sqlite:///data.db',echo=True)
session = scoped_session(sessionmaker(bind=engine))

if __name__ == '__main__':
    
    
    # delete all tables
    Base.metadata.drop_all(engine)
    #create all tables
    Base.metadata.create_all(engine)
    #db = scoped_session(sessionmaker(bind=engine))
