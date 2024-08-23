import time
import allure
import uiautomator2 as u2
from pages.homePage import HomePage


@allure.feature('homepage test')
class Test_HomePage:
    def test_check_9day_forecast(self):
        device = u2.connect()
        homePage = HomePage(device=device)
        time.sleep(3)
        with allure.step("Open Menu"):
            homePage.open_navigate()
        with allure.step("click the forecast waring services item"):
            homePage.click_forecast_waring_services_item()
        time.sleep(3)
        with allure.step("click the 9 day forecast item"):
            homePage.click_9day_forecast()
        with allure.step('check the 9day forecast view by the element'):
            homePage.assert_open_9day_forecast()
