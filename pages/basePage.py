class BasePage:
    def __init__(self, device):
        self.device = device

    def find_element(self, element):
        if "xpath" in element.keys():
            return self.device.xpath(element["xpath"])
        else:
            return self.device(**element)

    def assert_existed(self, element):  # 断言元素是否存在
        element_tmp = self.find_element(element)
        assert element_tmp.exists, "断言失败，{}元素不存在!".format(element)

    def is_element_existed(self, element):  # 断言元素是否存在
        element_tmp = self.find_element(element)
        return element_tmp.exists
