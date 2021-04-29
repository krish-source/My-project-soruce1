from selenium import webdriver

                                  # all broswer exposes an exe file, use driver to invoke browser



driver = webdriver.Chrome(r"C:\\chromedriver.exe")
driver.maximize_window()

driver.get("http://kdp.amazon.com")


print(driver.title)
print(driver.current_url)

driver.get("https://kdp.amazon.com/en_US/help/topic/G200673300")
driver.minimize_window()
driver.back()
driver.refresh()


driver.close()
