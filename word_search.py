"""

A researcher has gathered thousands of news articles.
But she wants to focus her attention on articles including a specific word.
Complete the function below to help her filter her list of articles.
"""

def word_search(documents, keyword):
    # list holds the indices of matching documents
    indices = []
    # iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # split the string doc into a list of words
        tokens = doc.split()
        # make a transformed list whee we 'normalize' each word to facilitate matching
        # periods and commas are removed from the end of each word
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # is there a match? if so, update the list
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices