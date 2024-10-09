import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_object.home_page import Homepage
from page_object.homepage_simulation import HomepageSimulation
from utilities.base_class import BaseClass


class TestHomepageSimulation(BaseClass):

    def search_wait(self):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        simulation = HomepageSimulation(self.driver)

        wait2 = WebDriverWait(self.driver, 10)
        wait2.until(expected_conditions.presence_of_element_located(HomepageSimulation.locator_dropdown_search))
        log.info("Search box is found")

    def test_homepage_simulasi_kredit_01(self):
        # Given that User is on the Kategori Menu section on the Homepage when User clicked on Simulasi button then User will see popup modal for Hitung Simulasi
        log = self.getLogger()
        homepage = Homepage(self.driver)
        simulation = HomepageSimulation(self.driver)
        log.info("Start executing Test Case Homepage Simulasi Kredit - 01")

        # Click the Simulasi Menu on the Homepage
        homepage.simulasi_menu().click()
        log.info("Simulation menu is clicked")
        time.sleep(2)

        try:
            simulasi = simulation.simulasi_popup()
            assert simulasi.is_displayed(), "Simulasi Popup is not visible"
            log.info("Simulation Popup is displayed")
        except NoSuchElementException:
            assert False, "Simulasi Popup is not present on the page"

    def test_homepage_simulasi_kredit_02_03(self):
        #  [02] Given that User is on popup Hitung Simulasi when User fill in the fields with valid keyword and click button Hitung Simulasi then User will be redirected to Simulasi Pembiayaan page with details for Hasil Simulasi
        #  [03] Given that User is on popup Hitung Simulasi when User leave all the fields empty and click button Hitung Simulasi then User able to see a notification alert to fill the mandatory field

        # NOTE:
        # For TC-03, the alert is using default HTML5 validation which can't be detected using Selenium
        # This script approach is by detecting whether the particular mandatory field still has an empty value after the form is submitted
        # If the mandatory field is detected has an empty value after submit button is clicked, means that the form is not yet submitted

        log = self.getLogger()
        homepage = Homepage(self.driver)
        simulation = HomepageSimulation(self.driver)
        log.info("Start executing Test Case Homepage Simulasi Kredit - 02")

        # Click the Simulasi Menu on the Homepage
        homepage.simulasi_menu().click()
        log.info("Simulation menu is clicked")

        #####################################
        # MERK DROPDOWN
        #####################################

        # Explicit wait, until the Merk dropdown is presence
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(HomepageSimulation.locator_merk_dropdown))
        log.info("Merk dropdown is found")

        time.sleep(1)

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        merk_select = simulation.merk_dropdown()
        merk = merk_select.get_attribute('value')
        print(f"Merk is {merk}")
        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert merk is None, "Merk should be empty"
        log.info(f"Mandatory validation on merek is work")
        time.sleep(1)

        # End of mandatory validation check

        # Click the Merk dropdown
        simulation.merk_dropdown().click()
        log.info("Merk dropdown is clicked")

        self.search_wait()

        # Fill the merk search keyword
        simulation.dropdown_search().send_keys("Dai")
        log.info("Merk keyword (\"Dai\") is inputted")

        # Explicit wait, until the Daihatsu (Merk) is presence
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(HomepageSimulation.locator_daihatsu))
        log.info("Merk Daihatsu is found")

        # Click the 'Daihatsu'
        simulation.merk_daihatsu().click()
        log.info("Merk Daihatsu is clicked")

        # Get the string of the selected Merk for assertion on the Result Page purpose
        selected_merk = simulation.merk_dropdown2().text

        time.sleep(1)

        #####################################
        # MODEL DROPDOWN
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        model_select = simulation.model_dropdown()
        selected_model = model_select.get_attribute('value')
        print(f"Model is: '{selected_model}'")

        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert selected_model is None, "Model should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Click the Model dropdown
        simulation.model_dropdown().click()
        log.info("Model dropdown is clicked")

        self.search_wait()

        # Fill the Model search keyword
        simulation.dropdown_search().send_keys("Xen")
        log.info("Model keyword (\"Xen\") is inputted")

        # Explicit wait, until the Xenia (Model) is presence
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(HomepageSimulation.locator_xenia))
        log.info("Model Xenia is found")

        # Click the 'Xenia'
        simulation.model_xenia().click()
        log.info("Model Xenia is clicked")

        # Get the string of the selected Merk for assertion on the Result Page purpose
        selected_model = simulation.model_dropdown2().text

        time.sleep(1)

        #####################################
        # TIPE DROPDOWN
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        tipe_select = simulation.tipe_dropdown()
        selected_tipe = tipe_select.get_attribute('value')
        print(f"Tipe is: '{selected_tipe}'")

        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert selected_tipe is None, "Tipe should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Click the Tipe dropdown
        simulation.tipe_dropdown().click()
        log.info("Tipe dropdown is clicked")

        self.search_wait()

        # Fill the Tipe search keyword
        simulation.dropdown_search().send_keys("1.0L Li")
        log.info("Model keyword (\"1.0L Li\") is inputted")

        # Click the '1.0L Li'
        simulation.tipe_10L_Li().click()
        log.info("Tipe 1.0L Li is clicked")

        # Get the string of the selected Tipe for assertion on the Result Page purpose
        selected_tipe = simulation.tipe_dropdown2().text

        time.sleep(1)

        #####################################
        # TRANSMISI DROPDOWN
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        transmisi_select = simulation.transmisi_dropdown()
        selected_transmisi = transmisi_select.get_attribute('value')
        print(f"Transmisi is: '{selected_transmisi}'")

        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert selected_transmisi is None, "Transmisi should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Click the Transmisi dropdown
        simulation.transmisi_dropdown().click()
        log.info("Transmisi dropdown is clicked")

        self.search_wait()

        # Click the 'Manual'
        simulation.transmisi_manual().click()
        log.info("Transmisi \"Manual\" is clicked")

        time.sleep(1)

        #####################################
        # TAHUN DROPDOWN
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        tahun_select = simulation.tahun_dropdown()
        selected_tahun = tahun_select.get_attribute('value')
        print(f"Tahun is: '{selected_tahun}'")

        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert selected_tahun is None, "Transmisi should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Click the Tahun dropdown
        simulation.tahun_dropdown().click()
        log.info("Tahun dropdown is clicked")

        self.search_wait()

        # Fill the Tahun search keyword
        simulation.dropdown_search().send_keys("2010")
        log.info("Tahun keyword (\"2010\") is inputted")

        time.sleep(1)

        # Click the '2010'
        simulation.tahun_2010().click()
        log.info("Tahun 2010 is clicked")

        time.sleep(1)

        #####################################
        # WARNA DROPDOWN
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        warna_select = simulation.warna_dropdown()
        selected_warna = warna_select.get_attribute('value')
        print(f"Warna is: '{selected_warna}'")

        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert selected_warna is None, "Warna should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Click the Warna dropdown
        simulation.warna_dropdown().click()
        log.info("Warna dropdown is clicked")

        self.search_wait()

        # Fill the Warna search keyword
        simulation.dropdown_search().send_keys("Hitam")
        log.info("Warna keyword (\"Hitam\") is inputted")

        time.sleep(1)

        # Click the 'Hitam'
        simulation.warna_hitam().click()
        log.info("Warna Hitam is clicked")

        time.sleep(1)

        #####################################
        # KILOMETER
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        kilometer_input = simulation.input_kilometer()
        inputted_kilometer = kilometer_input.get_attribute('value')
        print(f"Kilometer is: '{inputted_kilometer}'")

        # Assert if the input still empty after the Hitung Simulasi button is clicked
        assert inputted_kilometer is "", "Kilometer should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Fill the Kilometer search keyword
        simulation.input_kilometer().send_keys("50000")
        log.info("Kilometer (\"50.000\") is inputted")

        time.sleep(1)

        #####################################
        # PROVINSI DROPDOWN
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        provinsi_select = simulation.provinsi_dropdown()
        selected_provinsi = provinsi_select.get_attribute('value')
        print(f"Provinsi is: '{selected_provinsi}'")

        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert selected_provinsi is None, "Provinsi should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Click the Provinsi dropdown
        simulation.provinsi_dropdown().click()
        log.info("Provinsi dropdown is clicked")

        self.search_wait()

        # Fill the Provinsi search keyword
        simulation.dropdown_search().send_keys("jak")
        log.info("Provinsi keyword (\"jak\") is inputted")

        time.sleep(1)

        # Click the 'Jakarta D.K.I.'
        simulation.provinsi_jakarta_dki().click()
        log.info("Provinsi Jakarta D.K.I. is clicked")

        time.sleep(1)

        #####################################
        # KOTA DROPDOWN
        #####################################

        # Check the mandatory validation
        # Directly click Hitung Simulasi button
        simulation.button_hitung_simulasi().click()
        log.info("Hitung Simulasi button is clicked")
        time.sleep(1)

        kota_select = simulation.kota_dropdown()
        selected_kota = kota_select.get_attribute('value')
        print(f"Kota is: '{selected_kota}'")

        # Assert if the dropdown still empty after the Hitung Simulasi button is clicked
        assert selected_kota is None, "Kota should be empty"
        time.sleep(1)

        # End of mandatory validation check

        # Click the Kota dropdown
        simulation.kota_dropdown().click()
        log.info("Kota dropdown is clicked")

        self.search_wait()

        # Fill the Kota search keyword
        simulation.dropdown_search().send_keys("pus")
        log.info("Kota keyword (\"pus\") is inputted")

        time.sleep(1)

        # Click the 'Jakarta Pusat'
        simulation.kota_jakarta_pusat().click()
        log.info("Kota Jakarta Pusat is clicked")

        time.sleep(1)

        ###################################################
        # CLICK  'HITUNG SIMULASI' and OPEN THE RESULT PAGE
        ###################################################

        simulation.button_hitung_simulasi().click()
        time.sleep(2)
        log.info("Button Hitung Simulasi is clicked")

        #  Verify the "Simulasi Pembiayaan" title exist on the Result Page
        expected_title = "Simulasi Pembiayaan"
        actual_title = simulation.title_simulasi_pembiayaan().text
        assert expected_title == actual_title, f"{expected_title} not found on the page"
        log.info("Simulasi Pembiayaan page is opened")

        #  Verify the selected Merk exist on the Result Page
        actual_merk = simulation.actual_merk().text
        assert selected_merk.lower() in actual_merk.lower(), f"{selected_merk} not found on the page"
        log.info("The selected Merk appear on the Result Page")

        #  Verify the selected Model and Tipe exist on the Result Page
        actual_model_tipe = simulation.actual_model_tipe().text
        assert selected_model.lower() in actual_model_tipe.lower(), f"{selected_model} not found on the page"
        assert selected_tipe.lower() in actual_model_tipe.lower(), f"{selected_tipe} not found on the page"
        log.info("The selected Model and Tipe appear on the Result Page")

        time.sleep(3)
