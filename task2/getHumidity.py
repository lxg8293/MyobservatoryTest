import json
from datetime import datetime, timedelta
import requests


def getweather(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    # 如果请求返回了失败的状态码，将抛出异常
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return
    try:
        content = res.content.decode()
        print("content:" + content)
        if res.status_code == 200:
            print("getweather success")
            content_dict = json.loads(content)
            today = datetime.now()
            future_date_str = add_2day(today)
            forecast_detail_days = content_dict["forecast_detail"]

            # 遍历预报的每一天，找到后天的湿度信息
            for day in forecast_detail_days:
                if day["forecast_date"] == future_date_str:
                    max_rh = day["max_rh"]
                    min_rh = day["min_rh"]
            print(future_date_str)
            print("the relative humidity of the day after tomorrow is " + str(min_rh) + "-" + str(max_rh) + "%")
        else:
            print("getweather failed")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")


def add_2day(today):
    future_date = today + timedelta(days=2)
    future_date_str = future_date.strftime("%Y%m%d")
    return future_date_str


if __name__ == '__main__':
    weather_url = 'https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml'
    getweather(weather_url)
