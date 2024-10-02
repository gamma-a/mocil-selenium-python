from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    # region LOCATOR
    # Declare the variable that contain Locator, using the 'tuple' data type
    ###########################################################################################################
    # LOCATOR
    ###########################################################################################################
    # HEADER
    locator_LogoMocil = (By.XPATH, "//a/img[@src='https://qamocil.dipostar.org/img/apps/logo-color.svg']")
    locator_SearchBox = (By.XPATH, "//input[@name='keyword']")
    locator_HamburgerMenu = (By.XPATH, "//a[@class='d-none d-md-block p-3 tray-menu-overlay-btn']")
    locator_PenumpangButton = (By.XPATH, "//a[@class='section-navigator-pc section-navigator-select']")
    locator_NiagaButton = (By.XPATH, "//a[@class='section-navigator-cv section-navigator-select']")
    locator_TukarTambahButton = (By.XPATH, "//div[@class='header-tradein']")
    locator_FavoritButton = (By.XPATH, "//div[@class='favorite-nav']")
    locator_AdvanceFilter = (By.XPATH, "(//div[@class='universal-filter d-flex justify-content-center'])[1]")

    # BANNER AND KATEGORI MENU
    locator_main_banner = (By.XPATH, "//div[@id='carouselBanner']")
    locator_kategori_menu_title = (By.XPATH, "//h5[@class='fresh-title']")
    locator_mobil_harga_miring_menu = (By.XPATH, "(//a[@class='col-4 col-md-4 section-menu-item'])[1]")
    locator_cicilan_murah_menu = (By.XPATH, "(//a[@class='col-4 col-md-4 section-menu-item'])[2]")
    locator_dp_rendah_menu = (By.XPATH, "(//a[@class='col-4 col-md-4 section-menu-item'])[3]")
    locator_promo_menu = (By.XPATH, "(//a[@class='col-4 col-md-4 section-menu-item'])[4]")
    locator_simulasi_menu = (By.XPATH, "//a[@class='d-none d-md-flex col-4 section-menu-item']")
    locator_tukar_tambah_menu = (By.XPATH, "(//a[@class='col-4 col-md-4 section-menu-item'])[5]")
    locator_wa_floating_button = (By.XPATH, "(//a[@id='contact_us_chat'])[3]")

    # CAR LIST SECTION
    locator_mobil_bekas_pilihan_title = (By.CSS_SELECTOR, ".fresh-title.page-title")
    locator_deskripsi_car_list = (By.CSS_SELECTOR, ".page-excerpt.mb-3")

    # endregion

    # FOOTER
    locator_mocil_logo_footer = (By.XPATH, "//a[@class='fresh-footer-logo']")
    locator_blog_link = (By.XPATH, "(//a[text()='Blog'])[1]")
    locator_mitra_link = (By.XPATH, "(//a[text()='Daftar Mitra Mocil'])[1]")
    locator_faq_link = (By.XPATH, "(//a[text()='FAQ'])[1]")
    locator_kebijakan_link = (By.XPATH, "(//a[text()='Kebijakan Privasi'])[1]")
    locator_tentang_link = (By.XPATH, "(//a[text()='Tentang Mocil'])[1]")
    locator_syarat_link = (By.XPATH, "(//a[text()='Syarat dan Ketentuan'])[1]")
    locator_hak_link = (By.XPATH, "(//a[text()='Hak Cipta'])[1]")
    locator_karir_link = (By.XPATH, "(//a[text()='Karir'])[1]")
    locator_facebook_link = (By.XPATH, "//a[@href='https://www.facebook.com/Mocilid-114845429884611']")
    locator_twitter_link = (By.XPATH, "//a[@href='https://twitter.com/Mocil_Official']")
    locator_instagram_link = (By.XPATH, "//a[@href='https://www.instagram.com/mocil.id/']")

    # region WEB ELEMENT
    ###########################################################################################################
    # WEB ELEMENT
    ###########################################################################################################

    # HEADER ELEMENT
    ###########################################################################################################
    def mocil_logo(self):
        return self.driver.find_element(*Homepage.locator_LogoMocil)  # Put * to understand the tuple format

    def search_box(self):
        return self.driver.find_element(*Homepage.locator_SearchBox)

    def hamburger_menu(self):
        return self.driver.find_element(*Homepage.locator_HamburgerMenu)

    def penumpang_button(self):
        return self.driver.find_element(*Homepage.locator_PenumpangButton)

    def niaga_button(self):
        return self.driver.find_element(*Homepage.locator_NiagaButton)

    def tukar_tambah_button(self):
        return self.driver.find_element(*Homepage.locator_TukarTambahButton)

    def favorit_button(self):
        return self.driver.find_element(*Homepage.locator_FavoritButton)

    def advance_filter(self):
        return self.driver.find_element(*Homepage.locator_AdvanceFilter)

    # BANNER AND KATEGORI MENU ELEMENT
    #################################################################################################################
    def main_banner(self):
        return self.driver.find_element(*Homepage.locator_main_banner)

    def mobil_harga_miring_menu(self):
        return self.driver.find_element(*Homepage.locator_mobil_harga_miring_menu)

    def cicilan_murah_menu(self):
        return self.driver.find_element(*Homepage.locator_cicilan_murah_menu)

    def dp_rendah_menu(self):
        return self.driver.find_element(*Homepage.locator_dp_rendah_menu)

    def promo_menu(self):
        return self.driver.find_element(*Homepage.locator_promo_menu)

    def simulasi_menu(self):
        return self.driver.find_element(*Homepage.locator_simulasi_menu)

    def tukar_tambah_menu(self):
        return self.driver.find_element(*Homepage.locator_tukar_tambah_menu)

    def wa_floating_button(self):
        return self.driver.find_element(*Homepage.locator_wa_floating_button)

    # CAR LIST SECTION
    #################################################################################################################
    def mobil_bekas_pilihan_title(self):
        return self.driver.find_element(*Homepage.locator_mobil_bekas_pilihan_title)

    def deskripsi_car_list(self):
        return self.driver.find_element(*Homepage.locator_deskripsi_car_list)

    # FOOTER
    #################################################################################################################
    def mocil_logo_footer(self):
        return self.driver.find_element(*Homepage.locator_mocil_logo_footer)

    def blog_link(self):
        return self.driver.find_element(*Homepage.locator_blog_link)

    def mitra_link(self):
        return self.driver.find_element(*Homepage.locator_mitra_link)

    def faq_link(self):
        return self.driver.find_element(*Homepage.locator_faq_link)

    def kebijakan_link(self):
        return self.driver.find_element(*Homepage.locator_kebijakan_link)

    def tentang_link(self):
        return self.driver.find_element(*Homepage.locator_tentang_link)

    def syarat_link(self):
        return self.driver.find_element(*Homepage.locator_syarat_link)

    def hak_link(self):
        return self.driver.find_element(*Homepage.locator_hak_link)

    def karir_link(self):
        return self.driver.find_element(*Homepage.locator_karir_link)

    def facebook_link(self):
        return self.driver.find_element(*Homepage.locator_facebook_link)

    def twitter_link(self):
        return self.driver.find_element(*Homepage.locator_twitter_link)

    def instagram_link(self):
        return self.driver.find_element(*Homepage.locator_instagram_link)

    # endregion
