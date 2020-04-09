import collections
import math

users_interests = [
    ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
    ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
    ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
    ["R", "Python", "statistics", "regression", "probability"],
    ["machine learning", "regression", "decision trees", "libsvm"],
    ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
    ["statistics", "probability", "mathematics", "theory"],
    ["machine learning", "scikit-learn", "Mahout", "neural networks"],
    ["neural networks", "deep learning", "Big Data", "artificial intelligence"],
    ["Hadoop", "Java", "MapReduce", "Big Data"],
    ["statistics", "R", "statsmodels"],
    ["C++", "deep learning", "artificial intelligence", "probability"],
    ["pandas", "R", "Python"],
    ["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
    ["libsvm", "regression", "support vector machines"]
]


# popular_interest = collections.Counter(interest
#                             for user_interest in users_interests
#                             for interest in user_interest).most_common()

# print(popular_interest)
#
# suggestions = [(interest , frequency)
#                for interest , frequency in popular_interest
#                if interest in ["NoSQL", "MongoDB"]]
#
# print(suggestions)

def dot(v, w):
    return sum(v1 * w1
               for v1, w1 in zip(v, w))


def cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))


unique_interest = list(interest
                          for userInterest in users_interests
                          for interest in userInterest)




print(unique_interest)


def make_user_interest_vector(user_interests):
    return [1 if interest in user_interests else 0
            for interest in unique_interest]


def make_interest_mat(users_interests):
    return [make_user_interest_vector(userInterest)
            for userInterest in users_interests]


# Matrix Transpose
usersInterests = make_interest_mat(users_interests)


itemInterests = [[userIntVector[i]
                 for userIntVector in usersInterests]
                    for i,_ in enumerate(unique_interest)]

item_similarities = [[cosine_similarity(itemInti , itemIntj)
                        for itemIntj in itemInterests]
                        for itemInti in itemInterests]

print(item_similarities)

def mostSimilarItems (item_id) :
    similarities = item_similarities[item_id]
    pairs = [(unique_interest[otherItemId] , similarity)
                for otherItemId , similarity in enumerate(item_similarities[item_id])
                if otherItemId != item_id and similarity > 0]

    return sorted(pairs,
                  key = lambda similarity : similarity[1],
                  reverse=True)

# print(mostSimilarItems(0)[0][0])
def item_suggestion(user_id) :
    sugg = {}
    interests = usersInterests[user_id]
    for intr, isInterested in enumerate(interests) :
        if isInterested == 1 :
            mostSimilarInters = mostSimilarItems(intr)
            for interest, similarity in mostSimilarInters :
                if interest in sugg :
                    sugg[interest] += similarity
                else :
                    sugg[interest] = similarity


    sugg = sorted(sugg.items(),
                  key =lambda similarity : similarity[1],
                  reverse=True)

    return sugg

print(item_suggestion(0))
