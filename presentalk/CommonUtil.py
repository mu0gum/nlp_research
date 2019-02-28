# -*- coding: utf-8 -*-
from gensim.models import word2vec
import PresenTALKUtil
import pickle

with open('wiki.pickle', 'rb') as f:
    wiki_model = pickle.load(f)


def get_is_present(word):
    is_present = False;

    present_list = PresenTALKUtil.get_present_list()

    for present in present_list:
        if present in word:
            is_present = True
            break
        else:
            if word in wiki_model.wv.vocab:
                if wiki_model.similarity('선물', word) > 0.3:
                    is_present = True
                    break

    return is_present
