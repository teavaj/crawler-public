import polars as pl
import scrapy

domain_lst = (
    pl.read_csv("com_domains.csv")
    .select(pl.col("url_host_registered_domain"))
    .to_series()
).to_list()
# print(domain_lst)

filter_lst = [
    "about us",
    "contact us",
    "contact",
    "privacy policy",
    "privacy",
    "terms and conditions",
    "terms of use",
    "terms of service",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
}

search_criteria = ["google", "adwords"]


class NewCrawlerSpider(scrapy.Spider):
    name = "public-crawl"
    start_urls = domain_lst[:100]
    user_agent = headers["User-Agent"]

    def parse(self, response):
        for line in response.xpath("//a"):
            if line.xpath("text()").get() is None:
                continue
            else:
                txt = line.xpath("text()").get().lower().split(" ")  # remove tags
                link = line.attrib["href"]
            # print(txt.split(' '))
            if any(word in txt for word in filter_lst):
                # yield response.url
                yield response.follow(link, callback=self.parse_agb)
                # break

    def parse_agb(self, response):
        for line in response.xpath("//body//text()").extract():

            text = line.strip().lower()
            if len(text) < len("google"):  # site has partially no text
                continue
            elif any(criteria in text for criteria in search_criteria):
                yield {"googleads": response.url}
                break
