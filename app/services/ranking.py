class RankingService:

    def rank(self, analyses):

        return sorted(
            analyses,
            key=lambda x: (
                x["analysis"]["alpha"].score,
                x["analysis"]["confidence"].score,
            ),
            reverse=True,
        )