"""Generate memes."""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import random
import sys
import textwrap

class MemeEngine:
    """Generate memes."""

    def __init__(self, output_dir):
        """Init."""
        self.output_dir = output_dir
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
        except:
            print('Error: ', sys.exc_info()[0])

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make memes."""
        try:
            im = Image.open(img_path)
            im.thumbnail((width, width), Image.ANTIALIAS)
            x = ImageDraw.Draw(im)
            font = ImageFont.truetype('./_data/Fonts/FreeMono.ttf', 20)
            p1 = random.randint(0, 200)
            p2 = random.randint(0, 200)
            wrapper = textwrap.TextWrapper(width=20)
            meme_text = wrapper.fill(text=str(text)+'\n'+str(author))
            x.text((p1, p2), meme_text,
                   font=font, fill=(255, 255, 255), stroke_width=1,
                                    stroke_fill="white")
            tag = random.randint(0, 1000)
            meme = str(tag)+'.jpg'
            path = os.path.join(self.output_dir, meme)
            im.save(path, 'JPEG')
            return path
        except:
            print('Error: ', sys.exc_info()[0])
