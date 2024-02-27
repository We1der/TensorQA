from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class SearchLocators:
    LOCATOR_SEARCH_CONTACTS = (By.LINK_TEXT, "Контакты")
    LOCATOR_SEARCH_TENSOR_LOGO = (
        By.CLASS_NAME,
        "sbisru-Contacts__logo-tensor"
    )
    LOCATOR_SEARCH_CARD = (
        By.CSS_SELECTOR,
        "div[class*=tensor_ru-Index__block4-content]>p"
    )
    LOCATOR_SEARCH_MORE_DETAILS = (
        By.CSS_SELECTOR,
        "div[class*=tensor_ru-Index__block4-content]>p>a"
    )
    LOCATOR_SEARCH_CARDS_ABOUT_PAGE = (
        By.CSS_SELECTOR,
        "img[class*=tensor_ru-About__block3-image]"
    )
    LOCATOR_SEARCH_REGION = (
        By.CLASS_NAME,
        "sbis_ru-Region-Chooser__text"
    )
    LOCATOR_SEARCH_REGIONS_LIST = (
        By.CLASS_NAME,
        "sbis_ru-Region-Panel__item"
    )
    LOCATOR_SEARCH_PARTNERS = (
        By.CLASS_NAME,
        "sbisru-Contacts-List__name"
    )


class SearchHelper(BasePage):

    def enter_contacts(self):
        search_element = self.find_element(
            SearchLocators.LOCATOR_SEARCH_CONTACTS
        )
        search_element.click()
        return search_element

    def enter_tensor_site(self):
        search_element = self.find_element(
            SearchLocators.LOCATOR_SEARCH_TENSOR_LOGO
        )
        search_element.click()
        return search_element

    def get_people_card(self):
        banners_list = self.find_elements(
            SearchLocators.LOCATOR_SEARCH_CARD
        )
        return banners_list

    def enter_about(self):
        search_element = self.find_clickable_element(
            SearchLocators.LOCATOR_SEARCH_MORE_DETAILS
        )
        self.driver.execute_script("arguments[0].click();", search_element)
        return search_element

    def get_cards_from_about_page(self):
        cards_list = self.find_elements(
            SearchLocators.LOCATOR_SEARCH_CARDS_ABOUT_PAGE
        )
        sizes = [(el.rect["height"], el.rect["width"]) for el in cards_list]
        return sizes

    def get_region(self):
        search_element = self.find_element(
            SearchLocators.LOCATOR_SEARCH_REGION
        )
        return search_element

    def get_partners(self):
        search_element = self.find_elements(
            SearchLocators.LOCATOR_SEARCH_PARTNERS
        )
        return search_element

    def change_region(self, region_name_to_change: str):
        region_element = self.get_region()
        region_element.click()
        regions_objects_list = self.find_elements(
            SearchLocators.LOCATOR_SEARCH_REGIONS_LIST
        )
        regions_names_list = [el.text for el in regions_objects_list]
        search_region = regions_names_list.index(region_name_to_change)
        changed = regions_objects_list[search_region].click()
        return changed
