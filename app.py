"""Found the flask app."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
import sys
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        try:
            quotes.extend(Ingestor.parse(f))
        except:
            print('Error: ', sys.exc_info()[0])

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    try:
        img = random.choice(imgs)
        quote = random.choice(quotes)
        path = meme.make_meme(img, quote.body, quote.author)
        return render_template('meme.html', path=path)
    except:
       return render_template('error.html')


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    try:
        return render_template('meme_form.html')
    except:
        return render_template('error.html')


@app.route('/create', methods=['POST'])
def meme_post():
    try:
        """Create a user defined meme."""
        if not request.form['image_url']:
            return render_template('meme_form.html')
        tmp = './'+str(random.randint(0,1000))+'.jpg'
        response = requests.get(request.form['image_url'])
        file = open(tmp, 'wb')
        file.write(response.content)
        file.close()
        path = meme.make_meme(tmp, request.form['body'], request.form['author'])
        os.remove(tmp)
        return render_template('meme.html', path=path)
    except:
        # print('Error: ', sys.exc_info()[0])
        print("Invalid file type entered")
        return render_template('meme_error.html')


if __name__ == "__main__":
    app.run(debug=True)
