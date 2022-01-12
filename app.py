from flask import Flask, request, render_template
import logging
from test import transform_text, vectorize_word, predict
import os

app = Flask(__name__)

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        logging.basicConfig(filename='All_logs/Testing_logs.log',
                            filemode='w',
                            level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(module)s---- %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger('')
        f = open('All_logs/Testing_logs.log', 'w')
        f.truncate()

        text = request.form.get('message')

        transformed_text = transform_text(text, logger)
        vector = vectorize_word(transformed_text, logger)
        results = predict(vector, logger)

        if results == 1:
            results = "Yes it is a Spam Message"
        else:
            results = 'No it is not a spam message'
        return render_template('index.html', prediction=results)

    else:
        return render_template('index.html')


port = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
