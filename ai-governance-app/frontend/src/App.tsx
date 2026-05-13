import { Routes, Route, NavLink } from 'react-router-dom'
import { LayoutDashboard, FolderOpen, PlusCircle } from 'lucide-react'
import HomePage from './pages/HomePage'
import ProjectsPage from './pages/ProjectsPage'
import NewProjectPage from './pages/NewProjectPage'
import AssessmentPage from './pages/AssessmentPage'

export default function App() {
  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <nav className="w-56 bg-slate-900 border-r border-slate-800 flex flex-col p-4 shrink-0">
        <div className="mb-8">
          <div className="text-xs text-indigo-400 font-semibold uppercase tracking-widest mb-1">AI Governance</div>
          <div className="text-slate-300 font-bold text-sm leading-tight">Mapping Tool</div>
        </div>
        <div className="space-y-1 flex-1">
          <NavLink
            to="/"
            end
            className={({ isActive }) =>
              `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm transition-colors ${isActive ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800'}`
            }
          >
            <LayoutDashboard size={16} /> Dashboard
          </NavLink>
          <NavLink
            to="/projects"
            className={({ isActive }) =>
              `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm transition-colors ${isActive ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800'}`
            }
          >
            <FolderOpen size={16} /> Projects
          </NavLink>
          <NavLink
            to="/projects/new"
            className={({ isActive }) =>
              `flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm transition-colors ${isActive ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800'}`
            }
          >
            <PlusCircle size={16} /> New Project
          </NavLink>
        </div>
        <div className="text-xs text-slate-600 mt-4">Internal use only</div>
      </nav>

      {/* Main content */}
      <main className="flex-1 overflow-auto">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/projects" element={<ProjectsPage />} />
          <Route path="/projects/new" element={<NewProjectPage />} />
          <Route path="/assessment/:assessmentId" element={<AssessmentPage />} />
        </Routes>
      </main>
    </div>
  )
}
