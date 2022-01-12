# Spam-Ham_Classifier_Project_2
The increased number of unsolicited emails known as spam has necessitated the development of increasingly reliable and robust antispam filters. Recent machine learning approaches have been successful in detecting and filtering spam emails. I need to classify Spam or ham from the dataset which is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged according being ham (legitimate) or spam. 


# Approach
The main goal is to classify the message type as Spam or Ham.

## Data Collection :
####                The data is collected from UCI .
####                  The data has 4 columns V1,V2,V3,V4
####                  V1 tells us the message type and V2 column is for message while V3 and V4 are not important.
####                  Link: https://archive.ics.uci.edu/ml/datasets/sms+spam+collection  



## Text pre-processing in V2 Column:
 ####                              Text Preprocessing is a main step in NLP projects, Steps I did are
####                                  1)Converting the message into lower case.
####                                  2)Avoiding punctuation character and stopwords which might be present in the messages.
####                                  3)Now the final part comes which is vectorization , we are achieving this using tf-idf vectorizer provided by sklearn.

       
       

## Model Creation:
Model Creation is a crucial part of Machine learning project.Firstly I experimented using different Classification models that are
SVC,RandomForestClassifier,XGBClassifier, Multinomial Naive Bayes and upon experimenting i obtain that MNB is performing better than other classifiers
                

## Model Saving:
I saved my model using pickle as model.pickle

## Webpage:
Inside the webpage you will be able to see a big white box.There u have to type the message and then click on Predict button.
Message type will be shown at the bottom of webpage.

# Project Interface
#### I have deployed this model to Amazon Web Services (AWS)
#### Link:http://ec2-3-140-241-66.us-east-2.compute.amazonaws.com:5000/
##### User Interface
![ec2-3-140-241-66 us-east-2 compute amazonaws com_5000_](https://user-images.githubusercontent.com/90147205/149150718-6e0ccdb7-18e3-4a83-ab32-934bcf91eb16.png)


# Technologies Used
1. Python
2. Sklearn
3. MNB
4. Html,Css
5. Pandas,Numpy
6. Amazon Web Services
7. Flask and others

### Check out HLD,LLD for more info

### Help Me improve
Hello if you find any bug please consider raising issue. I will address them asap!
