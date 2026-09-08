import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {
    const [hawk, setHawk] = useState([]);
    const [intel, setIntel] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        let active = true;

        async function refreshDashboard() {
            try {
                const [intelResponse, hawkResponse] = await Promise.all([
                    api.get("/intel"),
                    api.get("/hawk"),
                ]);

                if (!active) return;
                setIntel(Array.isArray(intelResponse.data) ? intelResponse.data : []);
                setHawk(Array.isArray(hawkResponse.data) ? hawkResponse.data : []);
                setError("");
            } catch (err) {
                if (active) {
                    setError("Live data is temporarily unavailable. Retrying automatically.");
                }
                console.error("Dashboard refresh failed", err);
            } finally {
                if (active) setLoading(false);
            }
        }

        refreshDashboard();
        const timer = setInterval(refreshDashboard, 30000);

        return () => {
            active = false;
            clearInterval(timer);
        };

    }, []);

    if (loading) {

        return (

            <div className="flex items-center justify-center h-screen text-white">

                Loading Intelligence...

            </div>

        );

    }

    // The new-launch scanner is the primary source for early opportunities.
    // The deeper intelligence report augments it when available, but an empty
    // report must never hide valid live-launch candidates.
    const candidates = hawk.length > 0 ? hawk : intel;
    const rankedCandidates = [...candidates].sort(
        (left, right) => (right.alpha_score ?? 0) - (left.alpha_score ?? 0)
    );
    const top = rankedCandidates[0] ?? {
        ticker: "No live opportunities yet",
        name: "AIE is waiting for the next qualifying launch.",
        price: "—",
        alpha_score: 0,
        confidence: 0,
        recommendation: "WATCH",
    };

    return (

        <main className="flex-1 bg-slate-950 text-white p-8">
            {error && (
                <div className="mb-6 rounded-xl border border-amber-500/40 bg-amber-500/10 px-4 py-3 text-amber-200">
                    {error}
                </div>
            )}
            <div className="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl border border-slate-700 p-6 mb-8">

    <h2 className="text-3xl font-bold">

        🧠 GOOD MORNING, ROSE

    </h2>

    <p className="text-slate-400 mt-2">

        Here's today's intelligence briefing.

    </p>

    <div className="grid grid-cols-4 gap-6 mt-6">

        <div>

            <p className="text-slate-400">

                Market Mood

            </p>

            <h3 className="text-2xl font-bold text-emerald-400">

                Bullish 🟢

            </h3>

        </div>

        <div>

            <p className="text-slate-400">

                Top Opportunity

            </p>

            <h3 className="text-2xl font-bold">

                {top.ticker}

            </h3>

        </div>

        <div>

            <p className="text-slate-400">

                ASILI Rating

            </p>

            <h3 className="text-2xl font-bold text-emerald-400">

                PRIME 👑

            </h3>

        </div>

        <div>

            <p className="text-slate-400">

                Expected Hold

            </p>

            <h3 className="text-2xl font-bold">

                2–5 Days

            </h3>

        </div>

    </div>

</div>

            <div className="grid grid-cols-2 gap-6">

                <div className="bg-slate-900 rounded-xl p-6 border border-slate-800">

                    <h2 className="text-xl font-bold mb-4">

                        🔥 Opportunity of the Day

                    </h2>

                    <h1 className="text-4xl font-bold">

                        {top.ticker}

                    </h1>

                    <p className="mt-4 text-slate-400">

                        {top.name}

                    </p>

                    <div className="mt-6 space-y-2">

                        <p>Price: ${top.price}</p>

                        <div className="mt-6">

    <p className="mb-2 text-slate-300">
        Alpha Score
    </p>

    <div className="w-full bg-slate-800 rounded-full h-4">

        <div
            className="bg-emerald-500 h-4 rounded-full"
            style={{
                width: `${top.alpha_score}%`,
            }}
        />

    </div>

    <p className="mt-1 mb-5 text-emerald-400">

        {top.alpha_score}/100

    </p>

    <p className="mb-2 text-slate-300">

        Confidence

    </p>

    <div className="w-full bg-slate-800 rounded-full h-4">

        <div
            className="bg-cyan-500 h-4 rounded-full"
            style={{
                width: `${top.confidence}%`,
            }}
        />

    </div>

    <p className="mt-1">

        {top.confidence}%

    </p>
    <div className="mt-8">

    <h3 className="text-slate-300 mb-3">

        ASILI Rating

    </h3>

    <div
        className={
            top.alpha_score >= 90
                ? "bg-emerald-600 text-white px-5 py-3 rounded-xl inline-block font-bold"
                : top.alpha_score >= 75
                ? "bg-blue-600 text-white px-5 py-3 rounded-xl inline-block font-bold"
                : top.alpha_score >= 60
                ? "bg-amber-500 text-black px-5 py-3 rounded-xl inline-block font-bold"
                : "bg-red-600 text-white px-5 py-3 rounded-xl inline-block font-bold"
        }
    >

        {
            top.alpha_score >= 90
                ? "👑 ASILI PRIME"
                : top.alpha_score >= 75
                ? "🔷 ASILI WATCH"
                : top.alpha_score >= 60
                ? "⚡ ASILI SPECULATIVE"
                : "🚫 ASILI REJECT"
        }

    </div>

</div>
<div className="mt-8">

    <h3 className="text-slate-300">

        Why AIE Likes This

    </h3>

    <ul className="mt-3 space-y-2 text-slate-400">

        <li>✅ High Alpha Score</li>

        <li>✅ Strong Confidence</li>

        <li>✅ Healthy Liquidity</li>

        <li>✅ Positive Momentum</li>

    </ul>

</div>

</div>

                    </div>

                </div>

                <div className="bg-slate-900 rounded-xl p-6 border border-slate-800">

                    <h2 className="text-xl font-bold">

                        📡 Live Intelligence

                    </h2>

                    <h1 className="text-6xl mt-10">

                        {rankedCandidates.length}

                    </h1>

                    <p className="text-slate-400">

                        Active Opportunities

                    </p>

                </div>

            </div>
            <div className="mt-10 bg-slate-900 rounded-xl border border-slate-800 p-6">

    <h2 className="text-2xl font-bold mb-6">

        🏆 Project HAWK — New Launch Scanner

    </h2>

    <div className="space-y-4">

        {hawk.map((coin) => (

            <div
                key={coin.ticker}
                className="bg-slate-800 rounded-xl p-5 flex justify-between items-center"
            >

                <div>

                    <h3 className="text-xl font-bold">

                        {coin.ticker}

                    </h3>

                    <p className="text-slate-400">

                        Alpha {coin.alpha_score}

                    </p>

                    <p className="text-slate-400">

                        Confidence {coin.confidence}%

                    </p>

                </div>

                <div>

                    <span className="bg-emerald-600 px-4 py-2 rounded-xl font-bold">

                        {coin.rating}

                    </span>

                </div>

            </div>

        ))}

    </div>

</div>

            <div className="mt-10 bg-slate-900 rounded-xl border border-slate-800 p-6">

                <h2 className="text-xl font-bold mb-5">

                    Live Intelligence Feed

                </h2>

                <table className="w-full">

                    <thead>

                        <tr className="text-slate-500 border-b border-slate-700">

    <th className="text-left py-4">Ticker</th>

    <th className="text-center">Alpha</th>

    <th className="text-center">Confidence</th>

    <th className="text-center">Rating</th>

</tr>

                    </thead>

                    <tbody>

                        {rankedCandidates.map((coin) => (

                            <tr
    key={coin.address}
    className="border-b border-slate-800 hover:bg-slate-800 transition duration-200"
>

                                <td className="py-4 font-semibold text-white">

    {coin.ticker}

</td>

                                <td className="text-center">

    <span className="text-emerald-400 font-bold">

        {coin.alpha_score}

    </span>

</td>

                                <td className="text-center">

    <span className="text-cyan-400 font-bold">

        {coin.confidence}

    </span>

</td>

                                <td>

    <span
        className={
            (coin.recommendation ?? coin.rating ?? "").toLowerCase().includes("prime") ||
            (coin.recommendation ?? coin.rating ?? "").toLowerCase().includes("buy")
                ? "bg-green-600 text-white px-3 py-1 rounded-full"
                : (coin.recommendation ?? coin.rating ?? "").toLowerCase().includes("watch") ||
                  (coin.recommendation ?? coin.rating ?? "").toLowerCase().includes("speculative")
                ? "bg-yellow-500 text-black px-3 py-1 rounded-full"
                : "bg-red-600 text-white px-3 py-1 rounded-full"
        }
    >
        {coin.recommendation ?? coin.rating ?? "WATCH"}
    </span>

</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </main>

    );

}
