import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listProjects } from '../utils/api'
import type { Project } from '../types'
import { PlusCircle, FolderOpen } from 'lucide-react'

export default function HomePage() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listProjects().then(setProjects).finally(() => setLoading(false))
  }, [])

  return (
    <div className="p-8 max-w-5xl">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-white mb-2">AI Governance Dashboard</h1>
        <p className="text-slate-400 text-sm">
          Map your project proposals against PIA, Supplier, Agentic, and Cyber governance requirements.
          Identify gaps, assess risk, and generate compliance reports.
        </p>
      </div>

      {/* Stats row */}
      <div className="grid grid-cols-4 gap-4 mb-8">
        {[
          { label: 'Total Projects', value: projects.length, color: 'text-indigo-400' },
          { label: 'Governance Domains', value: 10, color: 'text-cyan-400' },
          { label: 'Assessment Questions', value: '100+', color: 'text-emerald-400' },
          { label: 'Standards Mapped', value: 5, color: 'text-amber-400' },
        ].map(({ label, value, color }) => (
          <div key={label} className="card">
            <div className={`text-3xl font-bold ${color}`}>{value}</div>
            <div className="text-slate-400 text-xs mt-1">{label}</div>
          </div>
        ))}
      </div>

      {/* Quick actions */}
      <div className="flex gap-3 mb-8">
        <Link to="/projects/new" className="btn-primary flex items-center gap-2">
          <PlusCircle size={16} /> New Assessment
        </Link>
        <Link to="/projects" className="btn-secondary flex items-center gap-2">
          <FolderOpen size={16} /> View Projects
        </Link>
      </div>

      {/* Governance pathway */}
      <div className="card mb-8">
        <h2 className="font-semibold text-slate-200 mb-4">Governance Pathway</h2>
        <div className="flex items-center gap-2">
          {['Register', 'Assess', 'Review', 'Align', 'Operate'].map((phase, i) => (
            <div key={phase} className="flex items-center gap-2">
              <div className="flex flex-col items-center">
                <div className="w-8 h-8 rounded-full bg-indigo-600 flex items-center justify-center text-xs font-bold text-white">
                  {i + 1}
                </div>
                <div className="text-xs text-slate-400 mt-1">{phase}</div>
              </div>
              {i < 4 && <div className="w-8 h-px bg-slate-700 mb-4" />}
            </div>
          ))}
        </div>
      </div>

      {/* Recent projects */}
      {loading ? (
        <div className="text-slate-500 text-sm">Loading projects...</div>
      ) : projects.length === 0 ? (
        <div className="card text-center py-12">
          <FolderOpen className="mx-auto text-slate-600 mb-3" size={36} />
          <div className="text-slate-400 mb-4">No projects yet</div>
          <Link to="/projects/new" className="btn-primary">Start your first assessment</Link>
        </div>
      ) : (
        <div>
          <h2 className="font-semibold text-slate-200 mb-3">Recent Projects</h2>
          <div className="space-y-2">
            {projects.slice(0, 5).map(p => (
              <Link
                key={p.id}
                to="/projects"
                className="card flex items-center justify-between hover:border-indigo-700 transition-colors"
              >
                <div>
                  <div className="font-medium text-slate-200">{p.name}</div>
                  <div className="text-xs text-slate-500">{p.team} · {new Date(p.created_at).toLocaleDateString()}</div>
                </div>
                <span className="text-xs text-slate-500">→</span>
              </Link>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
