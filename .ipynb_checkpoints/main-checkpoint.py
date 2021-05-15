import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import datetime


file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    weekday = datetime.date.today().weekday()
#     print(weekday)
    
    USER_ID = info['USER_ID']
    if (weekday == 6):
        messages = TextSendMessage(text="今日は6限まである!死ぬな!\n1.\n2.メディア分析法(10:40~\n3.\n4.教育相談の理論と方法\n5.教育相談の理論と方法\n6.情報科指導法")
    elif (weekday == 0):
        messages = TextSendMessage(text="1限[ビデオオン]あるぞ!起きて！\n1.データベース入門\n2.数学科指導法\n3.インターラクティブシステム\n4.\n5.センサー入門\n")
    elif (weekday == 1):
        messages = TextSendMessage(text="今日は大学に行く日だ!\n1.\n2.自然言語処理\n3.３年プロジェクト\n4.\n5.\n")
    elif (weekday == 2):
        messages = TextSendMessage(text="無の木曜日!\n1.情報科学英語a\n2.数理モデル\n3.数理モデル\n4.\n5.情報数学a\n")
    elif (weekday == 3):
        messages = TextSendMessage(text="午前休でも起きて家事するぞ\n1.\n2.\n3.情報科学c\n4.ソフトウェア開発法\n5.ソフトウェア開発法\n")
    else:
        messages = TextSendMessage(text="休日だけど、起きて!課題溜まってるでしょ！やれー！！！")
        
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()