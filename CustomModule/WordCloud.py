import os
from CustomModule import WordCloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

def WCGen():
    text = open(os.path.join(os.path.dirname(__file__), "../Resource", "data.txt"), encoding="utf-8").read()
    bg_mask = np.array(Image.open(os.path.join(os.path.dirname(__file__), "../Resource/BikeMask.jpg")))

    wc = WordCloud(background_color="white",
        font_path=os.path.join(os.path.dirname(__file__), "../Resource/NanumGothic.ttf"),
        mask=bg_mask
    )

    wc = wc.generate(text)

    plt.figure(figsize=(12, 12))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()