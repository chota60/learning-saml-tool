from base64 import b64encode, b64decode  

# input.txt から base64 形式の文字列を読み込む
file_name = "input.txt"
decode_text = ""
with open(file_name, mode='r') as f:
    input_text = f.read()
    # デコードして結果を格納
    decode_text = b64decode(input_text).decode()

import pprint
# pprint.pprint(decode_text)

# xml 形式の文字列だとよく構造がわからないので、 dict に変換してプリントする
# @がついているものは属性
# #text はテキスト
import xmltodict
dict_data = xmltodict.parse(decode_text, force_cdata=True)
pprint.pprint(dict_data)
