import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object import homepage_simulation
from page_object.home_page import Homepage
from page_object.homepage_simulation import HomepageSimulation
from utilities.base_class import BaseClass


class TestHomepageSimulation(BaseClass):

    def test_homepage_simulasi_kredit_01(self):
        #  Given that User is on the Kategori Menu section on the Homepage when User clicked on Simulasi button then User will see popup modal for Hitung Simulasi
        log = self.getLogger()
        homepage = Homepage(self.driver)
        simulation = HomepageSimulation(self. driver)
        log.info("Start executing Test Case Homepage Simulasi Kredit - 01")

        def search_wait():
            wait2 = WebDriverWait(self.driver, 10)
            wait2.until(expected_conditions.presence_of_element_located(HomepageSimulation.locator_dropdown_search))
            log.info("Search box is found")

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

        time.sleep(2)

        # Click the Merk dropdown
        simulation.merk_dropdown().click()
        log.info("Merk dropdown is clicked")

        search_wait()

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

        time.sleep(2)

        #####################################
        # MODEL DROPDOWN
        #####################################

        # Click the Merk dropdown
        simulation.model_dropdown().click()
        log.info("Model dropdown is clicked")

        search_wait()

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

        time.sleep(2)

        #####################################
        # TIPE DROPDOWN
        #####################################

        # Click the Tipe dropdown
        simulation.tipe_dropdown().click()
        log.info("Tipe dropdown is clicked")

        search_wait()

        # Fill the Tipe search keyword
        simulation.dropdown_search().send_keys("1.0L Li")
        log.info("Model keyword (\"1.0L Li\") is inputted")

        # Click the '1.0L Li'
        simulation.tipe_10L_Li().click()
        log.info("Tipe 1.0L Li is clicked")

        time.sleep(1)

        #####################################
        # TRANSMISI DROPDOWN
        #####################################

        # Click the Transmisi dropdown
        simulation.transmisi_dropdown().click()
        log.info("Transmisi dropdown is clicked")

        search_wait()

        # Click the 'Manual'
        simulation.transmisi_manual().click()
        log.info("Transmisi \"Manual\" is clicked")

        time.sleep(2)