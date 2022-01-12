import pandas as pd
import string
import nltk
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import pickle

ps = PorterStemmer()
tfidf = TfidfVectorizer(max_features=3000)


class data_preprocessing:
    """
        This class will be used for dataPreprocessing

        Written By: Suraj Joshi
        Version: 1.0
        Revisions: None

    """

    def __init__(self, file_location, logger):
        try:
            """
                Method Name:__init__
                Description:Will be used Member initialization
                Input:File location where is the training file is located
                Output: Nothing
                On Failure: Raise Exception
    
                Written By: Suraj Joshi
                Version: 1.0
                Revisions: None
    
            """
            self.file_location = file_location
            self.log = logger

        except Exception as e:
            self.log.warning('Exception occurred while class initialization in data_preprocessing {}'.format(e))
            raise Exception

    def transform_text(self, text):
        """
            Method Name:transform_text
            Description:It will make the data ready for the training completely data preprocessing for NLP
                        like,
                        Lower case
                        Tokenization
                        Removing special characters
                        Removing stop words and punctuation
                        Stemming

            Input:a string
            Output: string
            On Failure: Raise Exception

            Written By: Suraj Joshi
            Version: 1.0
            Revisions: None

        """

        try:
            text = text.lower()  # Converting the text to lower case
            text = nltk.word_tokenize(text)  # word tokenization

            y = []
            for i in text:
                if i.isalnum():
                    y.append(i)  # now the text is in list type
                    # we are taking only the alpha numeric words in our text
            text = y.copy()
            y.clear()
            for i in text:
                if i not in nltk.corpus.stopwords.words('english') and i not in string.punctuation:
                    y.append(i)
                    # we are avoiding the punctuation character and stopwords which might be present in our list

            text = y.copy()
            y.clear()

            for i in text:
                y.append(ps.stem(i))

            return " ".join(y)

        except Exception as e:
            self.log.warning('Exception occurred inside transform_text in data_preprocessing {}'.format(e))
            raise Exception

    def start_preprocessing(self):
        """
            Method Name:start_preprocessing
            Description:Simply calls the method of the class
            Input:Nothing
            Output: dataframe
            On Failure: Raise Exception

            Written By: Suraj Joshi
            Version: 1.0
            Revisions: None

        """
        df = pd.read_csv(self.file_location, encoding='latin1')

        # Removing 3rd,4th and 5th column from the dataframe
        df.drop(columns=['Id', 'V1', 'V2', 'V3'], inplace=True)

        # Renaming columns
        # df.rename(columns={'v1': 'target', 'v2': 'text'}, inplace=True)

        # Handling target column y converting ham into 0 and spam into 1
        encoder = LabelEncoder()
        df['target'] = encoder.fit_transform(df['target'])
        # o is for ham and 1 is for spam

        # remove duplicates
        df = df.drop_duplicates(keep="first")

        # Dropping null values
        df.dropna(inplace=True)

        # Word Preprocessing
        df['transformed_text'] = df['text'].apply(self.transform_text)

        # Word Vectorization using tfidf and converting the dataframe into X and y
        X = tfidf.fit_transform(df['transformed_text']).toarray()
        y = df['target'].values

        pickle.dump(tfidf, open('tfidf.pickle', 'wb'))
        return X, y
