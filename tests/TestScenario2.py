import logging
from Pages import SearchHelper


logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


class TestScenario2:

    def test_scenario(self, browser):
        logging.info("start testing second scenario")
        page = SearchHelper(browser)
        page.go_to_site()
        page.enter_contacts()
        expected_region = "г. Москва"
        # expected_region = "Ярославская обл."
        # Проверяем определился ли регион
        defined_region = page.get_region().text
        assert expected_region == defined_region, (
            f"Регионы не совпадают или не найдены! Ожидался регион "
            f"{expected_region}, а получили {defined_region}"
        )
        logging.info(f"expected region: {expected_region}")
        logging.info(f"defined region: {defined_region}")

        base_partners_list = page.get_partners()
        # Проверяем есть ли список партнёров
        assert len(base_partners_list) > 0, "Нет списка партнёров!"
        logging.info(f"count of partners list: {len(base_partners_list)}")

        region_to_change = "41 Камчатский край"
        page.change_region(region_to_change)
        expected_region = "Камчатский край"
        defined_region = page.get_region().text
        # Проверяем изменился ли регион
        assert expected_region == defined_region, (
            f"Регионы не совпадают или не найдены! Ожидался регион "
            f"{expected_region}, а получили {defined_region}"
        )
        logging.info(f"expected region: {expected_region}")
        logging.info(f"defined region: {defined_region}")

        new_partners_list = page.get_partners()
        # Проверяем изменился ли список партнёров после сены региона
        assert new_partners_list != base_partners_list, (
            "Список партнёров не изменился!"
        )

        expected_title = "СБИС Контакты — " + expected_region
        defined_title = new_partners_list[0].parent.title
        # Проверяем title у партнёра
        assert new_partners_list[0].parent.title == expected_title, (
            f"title не совпадает с ожидаемым! Ожидался {expected_title}, "
            f"а получили {defined_title}"
        )
        logging.info(f"partner has title {defined_title}")

        expected_region_url = "/41-kamchatskij-kraj"
        curr_url = page.driver.current_url
        # Проверяем изменился ли адрес ссылки после смены региона
        assert expected_region_url in curr_url, (
            "URL не содержит ожидаемого региона"
        )
        logging.info(f"current url {curr_url}")
