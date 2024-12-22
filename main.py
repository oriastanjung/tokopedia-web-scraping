import time
from internal.usecase.create_driver import create_driver
from internal.usecase.go_to_portal import go_to_portal
from internal.usecase.go_to_products_section import go_to_products_section
from internal.usecase.save_products import save_products
from internal.utils.save_to_json import save_to_json
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


def main():
    
    driver = create_driver()
    go_to_portal(driver)
    page_source = go_to_products_section(driver=driver, id="//div[@data-testid='divHomeRecomContents']")
    time.sleep(3)
    data = save_products(html=page_source)
    save_to_json(data=data, filename="extracted")
    
        
        
main()