import scrapy


class BondSpider(scrapy.Spider):
    name = "bond"
    start_urls = [
        "https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=shortterm&yield=&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19",
        "https://markets.businessinsider.com/bonds/finder?borrower=71&maturity=midterm&yield=&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19",
        "https://markets.businessinsider.com/bonds/finder?p=2&borrower=71&maturity=shortterm&yield=&bondtype=2%2c3%2c4%2c16&coupon=&currency=184&rating=&country=19"
    ]

    def parse(self, response):
        urls = response.css("td.table__td a::attr(href)").getall()
        for url in urls:
            yield response.follow(
                "https://markets.businessinsider.com" + url,
                callback=self.parse2
            )

    def parse2(self, response):
        bond_data = response.css("td.table__td::text").getall()
        yield {
            "price": response.css("span.price-section__current-value::text").get(),
            # "coupon": bond_data[20].strip(),
            "ISIN": bond_data[1].strip(),
            # "issue date": bond_data[17].strip(),
            # "maturity date": bond_data[30].strip()
        }
