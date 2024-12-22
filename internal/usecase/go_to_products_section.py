import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from internal.usecase.scroll_to_bottom import scroll_to_bottom
import time


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

def go_to_products_section(driver, id):
    try:
        logging.info("Go to products section...")
        current_position = {"value": 0}
        
        while True:
            scroll_to_bottom(driver=driver, position=current_position)
            
            try:
                button = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@data-testid='btnHomeRecomLoadMore']"))
                )
                
                if not button.is_displayed():
                    break
                    
                button.click()
                time.sleep(2)
                
            except Exception:
                break
                
        logging.info("Success Retrieving All Products")
        
        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, id))
            )
            html_content = element.get_attribute('innerHTML')
            soup = BeautifulSoup(html_content, 'html.parser')
            logging.info("Found and parsed element content with BeautifulSoup")
            logging.info("Successfully found and processed element")
            return soup
            
        except Exception as e:
            logging.error(f"Error finding element: {e}")
            return None
            
    except Exception as e:
        logging.error(f"Error in products section: {e}")
        return None

