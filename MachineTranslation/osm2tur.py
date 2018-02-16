import re
import tensorflow as tf


data_path = "D:\İshak\Database\Words\A.txt"
#  def get_word_list(data_path):
input_texts = list()
output_texts = list()
lines = list()

with open(data_path, 'r', encoding='utf-8') as f:
    lines = f.read().split("\n")
# you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
# with open(data_path, 'r', encoding='utf-8') as f:
#    lines.append(f.read())
# # text="*ali:ali"
# input_text, output_text = text.split(":")
# print(input_text.replace("*",""),":",output_text)

for line in lines:
#  print(line)
    if line is not None and line != "":
        line_text = str(line)
        input_text, output_text = line.split(":")
        input_texts.append(input_text.replace("*", ""))
        output_texts.append(output_text)


print(input_texts[12])
print(output_texts[12])

print(len(input_texts))
print(len(output_texts))


def load_vocab(filename):
    vocab = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            vocab[line.strip().replace("*","")] = idx
    return vocab


load_vocab(data_path)




