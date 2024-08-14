import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__=="__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    try:
        driver.implicitly_wait(5)
        driver.get("https://www.linkedin.com/feed")

        user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        user.send_keys("")
        password_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        time.sleep(15)
        # search_elem  = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "search")))
        driver.execute_script("window.open('')")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.linkedin.com/search/results/companies/?keywords=carson%20tahoe&origin=SWITCH_SEARCH_VERTICAL&sid=IGi")
        print(driver.find_element(By.CLASS_NAME,"search-results-container").text)
        a = driver.find_element(By.CLASS_NAME,"search-results-container").find_elements(By.TAG_NAME,"li")
        for divtag in a:

            print("|--------------------------|")
            print(divtag.text)
            print("|------------ clicking --------------|")
            divtag.click()
            break

        time.sleep(15)
        print(f"{     driver.current_url = }")
        new_url = driver.current_url + "/people"
        driver.implicitly_wait(5)
        driver.get(new_url)
        time.sleep(330)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
