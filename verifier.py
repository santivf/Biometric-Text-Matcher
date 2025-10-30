import textdistance

def verify_biometric(sample1, sample2, threshold=0.8):
    similarity = 1 - (textdistance.levenshtein.distance(sample1, sample2) / max(len(sample1), len(sample2)))
    return similarity, similarity >= threshold

