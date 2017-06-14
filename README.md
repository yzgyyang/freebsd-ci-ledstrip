# A Physical FreeBSD Build Status Dashboard

## Intro

What started as a side project during my first few weeks of interning at The FreeBSD Foundation, has become a useful LED display of the current FreeBSD CI (continuous integration) build status, and is running 24/7 in the Foundation Kitchener office, proudly running FreeBSD on a BeagleBone Green.

## Publications

A detailed guide/article is posted at the [FreeBSD Foundation Blog](https://www.freebsdfoundation.org/news-and-events/blog/blog-post/building-a-physical-freebsd-build-status-dashboard/).  
The draft of the article is posted [here](https://github.com/yzgyyang/stuff/blob/master/BeagleBone_FreeBSD_SPI_Setup.md). Pull Requests are very welcome.

## Requirements

- A working installation of FreeBSD
- BeagleBone Green with a 4GB micro-SD card, a serial cable and Internet connection
- An addressable LED RGB strip. This project uses an APA102 LED strip from Sparkfun

## Further reading

My implementation of this project: [yzgyyang/freebsd-ci-ledstrip](https://github.com/yzgyyang/freebsd-ci-ledstrip)

FreeBSD's support for BeagleBone: [FreeBSD/arm/BeagleBoneBlack](https://wiki.freebsd.org/FreeBSD/arm/BeagleBoneBlack)

A guide of building, installing and updating FreeBSD on a BeagleBone:
[Getting Started with FreeBSD on BeagleBone Black](https://www.freebsdfoundation.org/wp-content/uploads/2015/12/vol1_no1_beaglebone_dkr.pdf)

Official BeagleBone Green Document: [BeagleBone Green](http://wiki.seeed.cc/BeagleBone_Green/)

[APA102 Manual](https://cdn-shop.adafruit.com/datasheets/APA102.pdf)

[Understanding the APA102 “Superled”](https://cpldcpu.com/2014/11/30/understanding-the-apa102-superled/)

[FreeBSD GPIO Benchmark](https://www.bidouilliste.com/blog/2016/04/22/FreeBSD-GPIO-Benchmark/)

## Thanks

I would like to thank my supervisor [Ed Maste](https://twitter.com/ed_maste) for his guidance and support on my work. I would also like to thank [Siva Mahadevan](https://github.com/sivamahadevan), my colleague and friend, for the help and useful suggestions.
