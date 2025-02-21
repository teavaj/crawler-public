# crawler-public

# Project description

lorem ipsum

# Gathering data

# Crawling and scpraing websites

1. Set-up a new spider
   1. in terminal run
      ```bash
      scrapy startproject crawler_public
      ```
2. These changes to setting.py are recommended for a better performance
   1. USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
   2. CONCURRENT_REQUESTS = 60
   3. DOWNLOAD_DELAY = 0
   4. SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
   5. LOG_LEVEL = 'INFO'
3. Copy com_domains.csv into the newly created crawler_public directory
4. cd crawler_public
5. scrapy crawl public-crawl
