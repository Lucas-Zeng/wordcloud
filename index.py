import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread # 处理图像的函数
import jieba
import numpy as np
from PIL import Image

text_from_file_with_apath = open('article.txt').read()
# text_from_file_with_apath = u'你好吗今天的天气真好啊我昨天去了动物园'
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
mask = imread( "mask.jpeg")
# mask = imread( "mask.png")

# mask = np.array(Image.open( "mask.png"))
wc = WordCloud(mask=mask, font_path='fzmt.ttf').generate(wl_space_split)
wc.to_file("output/horse.png")
plt.imshow(wc)
plt.axis("off")
plt.show()
