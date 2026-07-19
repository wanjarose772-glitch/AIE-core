import { useEffect, useState } from "react";
import axios from "axios";
import api from "../services/api";

export default function Dashboard() {
    const [hawk, setHawk] = useState([]);

useEffect(() => {

    async function loadHawk() {

        try {

            const response = await axios.get(
                "http://127.0.0.1:8000/hawk"
            );

            setHawk(response.data);

        } catch (err) {

            console.log(err);

        }

    }

    loadHawk();

}, []);

    const [intel, setIntel] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        loadIntel();

        const timer = setInterval(loadIntel, 30000);

        return () => clearInterval(timer);

    }, []);

    async function loadIntel() {

        try {

            const response = await api.get("/intel");

            setIntel(response.data);

            setLoading(false);

        }

        catch (err) {

            console.error(err);

        }

    }

    if (loading) {

        return (

            <div className="flex items-center justify-center h-screen text-white">

                Loading Intelligence...

            </div>

        );

    }

    const top = intel[0];

    return (

        <main className="flex-1 bg-slate-950 text-white p-8">
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

                        {intel.length}

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

                        {intel.map((coin) => (

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
            coin.recommendation.toLowerCase().includes("buy")
                ? "bg-green-600 text-white px-3 py-1 rounded-full"
                : coin.recommendation.toLowerCase().includes("watch")
                ? "bg-yellow-500 text-black px-3 py-1 rounded-full"
                : "bg-red-600 text-white px-3 py-1 rounded-full"
        }
    >
        {coin.recommendation}
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