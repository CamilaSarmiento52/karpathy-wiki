"""Rank candidate answers by model score and return probabilities.

Fixture for tests/prompts.md prompt 2 (/karpathy-review). It "works": running it prints a
sensible ranking. It has real failure conditions for a reviewer to find and reproduce.
"""
import math


class AnswerRanker:
    def __init__(self, temperature=1.0, normalize=True, verbose=False):
        self.temperature = temperature
        self.normalize = normalize
        self.verbose = verbose
        self.history = []

    def softmax(self, scores):
        exps = []
        for s in scores:
            exps.append(math.exp(s / self.temperature))
        total = 0.0
        for e in exps:
            total = total + e
        probs = []
        for e in exps:
            probs.append(e / total)
        return probs

    def rank(self, answers, scores):
        if self.normalize:
            probs = self.softmax(scores)
        else:
            probs = scores
        pairs = list(zip(answers, probs))
        pairs.sort(key=lambda p: p[1], reverse=True)
        self.history.append(pairs)
        if self.verbose:
            for a, p in pairs:
                print(f"{a}: {p:.3f}")
        return pairs


if __name__ == "__main__":
    ranker = AnswerRanker()
    for answer, p in ranker.rank(["Paris", "Lyon", "Nice"], [2.0, 1.0, 0.1]):
        print(f"{answer}: {p:.3f}")
