"""Found the generate meme method."""
import os
import random
import argparse
import sys

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    try:
        img = None
        quote = None

        if path is None:
            images = "./_data/photos/dog/"
            imgs = []
            for root, dirs, files in os.walk(images):
                imgs = [os.path.join(root, name) for name in files]

            img = random.choice(imgs)
        else:
            img = path[0]

        if body is None:
            quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                        './_data/DogQuotes/DogQuotesDOCX.docx',
                        './_data/DogQuotes/DogQuotesPDF.pdf',
                        './_data/DogQuotes/DogQuotesCSV.csv']
            quotes = []
            for f in quote_files:
                quotes.extend(Ingestor.parse(f))
            quote = random.choice(quotes)
        else:
            if author is None:
                raise Exception('Author Required if Body is Used')
            quote = QuoteModel(body, author)

        meme = MemeEngine('./tmp')
        path = meme.make_meme(img, quote.body, quote.author)
        return path
    except:
        print('Error: ', sys.exc_info()[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='meme generator')
    parser.add_argument('--path', default=None, type=str,
                        help='path to image file')
    parser.add_argument('--body', default=None, type=str, help='meme')
    parser.add_argument('--author', default=None, type=str, help='meme author')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
