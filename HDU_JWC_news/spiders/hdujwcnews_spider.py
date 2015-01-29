# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

class HDUJWCNewsSpider(Spider):
	"""docstring for HDUJWCNewsSpider"""

	name = "HDUJWCNews"

	download_delay = 1
	allowed_domains = ["jwc.hdu.edu.cn"]
	start_urls = [
		"http://jwc.hdu.edu.cn/"
	]

	def parse(self,response):
		sel = Selector(response)

		news = sel.xpath("//table[@width='100%']//td[@align='left']/a")


		for new in news:

			for c in new.xpath("@title").extract():
				print c

			for u in new.xpath("@href").extract():
				print "http://jwc.hdu.edu.cn/" + u

			print '===================================================================='
		
			# yield item
