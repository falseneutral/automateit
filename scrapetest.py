from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
plans = tree.xpath('//h2[@class="alt-h3"]/text()')
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("Plans: ", plans, "\nPricing:", pricing)