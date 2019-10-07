# -*- coding: utf-8 -*-
from gensim.models import word2vec
from sklearn.manifold import TSNE
# import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import gensim.models as g
import pandas as pd
import PresenTALKUtil
from operator import itemgetter
from collections import OrderedDict


class W2VRecommender:

    def __init__(self, model_path):
        if model_path != '':
            self.model = g.Word2Vec.load(model_path)

    def train_word2vec(self, prefix, file_path, params):
        data = word2vec.LineSentence(file_path)
        self.model = word2vec.Word2Vec(data, size=params['size'], window=params['window'], min_count=params['min_count']
                                       , workers=4, iter=30, sg=1)
        self.model.save('rec_model_{0}_{1}_{2}_{3}_30'.format(prefix, params['size'], params['window']
                                                              , params['min_count']))

    def analyze_data(self, file_path):
        present_list = PresenTALKUtil.get_all_present_list()
        present_target = PresenTALKUtil.get_feature_target()
        present_purpose = PresenTALKUtil.get_feature_purpose()

        data_file = open(file_path, 'r', encoding='utf-8')
        lines = data_file.readlines()

        word_count_dict = dict()

        for line in lines:
            word_list = line.split(' ')

            for word in word_list:
                word = word.replace('\n', '')
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

        # word Count
        sorted_list = sorted(word_count_dict.items(), key=itemgetter(1), reverse=True)
        # for key, value in sorted_list:
        #     print(key, value)

        # present word count
        for key, value in sorted_list:
            if key in present_list:
                print(key, value)

        # target word count
        for key, value in sorted_list:
            if key in present_target:
                print(key, value)

        # purpose word count
        for key, value in sorted_list:
            if key in present_purpose:
                print(key, value)

    def visualization_data(self, word_count):
        font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
        font_manager.FontProperties(fname=font_path)
        rc('font', family="NanumGothic")

        vocab = list(self.model.wv.vocab)
        X = self.model[vocab]

        tsne = TSNE(n_components=2)
        X_tsne = tsne.fit_transform(X[:word_count, :])

        df = pd.DataFrame(X_tsne, index=vocab[:word_count], columns=['x', 'y'])

        fig = plt.figure()
        fig.set_size_inches(40, 20)
        ax = fig.add_subplot(1, 1, 1)

        ax.scatter(df['x'], df['y'])

        for word, pos in df.iterrows():
            ax.annotate(word, pos, fontsize=10)
        plt.show()
