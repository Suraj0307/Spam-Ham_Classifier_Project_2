import pickle
from sklearn.naive_bayes import MultinomialNB


class model_building:
    def __init__(self, X, y, logger):
        self.X = X
        self.y = y
        self.log = logger

    def model_training(self):
        """
            Method Name:model_training
            Description:It will create a object of class MultinomialNB and fit to the data

            Input:a string
            Output: string
            On Failure: Raise Exception

            Written By: Suraj Joshi
            Version: 1.0
            Revisions: None

        """
        try:
            model = MultinomialNB()
            model.fit(self.X, self.y)
            return model
        except Exception as e:
            self.log.warning('Exception occurred inside model_training in model_building {}'.format(e))
            raise Exception

    def save_model(self, model_to_save):
        """
            Method Name:save_model
            Description:It will simply save the model using pickle in a filename called model.pickle

            Input:a string
            Output: string
            On Failure: Raise Exception

            Written By: Suraj Joshi
            Version: 1.0
            Revisions: None

        """
        try:
            model_filename = 'model.pickle'
            pickle.dump(model_to_save, open(model_filename, 'wb'))
            return model_filename

        except Exception as e:
            self.log.warning('Exception occurred inside save_model in model_building {}'.format(e))
            raise Exception

    def start_model_building(self):
        model = self.model_training()
        filename = self.save_model(model)
        return filename
