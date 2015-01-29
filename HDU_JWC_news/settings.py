# -*- coding: utf-8 -*-

# Scrapy settings for HDU_JWC_news project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'HDU_JWC_news'

SPIDER_MODULES = ['HDU_JWC_news.spiders']
NEWSPIDER_MODULE = 'HDU_JWC_news.spiders'

ITEM_PIPELINES = {
	'HDU_JWC_news.pipelines.HduJwcNewsPipeline'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'HDU_JWC_news (+http://www.yourdomain.com)'
