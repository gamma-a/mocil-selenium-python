from selenium.webdriver.common.by import By


class HomepageSimulation:
    def __init__(self, driver):
        self.driver = driver

    ###########################################################################################################
    # LOCATOR
    ###########################################################################################################

    locator_merk_dropdown = (By.XPATH, "//span[@id='select2-brand-mrp-nds-container']")
    locator_dropdown_search = (By.XPATH, "//input[@class='select2-search__field']")
    locator_daihatsu = (By.XPATH, "//li[contains(@id,'Daihatsu')]")
    locator_model_dropdown = (By.XPATH, "//span[@id='select2-model-mrp-nds-container']")
    locator_xenia = (By.XPATH, "//li[contains(@id,'Xenia')]")
    locator_tipe_dropdown = (By.XPATH, "//span[@id='select2-variant-mrp-nds-container']")
    locator_10L_Li = (By.XPATH, "//li[contains(@id,'1.0L Li')]")
    locator_transmisi_dropdown = (By.XPATH, "//span[contains(@id, 'transmission')]")
    locator_manual = (By.XPATH, "//li[contains(@id,'Manual')]")

    ###########################################################################################################
    # WEB ELEMENT
    ###########################################################################################################

    def merk_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_merk_dropdown)

    def dropdown_search(self):
        return self.driver.find_element(*HomepageSimulation.locator_dropdown_search)

    def merk_daihatsu(self):
        return self.driver.find_element(*HomepageSimulation.locator_daihatsu)

    def model_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_model_dropdown)

    def model_xenia(self):
        return self.driver.find_element(*HomepageSimulation.locator_xenia)

    def tipe_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_tipe_dropdown)

    def tipe_10L_Li(self):
        return self.driver.find_element(*HomepageSimulation.locator_10L_Li)

    def transmisi_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_transmisi_dropdown)

    def transmisi_manual(self):
        return self.driver.find_element(*HomepageSimulation.locator_manual)

