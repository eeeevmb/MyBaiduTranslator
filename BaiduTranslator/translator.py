import requests
import hashlib
import random

class BaiduTranslator:
    def __init__(self, app_id, secret_key):
        """
        初始化百度翻译实例
        :param app_id: 百度翻译 API 的 APP ID
        :param secret_key: 百度翻译 API 的密钥
        """
        self.app_id = app_id
        self.secret_key = secret_key
        self.base_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

    def translate(self, query, from_lang='auto', to_lang='zh'):
        """
        调用百度翻译 API 进行翻译
        :param query: 待翻译的文本
        :param from_lang: 源语言（'auto' 表示自动检测）
        :param to_lang: 目标语言（例如 'zh' 表示中文，'en' 表示英文）
        :return: 翻译结果或错误信息
        """
        salt = random.randint(32768, 65536)
        sign = hashlib.md5((self.app_id + query + str(salt) + self.secret_key).encode('utf-8')).hexdigest()

        # 构建请求参数
        params = {
            'q': query,
            'from': from_lang,
            'to': to_lang,
            'appid': self.app_id,
            'salt': salt,
            'sign': sign
        }

        try:
            # 发起请求
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            result = response.json()
            if "trans_result" in result:
                return result['trans_result'][0]['dst']
            else:
                return "翻译失败：" + result.get("error_msg", "未知错误")
        except requests.exceptions.RequestException as e:
            return f"请求出错：{e}"

# 测试翻译功能
if __name__ == '__main__':

    translator = BaiduTranslator()  # 参数为id和密钥，字符串类型
    text = input("请输入要翻译的内容：")
    translated_text = translator.translate(text, from_lang='auto', to_lang='zh')
    print("翻译结果：", translated_text)
