import logging

from lxml import etree
import re

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

def save_products(html):
    
    data = []

    try:        
        # Convert BeautifulSoup object to string before parsing
        html_str = str(html)
        page = etree.HTML(html_str)
        logging.info("Successfully parsed to html")
        
        dom = page.xpath("//div[@data-testid='divProduct']/div")
        logging.info(f"Found {len(dom)} products")
        
        for product in dom:
            item = {}
            img = product.xpath(".//img")[0]
            img_src = img.get("src")
            item['image'] = img_src
            item['name'] = product.xpath(".//div[@data-testid='lblHomeProductNameRecom']")[0].text
            price = product.xpath(".//div[@data-testid='lblHomeProductPriceRecom']")[0].text
            filtered_price = int(re.sub(r'[Rp\.]', '', price))
            item['price'] = filtered_price
            url = product.xpath(".//div[@class='css-19oqosi']/a")[0].get("href")
            if not url.startswith('https://ta.tokopedia.com/'):
                url = 'https://tokopedia.com' + url
            item['url'] = url
            data.append(item)
            # print(f"Image source: {img_src}")
            
        logging.info(f"Successfully extracted {len(data)} product details")
        return data
    except Exception as e:
        logging.error(f"Error parsing HTML: {e}")
