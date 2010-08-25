# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FasItem(Item):
    USupplierName = Field()
    USupplierINN = Field()
    USupplierKPP = Field()
    USupplierCountry = Field()
    USupplierPostIndex = Field()
    USupplierRegion = Field()
    USupplierMunicipalForm = Field()
    USupplierSettlement = Field()
    USAdress = Field()
    Organ = Field()
    RNPReason = Field()
    RNPRegNum = Field()
    IncludeDT = Field()
    ExcludeDate = Field()
    RequesterName = Field()
    RequesterINN = Field()
    RequesterKPP = Field()
    RequesterAdress = Field()
    Subj = Field()
    PurchaseResultDT = Field()
    PurchaseResultDoc = Field()
    PurResultDocDT = Field()
    PurResultDocNum = Field()
    Summ = Field()
    Currency = Field()
    ContractDT = Field()
    RegNum = Field()
    CodeOKP = Field()
    ContractPlanDT = Field()
    ContractBreakDT = Field()

