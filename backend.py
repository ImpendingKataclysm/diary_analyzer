import glob
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))
analyzer = SentimentIntensityAnalyzer()
pos_scores = []
neg_scores = []


def get_scores(text, polarity):
    scores = analyzer.polarity_scores(text)
    return scores[polarity]


for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    pos_scores.append(get_scores(content, "pos"))
    neg_scores.append(get_scores(content, "neg"))
