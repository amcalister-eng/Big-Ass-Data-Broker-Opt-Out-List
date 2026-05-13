import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listProjects, startAssessment } from '../utils/api'
import type { Project } from '../types'
import { PlusCircle, Play, FolderOpen } from 'lucide-react'

export default function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)
  const [starting, setStarting] = useState<string | null>(null)

  useEffect(() => {
    listProjects().then(setProjects).finally(() => setLoading(false))
  }, [])

  const handleStartAssessment = async (projectId: string, e: React.MouseEvent) => {
    e.preventDefault()
    setStarting(projectId)
    try {
      const assessment = await startAssessment(projectId)
      window.location.href = `/assessment/${assessment.id}`
    } finally {
      setStarting(null)
    }
  }

  return (
    <div className="p-8 max-w-5xl">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-white">Projects</h1>
        <Link to="/projects/new" className="btn-primary flex items-center gap-2">
          <PlusCircle size={16} /> New Assessment
        </Link>
      </div>

      {loading ? (
        <div className="text-slate-500 text-sm">Loading...</div>
      ) : projects.length === 0 ? (
        <div className="card text-center py-16">
          <FolderOpen className="mx-auto text-slate-600 mb-3" size={40} />
          <div className="text-slate-400 mb-4">No projects yet. Start your first governance assessment.</div>
          <Link to="/projects/new" className="btn-primary">New Assessment</Link>
        </div>
      ) : (
        <div className="space-y-3">
          {projects.map(project => (
            <div key={project.id} className="card flex items-center justify-between">
              <div className="flex-1">
                <div className="font-semibold text-slate-200">{project.name}</div>
                <div className="text-sm text-slate-400 mt-0.5 line-clamp-1">{project.description}</div>
                <div className="flex gap-4 mt-1.5">
                  {project.team && (
                    <span className="text-xs text-slate-500">{project.team}</span>
                  )}
                  {project.business_unit && (
                    <span className="text-xs text-slate-500">{project.business_unit}</span>
                  )}
                  <span className="text-xs text-slate-600">
                    {new Date(project.created_at).toLocaleDateString()}
                  </span>
                </div>
              </div>
              <button
                onClick={e => handleStartAssessment(project.id, e)}
                disabled={starting === project.id}
                className="btn-secondary flex items-center gap-2 ml-4"
              >
                <Play size={14} />
                {starting === project.id ? 'Starting...' : 'Run Assessment'}
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
