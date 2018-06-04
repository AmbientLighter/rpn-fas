Please note that this parser is outdated as it doesn't support new design of rnp.fas.gov.ru.
Parsed data available at scraped_items.csv
Parsed at 26.08.2010 (now it's changed)

The program works in scrapy framework (scrapy.org), version 0.8 and 0.9.
In order to run parser, type ./scrapy-ctl.py runspider fas/spiders/rnp.py

------------------------------------------------
This program itself is cross-platform, as it has been tested by developer with following settings:
- Linux Ubuntu 10.04 (Lucid Lynx) + Python 2.6, both Scrapy 0.8 and 0.9, Twisted 10.0.0
- Windows Vista + Python 2.6, both Scrapy 0.8 and 0.9, Twisted 10.1.0

Note that it doesn't claim to work with scrapy 0.10!
------------------------------------------------

Windows users should follow these instructions:

- Install Python 2.6 (http://www.python.org/ftp/python/2.6/python-2.6.msi)
- Install Twisted-10.1.0 (http://pypi.python.org/packages/2.6/T/Twisted/Twisted-10.1.0.winxp32-py2.6.msi#md5=bab4611abfdd63fc92424f4afa1e2865)
- Install zope.interface-3.6.1 either using official EGG distribution (http://pypi.python.org/packages/2.6/z/zope.interface/zope.interface-3.6.1-py2.6-win32.egg#md5=0d09224cea973b75feec65f84660742b) or non-official MSI at http://feisley.com/python/zope.interface-3.5.0.win32-py2.6.exe
- Install libxml2: http://users.skynet.be/sbi/libxml-python/binaries/libxml2-python-2.7.4.win32-py2.6.exe
- Install http://pypi.python.org/packages/any/S/Scrapy/Scrapy-0.9.win32.exe#md5=35c412031e87609a17560d3e50d7edde

Note that MSI are explicitly stated just for convenience.
All the setup takes about 5 minutes.

- Checkout and unzip source code from http://github.com/AmbientLighter/rpn-fas/zipball/master to (for example) the rpn-fas folder.
- Open console at rpn-fas and type C:\Python26\python.exe scrapy-ctl.py runspider fas\spiders\rnp.py

Parsing takes about 40 min, so please be patient.
------------------------------------------------

Author: Victor Mireyev
License: Creative Commons Attribution 3.0 Unported License
