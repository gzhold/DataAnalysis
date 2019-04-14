from sklearn.feature_extraction.text import TfidfVectorizer



tfidf_vec = TfidfVectorizer()

documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]
tfidf_matrix = tfidf_vec.fit_transform(documents)

# 输出文档中所有不重复的词：
print('不重复的词:', tfidf_vec.get_feature_names())

print('每个单词的 ID:', tfidf_vec.vocabulary_)

#输出每个单词在每个文档中的 TF-IDF 值，向量里的顺序是按照词语的 id 顺序来的
print('每个单词的 tfidf 值:', tfidf_matrix.toarray())