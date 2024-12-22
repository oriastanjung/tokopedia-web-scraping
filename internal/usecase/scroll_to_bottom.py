import time
from selenium.webdriver.common.by import By

def scroll_to_bottom(driver, position):
    try:
        button = driver.find_element(By.XPATH, "//button[@data-testid='btnHomeRecomLoadMore']")
        button_location = button.location['y']
        scroll_step = 100
        while position["value"] < button_location:
            position["value"] = min(position["value"] + scroll_step, button_location)
            driver.execute_script(f"window.scrollTo(0, {position['value']});")
            time.sleep(0.1)
    except Exception:
        # If button not found, scroll to bottom of page
        total_height = driver.execute_script("return document.body.scrollHeight")
        scroll_step = 150
        while position["value"] < total_height:
            position["value"] = min(position["value"] + scroll_step, total_height)
            driver.execute_script(f"window.scrollTo(0, {position['value']});")
            time.sleep(0.1)
