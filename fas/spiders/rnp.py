import re
from scrapy import log

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.http import Request
from fas.items import FasItem
from scrapy.contrib.loader import XPathItemLoader

from scrapy.contrib.loader.processor import TakeFirst
class FasLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

class RnpSpider(BaseSpider):
    domain_name = 'rnp.fas.gov.ru'
    start_urls = ['http://rnp.fas.gov.ru/Default.aspx']

    def parse(self, response):
        response = response.replace(body=response.body.replace("disabled",""))
        xs = HtmlXPathSelector(response)
        requests = []
        ids = xs.select("//input[contains(@name,'btnView')]/@onclick").re('id=[a-z0-9-]+')
        for id in ids:
            requests.append(Request("http://rnp.fas.gov.ru/RNPCard.aspx?%s" % id, callback=self.parse_item))
            
        start_index = xs.select("//span[@id='ctl00_phWorkZone_rnpList_datapgr_lblRecNumTill']/text()").extract()[0]
        end_index = xs.select("//span[@id='ctl00_phWorkZone_rnpList_datapgr_lblRecNumAll']/text()").extract()[0]
        if start_index!=end_index:
            el = xs.select("//input[@id='ctl00_phWorkZone_rnpList_datapgr_tbRecNumFrom']/@value")[0]
            val = int(el.extract())
            newval = val+10
            requests.append(FormRequest.from_response(
                    response,
                    formdata={'ctl00$phWorkZone$rnpList$datapgr$tbRecNumFrom':newval},
                    callback=self.parse
                )
            )
                
        for request in requests:
            yield request
        
    def parse_item(self, response):
        def name(s):
            return "//td[span[@id='ctl00_phWorkZone_lbl%s']]/following-sibling::td/span/text()" % s
            
        hxs = HtmlXPathSelector(response)
        l = FasLoader(FasItem(), hxs)
        for field in FasItem.fields.keys():
            l.add_xpath(field, name(field))
        
        return l.load_item()
        
SPIDER = RnpSpider()
