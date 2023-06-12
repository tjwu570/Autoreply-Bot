import string
from mtranslate import translate

def translate_to_sc(text: str) -> str:
    if text == "結塊" or text == "塊狀物" or text == "潮濕結塊":
        text = "我在奶粉罐裡發現了結塊，請告訴我這是怎麼回事。"
    elif text == "蟲" or text == "蜜蜂" or text == "螞蟻" or text == "蟲蟲":
        text = "我上禮拜新買了一罐奶粉，喝到一半的時候發現有蟲在奶粉罐裡面，這有點離譜，請給我一個合理的解釋。"
    elif text == "頭髮" or text == "毛髮" or text == "髮" or text == "體毛":
        text = "我在奶粉裡發現毛髮，看長度似乎不是我們家裡任何一個人的，想確認這是否工廠的人員所造成的疏失?請給我一個合理的答覆。"
    elif text == "藍色碎屑" or text == "藍色屑屑":
        text = "今天將奶粉罐開封之後，就發現上面有藍色的碎屑，看起來是蓋子的塑膠脫落。我覺得這已經是很嚴重的食安問題了，要是我沒注意到，讓小孩喝下肚，後果根本無法想像。請你給我合理的解釋，以及如何進行補償。"
    elif text == "生鏽" or text == "鏽斑" or text == "鐵鏽" or text == "鏽":
        text = "剛買的奶粉，卻發現外罐有生鏽的情形，請問這是正常現象嗎?"

    
    sc = translate(text, to_language='zh-CN')
    # return text
    return sc