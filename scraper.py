import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_with_selenium(url):
    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument("--headless")

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(3)  # Let JS render

    elements = driver.find_elements(By.XPATH, "//*[not(self::script) and not(self::style)]")
    visible_text = "\n".join([el.text for el in elements if el.text.strip() != ""])

    driver.quit()
    return visible_text[:10000]

if __name__ == "__main__":
    url = input("Paste CVE blog/article URL: ")
    result = scrape_with_selenium(url)
    print("\n--- Paste this into your GPT assistant ---\n")
    print(result)
