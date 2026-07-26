"""
Whale Reputation Engine
"""


class WhaleEngine:

    def analyze(self, whale):

        score = 0

        score += whale.buy_count * 8

        score -= whale.sell_count * 3

        score += whale.net_position / 1000

        whale.confidence = round(score)

        if score >= 300:

            whale.grade = "LEGEND"

        elif score >= 200:

            whale.grade = "ELITE"

        elif score >= 120:

            whale.grade = "STRONG"

        elif score >= 60:

            whale.grade = "GOOD"

        else:

            whale.grade = "UNKNOWN"

        return whale