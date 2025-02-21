# Project description

This is a demo of a project I did for a company. The goal was to gather to most links from a specific market and scan through the websites looking for a specific keyword. This project creates such a dataset from the Common Crawl database for further manual tasks.

# Gathering data

Data is fetched from "https://data.commoncrawl.org/" with the requests library. The incoming data goes through a filter process, looking for a specified domain (in this example .com). After additional data cleaning steps the output is a CSV table.

# Crawling and scpraing websites

The spider in the project has 2 main steps:
1. Opens the main domain (the homepage) and looks for internal links like 'privacy policy'
2. If found, it follows the link and parses the text looking for a keyword (e.g. 'google')

Every link, where such a keyword was found will be writen than in a JSON file.
