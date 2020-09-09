from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class DocumentSimilarity:

    def __init__(self, texts):
        self.texts = texts

    def calculate_document_similarity(self):
        # Create the Document Term Matrix
        vector = CountVectorizer(stop_words='english')
        sparse_matrix = vector.fit_transform(self.texts)

        # Interpret the document term matrix.
        document_term_matrix = sparse_matrix.todense()
        df = pd.DataFrame(document_term_matrix,
                          columns=vector.get_feature_names())
        # calculate cosine similarity and convert to string
        return str(cosine_similarity(df, df))