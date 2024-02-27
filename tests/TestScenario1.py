from Pages import SearchHelper
import logging

logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


class TestScenario1:

    def test_scenario(self, browser):
        logging.info("start testing first scenario")
        page = SearchHelper(browser)
        page.go_to_site()
        page.enter_contacts()
        page.enter_tensor_site()
        handles_list = browser.window_handles
        browser.switch_to.window(handles_list[1])
        logging.info(f"window was switched. from {handles_list[0]} to"
                     f" {handles_list[1]}")
        card_about_people = page.get_people_card()

        search_title = "Сила в людях"
        # Проверяем есть ли на странице нужный блок
        assert search_title == card_about_people[0].text, (
            f"Не нашли блок {search_title}"
        )

        page.enter_about()
        expected_url = "https://tensor.ru/about"
        curr_url = page.driver.current_url
        # Проверяем что перешли по ожидаемой ссылке
        assert expected_url == curr_url, (
            f"{expected_url} не совпадает с текущей ссылкой: {curr_url}"
        )
        logging.info(f"current url {curr_url}")

        sizes_list = page.get_cards_from_about_page()
        logging.info(f"1 image sizes: {sizes_list[0]}")
        for i in range(len(sizes_list)-1):
            # Проверяем что фотографии одинакового размера
            assert sizes_list[0] == sizes_list[i+1], (
                f"Размер фотографий не совпадает!"
            )
            logging.info(f"{i+1} image sizes: {sizes_list[i+1]}")
