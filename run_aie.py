from app.services.scanner import MarketScanner
from app.services.aie_core import AIECore
from app.services.ranking import RankingService


def main():

    scanner = MarketScanner()
    aie = AIECore()
    ranking = RankingService()

    print("=" * 70)
    print("AIE LIVE MARKET ANALYSIS")
    print("=" * 70)

    tokens = scanner.scan()

    results = []

    for token in tokens:

        analysis = aie.analyze(token)

        results.append(
            {
                "token": token,
                "analysis": analysis,
            }
        )

    results = ranking.rank(results)

    print("\n" + "=" * 70)
    print("TOP OPPORTUNITIES")
    print("=" * 70)

    for position, item in enumerate(results, start=1):

        token = item["token"]
        analysis = item["analysis"]

        print()
        print(f"#{position} {token['symbol']} ({token['name']})")
        print("-" * 55)

        print(f"Alpha          : {analysis['alpha'].score}")
        print(f"Risk           : {analysis['risk'].level}")
        print(f"Confidence     : {analysis['confidence'].score}")
        print(f"Momentum       : {analysis['momentum'].score}")
        print(f"Opportunity    : {analysis['opportunity'].score}")
        print(f"Conviction     : {analysis['conviction'].score}")
        print(f"Trend          : {analysis['trend'].score}")
        print(f"Decision       : {analysis['conviction'].action}")

        print("\nMomentum")

        if analysis["momentum"].reasons:
            for reason in analysis["momentum"].reasons:
                print(f"  ✓ {reason}")
        else:
            print("  None")

        print("\nOpportunity")

        if analysis["opportunity"].reasons:
            for reason in analysis["opportunity"].reasons:
                print(f"  ✓ {reason}")
        else:
            print("  None")

        print("\nTrend")

        if analysis["trend"].reasons:
            for reason in analysis["trend"].reasons:
                print(f"  ✓ {reason}")
        else:
            print("  First observation")

        print("\nConviction")

        if analysis["conviction"].reasons:
            for reason in analysis["conviction"].reasons:
                print(f"  ✓ {reason}")
        else:
            print("  None")

        print("\nSmart Wallets")

        wallets = analysis.get("wallets", [])

        if wallets:

            for wallet in wallets:

                print(
                    f"  {wallet.address} | "
                    f"{wallet.grade} | "
                    f"{wallet.confidence:.1f}"
                )

        else:

            print("  None detected")

        print("\nWhales")

        whales = analysis.get("whales", [])

        if whales:

            for whale in whales:

                print(
                    f"  {whale.address} | "
                    f"{whale.grade} | "
                    f"{whale.confidence:.1f}"
                )

        else:

            print("  None detected")


if __name__ == "__main__":
    main()