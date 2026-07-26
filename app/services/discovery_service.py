from packages.discovery.aggregator import discover_all_launches
from app.services.aie_core import AIECore


class DiscoveryService:

    def __init__(self):
        self.aie = AIECore()

    def intel(self):

        launches = discover_all_launches()

        results = []

        for token in launches:

            analysis = self.aie.analyze(token)

            token["ticker"] = (
                token.get("ticker")
                or token.get("symbol")
                or "UNKNOWN"
            )

            token["name"] = token.get("name", "")
            token["address"] = token.get("address", "")
            token["price"] = token.get("price", 0)

            # -----------------------------
            # Engine Scores
            # -----------------------------

            token["alpha_score"] = analysis["alpha"].score

            token["confidence"] = analysis["confidence"].score

            token["risk"] = analysis["risk"].level

            token["momentum"] = analysis["momentum"].score

            token["opportunity"] = analysis["opportunity"].score

            token["trend"] = analysis["trend"].score

            # -----------------------------
            # Master Score
            # -----------------------------

            master = analysis.get("master_score", {})

            token["aie_score"] = master.get("aie_score", 0)

            token["rating"] = master.get("rating", "UNKNOWN")

            token["recommendation"] = (
                analysis["conviction"].action
            )

            # -----------------------------
            # Smart Money
            # -----------------------------

            token["wallets"] = analysis.get(
                "wallets",
                [],
            )

            token["whales"] = analysis.get(
                "whales",
                [],
            )

            results.append(token)

        results.sort(
            key=lambda x: x["aie_score"],
            reverse=True,
        )

        return results