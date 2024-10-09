from selenium.webdriver.common.by import By


class HomepageSimulation:
    def __init__(self, driver):
        self.driver = driver

    ###########################################################################################################
    # LOCATOR
    ###########################################################################################################

    # Simulation Form
    locator_simulasi_popup = (By.XPATH, "//h5[contains(text(),'Cari Tahu Seberapa Murah Nyicil di Mocil!')]")
    locator_merk_dropdown = (By.XPATH, "//span[@id='select2-brand-mrp-nds-container']")
    locator_merk_dropdown2 = (By.XPATH, "//span[@title='Daihatsu']")
    locator_dropdown_search = (By.XPATH, "//input[@class='select2-search__field']")
    locator_daihatsu = (By.XPATH, "//li[contains(@id,'Daihatsu')]")
    locator_model_dropdown = (By.XPATH, "//span[@id='select2-model-mrp-nds-container']")
    locator_model_dropdown2 = (By.XPATH, "//span[@title='Xenia']")
    locator_xenia = (By.XPATH, "//li[contains(@id,'Xenia')]")
    locator_tipe_dropdown = (By.XPATH, "//span[@id='select2-variant-mrp-nds-container']")
    locator_tipe_dropdown2 = (By.XPATH, "//span[@title='1.0L Li']")
    locator_10L_Li = (By.XPATH, "//li[contains(@id,'1.0L Li')]")
    locator_transmisi_dropdown = (By.XPATH, "//span[contains(@id, 'transmission')]")
    locator_manual = (By.XPATH, "//li[contains(@id,'Manual')]")
    locator_tahun_dropdown = (By.XPATH, "//span[@id='select2-year-mrp-nds-container']")
    locator_tahun_2010 = (By.XPATH, "//li[contains(@data-select2-id,'2010')]")
    locator_warna_dropdown = (By.XPATH, "//span[@id='select2-color-mrp-nds-container']")
    locator_warna_hitam = (By.XPATH, "//li[contains(@data-select2-id,'Hitam')]")
    locator_kilometer = (By.XPATH, "//input[@name='mileage']")
    locator_provinsi_dropdown = (By.XPATH, "//span[@id='select2-province-name-mrp-nds-container']")
    locator_jakarta_dki = (By.XPATH, "//li[contains(@data-select2-id,'Jakarta D.K.I.')]")
    locator_kota_dropdown = (By.XPATH, "//span[@id='select2-city-name-mrp-nds-container']")
    locator_kota_jakarta_pusat = (By.XPATH, "//li[contains(@data-select2-id,'Jakarta Pusat')]")
    locator_button_hitung_simulasi = (By.XPATH, "//button[@id='home_simulasi_a']")

    # Result Page
    locator_simulasi_pembiayaan_title = (By.XPATH, "//h1[contains(text(),'Simulasi Pembiayaan')]")
    locator_actual_merk = (By.XPATH, "//h3[contains(text(),'Daihatsu')]")
    locator_actual_model_tipe = (By.XPATH, "//h2[contains(text(),'Xenia 1.0L Li')]")
    locator_alert_tahun = (By.XPATH, "//select[@id='year-mrp-nds']")

    ###########################################################################################################
    # WEB ELEMENT
    ###########################################################################################################

    # Simulation Form
    def simulasi_popup(self):
        return self.driver.find_element(*HomepageSimulation.locator_simulasi_popup)

    def merk_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_merk_dropdown)

    def merk_dropdown2(self):
        return self.driver.find_element(*HomepageSimulation.locator_merk_dropdown2)

    def dropdown_search(self):
        return self.driver.find_element(*HomepageSimulation.locator_dropdown_search)

    def merk_daihatsu(self):
        return self.driver.find_element(*HomepageSimulation.locator_daihatsu)

    def model_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_model_dropdown)

    def model_dropdown2(self):
        return self.driver.find_element(*HomepageSimulation.locator_model_dropdown2)

    def model_xenia(self):
        return self.driver.find_element(*HomepageSimulation.locator_xenia)

    def tipe_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_tipe_dropdown)

    def tipe_dropdown2(self):
        return self.driver.find_element(*HomepageSimulation.locator_tipe_dropdown2)

    def tipe_10L_Li(self):
        return self.driver.find_element(*HomepageSimulation.locator_10L_Li)

    def transmisi_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_transmisi_dropdown)

    def transmisi_manual(self):
        return self.driver.find_element(*HomepageSimulation.locator_manual)

    def tahun_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_tahun_dropdown)

    def tahun_2010(self):
        return self.driver.find_element(*HomepageSimulation.locator_tahun_2010)

    def warna_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_warna_dropdown)

    def warna_hitam(self):
        return self.driver.find_element(*HomepageSimulation.locator_warna_hitam)

    def input_kilometer(self):
        return self.driver.find_element(*HomepageSimulation.locator_kilometer)

    def provinsi_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_provinsi_dropdown)

    def provinsi_jakarta_dki(self):
        return self.driver.find_element(*HomepageSimulation.locator_jakarta_dki)

    def kota_dropdown(self):
        return self.driver.find_element(*HomepageSimulation.locator_kota_dropdown)

    def kota_jakarta_pusat(self):
        return self.driver.find_element(*HomepageSimulation.locator_kota_jakarta_pusat)

    def button_hitung_simulasi(self):
        return self.driver.find_element(*HomepageSimulation.locator_button_hitung_simulasi)

    # Result Page
    ##########################################
    def title_simulasi_pembiayaan(self):
        return self.driver.find_element(*HomepageSimulation.locator_simulasi_pembiayaan_title)

    def actual_merk(self):
        return self.driver.find_element(*HomepageSimulation.locator_actual_merk)

    def actual_model_tipe(self):
        return self.driver.find_element(*HomepageSimulation.locator_actual_model_tipe)
