import glob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')

directory = "diary/"
extension = ".txt"
filepaths = sorted(glob.glob(f"{directory}*{extension}"))
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

dates = [path[len(directory):-len(extension)] for path in filepaths]
