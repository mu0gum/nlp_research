from gensim.models import word2vec
import CommonUtil


class Recommandation:
    def __init__(self):
        pass

    # TODO : 로직 개선
    def get_recommand_message(self, feature_dict):

        feature_list = list(feature_dict.values())

        model = word2vec.Word2Vec.load('instagram_model_20181030')
        # learn_result = model.most_similar(positive=feature_list)
        learn_result = model.most_similar(positive=['엄마', '생신', '선물'])

        recommand_present_list = []

        for item, similar in learn_result:
            if CommonUtil.get_is_present(item):
                recommand_present_list.append(item)

        return '빅데이터 추천 결과입니다! ' + ','.join(recommand_present_list) + ' 어떠신가요?'
