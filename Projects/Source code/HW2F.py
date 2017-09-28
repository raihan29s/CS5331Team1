import unicodecsv
import random
import operator
import math
import csv

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()


# tweet categorization i.e. rescue/non-rescue tweet
def categorize_tweet_data (TD_file):
    categorized_TD_file = 'PTD.csv'
    bag_of_words = ['rescue','harvey', 'relief', 'save','hurricane']
    with open(TD_file, encoding='ISO-8859-1') as fin, open(categorized_TD_file, 'w') as fout:                                                                        
        reader = csv.reader(fin)                                                                                                                               
        writer = csv.writer(fout)                                                                                                                                              
        i = next(reader)
        i.append("Category")
        writer.writerow(i)
        #print (i)
        for line in reader:
            text = line[1]
            if [word for word in text.split() if word in bag_of_words]:
                line.append("rescue")
            else:
                line.append("non-rescue")
            writer.writerow(line)
    fout.close()
    return categorized_TD_file


# Term document matrix generation
def term_doc_matrix(categorized_twitter_data):
    with open(categorized_twitter_data, encoding='ISO-8859-1') as fin:
        tweets = []
        reader = csv.reader(fin)
        for line in reader:
            tweets.append(line[1])

        vectorizer = CountVectorizer (reader, analyzer='word', stop_words='english', max_features=7)

        dtm = vectorizer.fit_transform(tweets)                                                                                                                      

        analyze = vectorizer.build_analyzer()

        vocab = vectorizer.get_feature_names()

        dtm=dtm.toarray()

    doc_term_matrix = 'doc_term_matrix.csv'
    with open(doc_term_matrix, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(dtm)
        output.close()
        
        print ("\n\nDocument Term Matrix:\n")
        print (dtm)  
        print ("\n\nVocabulary:\n")
        print (vocab)

    return doc_term_matrix

#getdata() function definition
def getdata(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.reader(f)
        return list(reader)
 
#random train test data split function definition
def shuffle(i_data):
    random.shuffle(i_data)
    train_data = i_data[:int(0.7*30)]
    test_data = i_data[int(0.7*30):]
    return train_data, test_data
 
def euclideanDist(x, xi):
    d = 0.0
    for i in range(len(x)-1):
        d += pow((float(x[i])-float(xi[i])),2)  #euclidean distance
    d = math.sqrt(d)
    return d
 
#KNN prediction and model training
def knn_predict(test_data, train_data, k_value):
    for i in test_data:
        eu_Distance =[]
        knn = []
        rescue = 0
 
        no_rescue = 0
        for j in train_data:
            eu_dist = euclideanDist(i, j)
            eu_Distance.append((j[9], eu_dist))
            eu_Distance.sort(key = operator.itemgetter(1))
            knn = eu_Distance[:k_value]
            for k in knn:
                if k[0] =='1':
                    rescue += 1
                else:
                    no_rescue +=1
        if rescue > no_rescue:
            i.append('1')
        elif rescue < no_rescue:
            i.append('0')
 
#Accuracy calculation function
def accuracy(test_data):
    correct = 0
    for i in test_data:
        if i[9] == i[10]:
            correct += 1
    accuracy = float(correct)/len(test_data) *100  #accuracy 
    return accuracy


categorized_TD_file = categorize_tweet_data ('TD.csv')
doc_term_mat = term_doc_matrix(categorized_TD_file)
dataset = getdata(doc_term_mat)  #getdata function call with csv file as parameter
train_dataset, test_dataset = shuffle(dataset) #train test data split
K = 3             # Assumed K value
knn_predict(test_dataset, train_dataset, K)   
#print (test_dataset)
print ("\n\nAccuracy : ",accuracy(test_dataset))
print ("\n\n")
