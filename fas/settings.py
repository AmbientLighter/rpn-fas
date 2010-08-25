# Scrapy settings for fas project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'fas'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['fas.spiders']
NEWSPIDER_MODULE = 'fas.spiders'
DEFAULT_ITEM_CLASS = 'fas.items.FasItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'scrapy.contrib.pipeline.fileexport.FileExportPipeline'
]
EXPORT_FORMAT = 'csv'
EXPORT_FILE = 'scraped_items.csv'
EXPORT_ENCODING = 'utf8'
EXPORT_FIELDS = ('USupplierName',
 'USupplierINN',
 'USupplierKPP',
 'USupplierCountry',
 'USupplierPostIndex',
 'USupplierRegion',
 'USupplierMunicipalForm',
 'USupplierSettlement',
 'USAdress',
 'Organ',
 'RNPReason',
 'RNPRegNum',
 'IncludeDT',
 'ExcludeDate',
 'RequesterName',
 'RequesterINN',
 'RequesterKPP',
 'RequesterAdress',
 'Subj',
 'PurchaseResultDT',
 'PurchaseResultDoc',
 'PurResultDocDT',
 'PurResultDocNum',
 'Summ',
 'Currency',
 'ContractDT',
 'RegNum',
 'CodeOKP',
 'ContractPlanDT',
 'ContractBreakDT')
