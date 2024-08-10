from DrissionPage import ChromiumPage
from typing import Optional
import pyttsx3


class TJWeb:
    """_summary_
    """    
    def __init__(self):
        """_summary_
        """        
        self.drission = ChromiumPage()
        self.news_url = 'https://news.tongji.edu.cn/info/1003/88136.htm'
        self.drission.get(self.news_url)
        self.main_text = ''

    def auto_replace(self, replace_text: Optional[str] = '陈麒安'):
        """_summary_

        Args:
            replace_text (Optional[str], optional): _description_. Defaults to 'Python'.
        """        
        block = self.drission.ele('@class=content-title fl')
        title_ele = block.ele('tag:h3')
        text = title_ele.raw_text
        text = text.replace('覃海洋', replace_text)
        js_code = f'''
            document.getElementsByTagName("h3")[1].innerHTML = '{text}';
        '''
        block.run_js(js_code)
        main_ele = self.drission.ele('@style=background:#f5f5f5;')
        main_text = main_ele.raw_text
        self.main_text += main_text

    def speak_text(self):
        """_summary_
        """
        pyttsx3.speak(self.main_text)


def main():
    tj_web = TJWeb()
    tj_web.auto_replace()
    tj_web.speak_text()


if __name__ == '__main__':
    main()
