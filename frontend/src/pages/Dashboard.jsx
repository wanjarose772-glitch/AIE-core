import { useEffect, useState } from "react";
import api from "../services/api";

export default function Dashboard() {

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

                        <p>Alpha Score: {top.alpha_score}</p>

                        <p>Confidence: {top.confidence}</p>

                        <p>{top.recommendation}</p>

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

                <h2 className="text-xl font-bold mb-5">

                    Live Intelligence Feed

                </h2>

                <table className="w-full">

                    <thead>

                        <tr className="text-slate-400">

                            <th className="text-left pb-3">Ticker</th>

                            <th className="text-left">Alpha</th>

                            <th className="text-left">Confidence</th>

                            <th className="text-left">Recommendation</th>

                        </tr>

                    </thead>

                    <tbody>

                        {intel.map((coin) => (

                            <tr
                                key={coin.address}
                                className="border-t border-slate-800"
                            >

                                <td className="py-3">

                                    {coin.ticker}

                                </td>

                                <td>{coin.alpha_score}</td>

                                <td>{coin.confidence}</td>

                                <td>{coin.recommendation}</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </main>

    );

}