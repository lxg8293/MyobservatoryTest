import os
import allure
import pytest
import uiautomator2 as u2
import time
from PIL import Image

from pages.basePage import BasePage
from pages.homePage import HomePage

device = None
homePage = None


# 处里启动app
@pytest.fixture(scope='function', autouse=True)
def start_app():
    device.app_start(homePage.package_name, stop=True)
    time.sleep(9)
    # 处理启动后的广告弹窗，如果是安装后的首次启动，还需要处理权限弹框，暂未处理
    homePage.deal_home_popbox()
    yield
    device.app_stop(homePage.package_name)


# 处理断言失败后截图，并添加到报告中
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        screenshot_path = f"screenshot_wait.png"
        save_screenshot(device,screenshot_path)
        # 将截图附加到Allure报告中
        with open(screenshot_path, "rb") as f:
            allure.attach(f.read(), name=f"断言失败截图", attachment_type=allure.attachment_type.PNG)
            time.sleep(0.4)
        delete(screenshot_path)
        time.sleep(0.1)


# 实例化device
@pytest.fixture(scope='class', autouse=True)
def init_devices():
    global device
    global homePage
    if device is None:
        device = u2.connect()
    homePage = HomePage(device=device)
    return device


def save_screenshot(dev,screenshot_path):
    """
    删除图片
    :param dev:device实例
    :param screenshot_path:图片名称
    """
    dev.screenshot(screenshot_path)
    im = Image.open(screenshot_path)
    # 读取图片尺寸（像素）
    (x, y) = im.size
    # 定义缩小后的标准宽度
    x_1 = 300
    # 计算缩小后的高度
    y_1 = int(y * x_1 / x)
    # 改变尺寸，保持图片高品质
    out = im.resize((x_1, y_1))
    # 判断图片的通道模式，若图片在RGBA模式下，需先将其转变为RGB模式
    if out.mode == 'RGBA':
        # 转化为rgb格式
        out = out.convert('RGB')
    # 最后保存为png格式的图片，这里因为图片本身为png所以后缀不更改
    out.save(screenshot_path)


def delete(image_path):
    """
    删除图片
    :param image_path:
    :return:
    """
    if os.path.isfile(image_path):
        os.remove(image_path)
