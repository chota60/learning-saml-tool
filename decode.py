from base64 import b64encode, b64decode  

# input.txt から base64 形式の文字列を読み込む
file_name = "input.txt"
decode_text = ""
with open(file_name, mode='r') as f:
    input_text = f.read()
    # デコードして結果を格納
    decode_text = b64decode(input_text).decode()

# xml 形式の文字列になっているので、パースする
from xml.etree import ElementTree
root = ElementTree.fromstring(decode_text)
print(root.tag)
# 子要素も出力する
for child in root:
    print(child.tag, child.text)
    



