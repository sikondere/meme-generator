"""Generate memes."""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random


class MemeEngine:
    """Generate memes."""

    def __init__(self, output_dir):
        """Init."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make memes."""
        try:
            im = Image.open(img_path)
            im.thumbnail((width, width), Image.ANTIALIAS)
            x = ImageDraw.Draw(im)
            font = ImageFont.truetype('FreeMono.ttf', 20)
            p1 = random.randint(0, 200)
            p2 = random.randint(0, 200)
            x.text((p1, p2), f'{text}\n {author}',
                   font=font, fill=(255, 255, 255), stroke_width=1,
                                    stroke_fill="white")
            # im.show()
            tag = random.randint(0, 1000)
            path = self.output_dir+f'{str(tag)}.jpg'
            im.save(path, 'JPEG')
            return path
        except Exception:
            pass
