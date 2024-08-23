import time
from pages.basePage import BasePage


class HomePage(BasePage):
    """========home页面封装=============="""
    package_name = 'hko.MyObservatory_v1_0'

    # 首页弹窗广告退出按钮
    pop_exit_btn = {"resourceId": "hko.MyObservatory_v1_0:id/exit_btn"}

    # 菜单导航按钮
    home_navigate = {"description": "Navigate up"}

    # Forecast & Warning Services菜单
    forecast_warning_services = {"text": "Forecast & Warning Services"}

    # 9-Day Forecast子菜单
    forecast9 = {"text": "9-Day Forecast"}

    forecast9_view = {"resourceId": "hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit"}

    def open_navigate(self):
        self.find_element(self.home_navigate).click()

    def click_forecast_waring_services_item(self):
        self.find_element(self.forecast_warning_services).click()

    def click_9day_forecast(self):
        # 有两个同样名称的元素，取第二个
        self.find_element(self.forecast9)[1].click()

    def assert_open_9day_forecast(self):
        time.sleep(3)
        self.assert_existed(self.forecast9_view)

    def deal_home_popbox(self):
        while self.is_element_existed(self.pop_exit_btn):
            self.find_element(self.pop_exit_btn).click()
