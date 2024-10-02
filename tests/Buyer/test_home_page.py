from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.home_page import Homepage
from utilities.base_class import BaseClass


class TestHomePage(BaseClass):

    def test_Homepage_01(self):
        # Given that User is on Mocil homepage then User able to locate clickable Mocil logo, search field, hamburger menu, button Penumpang and Niaga, button Tukar Tambah, button favorit, and Advance Filters
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Start executing Test Case Homepage - 01")

        header_elements = [
            (homepage.mocil_logo, "Mocil Logo - Header"),
            (homepage.search_box, "Search Box - Header"),
            (homepage.hamburger_menu, "Hamburger Menu"),
            (homepage.penumpang_button, "Penumpang Button"),
            (homepage.niaga_button, "Niaga Button"),
            (homepage.tukar_tambah_button, "Tukar Tambah Button"),
            (homepage.favorit_button, "Favorit Button"),
            (homepage.advance_filter, "Advance Filter")
        ]

        for element, element_name in header_elements:
            try:
                exist = element()
                assert exist, f"{element_name} doesn't exist"
                log.info(f"{element_name} exist")
            except NoSuchElementException:
                log.error(f"{element_name} doesn't exist")
                assert False, f"{element_name} doesn't exist"
        log.info(f"Done checking header element availability")

    def test_Homepage_02(self):
        # Given that User is on Mocil homepage, then User able to locate sections for Main Banner, Kategori Menu Title, Super Deal Menu, Cicilan Murah Menu, DP Rendah Menu, Promo Menu, Simulasi Menu, Tukar Tambah Menu, Rekomendasi Mobil Bekas Pilihan Title, Testimoni, and WA Floating button
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Start executing Test Case Homepage - 02")

        banner_kategori_elements = [
            (homepage.main_banner, "Main Banner"),
            (homepage.mobil_harga_miring_menu, "Mobil Harga Miring Menu"),
            (homepage.cicilan_murah_menu, "Cicilan Murah Menu"),
            (homepage.dp_rendah_menu, "DP Rendah Menu"),
            (homepage.promo_menu, "Promo Menu"),
            (homepage.simulasi_menu, "Simulasi Menu"),
            (homepage.tukar_tambah_menu, "Tukar Tambah Menu"),
            (homepage.wa_floating_button, "WA Floating Button")
        ]

        for element, element_name in banner_kategori_elements:
            try:
                exist = element()
                assert exist, f"{element_name} doesn't exist"
                log.info(f"{element_name} exist")
            except NoSuchElementException:
                log.error(f"{element_name} doesn't exist")
                assert False, f"{element_name} doesn't exist"
        log.info("Done checking main banner and kategori menu element availability")

    def test_Homepage_03(self):
        #  Given that User is on Mocil homepage, when User navigate to the footer then User able to locate clickable Mocil logo, socil media section (Facebook, Twitter, Instagram), Hubungi Kami section and Footer links.
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Start executing Test Case Homepage - 03")

        footer_elements = [
            (homepage.mocil_logo_footer, "Mocil Logo - Footer"),
            (homepage.blog_link, "Link to Blog"),
            (homepage.mitra_link, "Link to Daftar Mitra Mocil"),
            (homepage.faq_link, "Link to FAQ"),
            (homepage.kebijakan_link, "Link to Kebijakan Privasi"),
            (homepage.tentang_link, "Link to Tentang Mocil"),
            (homepage.syarat_link, "Link to Syarat dan ketentuan"),
            (homepage.hak_link, "Link to Hak Cipta"),
            (homepage.karir_link, "Link to Karir"),
            (homepage.facebook_link, "Link to Facebook"),
            (homepage.twitter_link, "Link to Twitter"),
            (homepage.instagram_link, "Link to Instagram")
        ]

        for element, element_name in footer_elements:
            try:
                exist = element()
                assert exist, f"{element_name} doesn't exist"
                log.info(f"{element_name} exist")
            except NoSuchElementException:
                log.error(f"{element_name} doesn't exist")
                assert False, f"{element_name} doesn't exist"
        log.info("Done checking footer element availability")

    def test_Homepage_04(self):
        #  Given that User is on Mocil homepage when User check the Mocil Logo then it should have H1 heading tag
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Start executing Test Case Homepage - 04")

        mocil_logo = homepage.mocil_logo()
        grandparent_h1 = mocil_logo.find_element(By.XPATH,
                                                 "./ancestor::h1")  # Check if the grandparent has <h1> tag or not
        assert grandparent_h1.tag_name == "h1", "Grandparent is not <h1> element"
        log.info(f"The {homepage.mocil_logo.__name__} has <H1> tag")

    def test_Homepage_05(self):
        #  Given that User is on Mocil homepage when User check the Mobil Bekas Pilihan title section then they will have H3 heading tag
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Start executing Test Case Homepage - 05")

        car_list_title = homepage.mobil_bekas_pilihan_title()
        assert car_list_title.tag_name == "h1", "H1 is not available"
        log.info(f"The {homepage.mobil_bekas_pilihan_title.__name__} has <H1> tag")

    def test_Homepage_06(self):
        #  Given that User is on Mocil homepage when User check the description of the Rekomendasi Mobil Bekas Pilihan section then they will have H3 heading tag
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Start executing Test Case Homepage - 06")

        deskripsi = homepage.deskripsi_car_list()
        assert deskripsi.tag_name == "h3", "H3 is not available"
        log.info(f"The {homepage.deskripsi_car_list.__name__} has <H3> tag")

    def test_Homepage_07(self):
        #  Given that User is on Mocil homepage when User check the Mobil Harga Miring, Cicilan Murah Menu, DP Rendah Menu, Promo Menu, Simulasi Menu, Tukar Tambah Menu then it will have H4 heading tag
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Start executing Test Case Homepage - 07")

        kategori_menu_title_list = [
            (homepage.mobil_harga_miring_menu(), "Mobil Harga Miring Menu Title"),
            (homepage.cicilan_murah_menu(), "Cicilan Murah Menu Title"),
            (homepage.dp_rendah_menu(), "DP Rendah Menu Title"),
            (homepage.promo_menu(), "Promo Menu Title"),
            (homepage.simulasi_menu(), "Simulasi Menu Title"),
            (homepage.tukar_tambah_menu(), "Tukar Tambah Menu Title")
        ]

        for title, title_name in kategori_menu_title_list:
            h4 = title.find_element(By.TAG_NAME, "h4")
            assert h4 is not None, f"The {title_name} doesn't contain H4 tag"
            log.info(f"The {title_name} has an <H4> tag")
