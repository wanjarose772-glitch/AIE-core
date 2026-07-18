import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import Dashboard from "./pages/Dashboard";

export default function App() {

    return (

        <div className="flex h-screen bg-slate-950">

            <Sidebar />

            <div className="flex flex-col flex-1">

                <Header />

                <Dashboard />

            </div>

        </div>

    );

}