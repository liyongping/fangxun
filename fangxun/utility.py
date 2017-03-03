# --*-- coding: utf-8 -*-
import urlparse

def strip_null(input):
	'''
	replace '无' with ""
	'''
	tmp = input.strip()
	if tmp == u'无':
		tmp = ""
	return tmp

def format_property_fee(fee):
	'''
	From:
	    u"1.7\r\n          ～\r\n          2.5\r\n          元/平方米/月"
	to:
		u"1.7-2.5"
	'''
	tmp = strip_null(fee).split()
	if len(tmp) == 4:
		return tmp[0] + "-" + tmp[2]
	return tmp[0]

def url_parse_parameter(url_str):
	'''
	return parameter dict 
	'''
	try:
		url = urlparse.urlparse(url_str)
		return urlparse.parse_qs(url.query)
	except Exception, e:
		return {}

if __name__ == '__main__':
	print format_property_fee(u"1.7\r\n          ～\r\n          2.5\r\n          元/平方米/月")
	print url_parse_parameter("http://www.wxhouse.com:9098/buildpub/ifrm_BuildStat.pub?blid=102704&plid=102704")
