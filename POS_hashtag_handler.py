import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("D:/Courses/Data Science Specialization/Datasets/airline-twitter-sentiment/separated_text_train.csv")
sample_text = state_union.raw("D:/Courses/Data Science Specialization/Datasets/airline-twitter-sentiment/separated_text_test.csv")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

g = open("D:/Courses/Data Science Specialization/Datasets/airline-twitter-sentiment/pos_tagged.csv","w")

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            g.write("%s\n" % tagged)
            g.write("\n\n")

    except Exception as e:
            print(str(e))


process_content()

g.close()
