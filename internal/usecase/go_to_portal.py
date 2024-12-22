from internal.config.config import url_portal
import logging


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


def go_to_portal(driver):
    logging.info("Go to portal...")
    driver.get(url_portal)
    return driver
