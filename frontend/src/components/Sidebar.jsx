export default function Sidebar() {

    const menu = [
        "Dashboard",
        "Radar",
        "Momentum",
        "Smart Money",
        "History",
        "Settings",
    ];

    return (
        <aside className="w-64 bg-slate-950 border-r border-slate-800 min-h-screen">

            <div className="p-8">

                <h2 className="text-xl text-white font-bold">
                    AIE
                </h2>

            </div>

            <nav>

                {menu.map(item => (

                    <div
                        key={item}
                        className="px-8 py-4 text-slate-300 hover:bg-slate-800 hover:text-white cursor-pointer transition"
                    >
                        {item}
                    </div>

                ))}

            </nav>

        </aside>
    );
}