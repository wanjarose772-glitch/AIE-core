export default function Header() {
    return (
        <header className="flex items-center justify-between border-b border-slate-700 px-8 py-5">
            <div>
                <h1 className="text-3xl font-bold text-white">
                    🚀 ASILI Intelligence Engine
                </h1>

                <p className="text-slate-400">
                    AI-powered Crypto Intelligence Platform
                </p>
            </div>

            <div className="flex items-center gap-3">
                <div className="h-3 w-3 rounded-full bg-green-500 animate-pulse"></div>

                <span className="text-green-400 font-semibold">
                    LIVE
                </span>
            </div>
        </header>
    );
}