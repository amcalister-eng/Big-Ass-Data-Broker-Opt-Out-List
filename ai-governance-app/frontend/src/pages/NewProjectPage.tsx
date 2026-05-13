import { useState, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import { useDropzone } from 'react-dropzone'
import { createProject, startAssessment } from '../utils/api'
import { Upload, FileText, Loader2 } from 'lucide-react'

export default function NewProjectPage() {
  const navigate = useNavigate()
  const [form, setForm] = useState({ name: '', description: '', team: '', business_unit: '' })
  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const onDrop = useCallback((accepted: File[]) => {
    if (accepted[0]) setFile(accepted[0])
  }, [])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'text/plain': ['.txt'],
    },
    maxFiles: 1,
  })

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!form.name || !form.description) {
      setError('Project name and description are required.')
      return
    }
    setLoading(true)
    setError('')
    try {
      const fd = new FormData()
      fd.append('name', form.name)
      fd.append('description', form.description)
      fd.append('team', form.team)
      fd.append('business_unit', form.business_unit)
      if (file) fd.append('file', file)

      const project = await createProject(fd)
      const assessment = await startAssessment(project.id)
      navigate(`/assessment/${assessment.id}`)
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : 'Failed to create project')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-8 max-w-2xl">
      <h1 className="text-2xl font-bold text-white mb-2">New Governance Assessment</h1>
      <p className="text-slate-400 text-sm mb-8">
        Upload your project proposal and we'll analyse it against all governance requirements.
      </p>

      <form onSubmit={handleSubmit} className="space-y-5">
        <div>
          <label className="block text-sm font-medium text-slate-300 mb-1.5">Project Name *</label>
          <input
            type="text"
            value={form.name}
            onChange={e => setForm({ ...form, name: e.target.value })}
            placeholder="e.g. Customer Churn Prediction AI"
            className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-300 mb-1.5">Project Description *</label>
          <textarea
            value={form.description}
            onChange={e => setForm({ ...form, description: e.target.value })}
            rows={4}
            placeholder="Describe what the AI system does, its purpose, data sources, and who it affects..."
            className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500 resize-none"
          />
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-slate-300 mb-1.5">Team</label>
            <input
              type="text"
              value={form.team}
              onChange={e => setForm({ ...form, team: e.target.value })}
              placeholder="e.g. Data Science"
              className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-slate-300 mb-1.5">Business Unit</label>
            <input
              type="text"
              value={form.business_unit}
              onChange={e => setForm({ ...form, business_unit: e.target.value })}
              placeholder="e.g. Retail Technology"
              className="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
          </div>
        </div>

        {/* Dropzone */}
        <div>
          <label className="block text-sm font-medium text-slate-300 mb-1.5">
            Project Proposal Document <span className="text-slate-500">(PDF, DOCX, or TXT)</span>
          </label>
          <div
            {...getRootProps()}
            className={`border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-colors ${
              isDragActive ? 'border-indigo-500 bg-indigo-950/20' : 'border-slate-700 hover:border-slate-500'
            }`}
          >
            <input {...getInputProps()} />
            {file ? (
              <div className="flex items-center justify-center gap-3 text-slate-300">
                <FileText size={20} className="text-indigo-400" />
                <span className="text-sm">{file.name}</span>
                <button
                  type="button"
                  onClick={e => { e.stopPropagation(); setFile(null) }}
                  className="text-xs text-slate-500 hover:text-red-400"
                >
                  Remove
                </button>
              </div>
            ) : (
              <div>
                <Upload className="mx-auto text-slate-600 mb-2" size={28} />
                <div className="text-sm text-slate-400">
                  {isDragActive ? 'Drop file here' : 'Drag & drop or click to upload'}
                </div>
                <div className="text-xs text-slate-600 mt-1">PDF, DOCX or TXT · Max 50MB</div>
              </div>
            )}
          </div>
        </div>

        {error && <div className="text-sm text-red-400 bg-red-950/30 border border-red-800 rounded-lg px-4 py-3">{error}</div>}

        <button type="submit" disabled={loading} className="btn-primary w-full flex items-center justify-center gap-2 py-3">
          {loading ? (
            <><Loader2 size={16} className="animate-spin" /> Running Governance Assessment...</>
          ) : (
            'Start Assessment'
          )}
        </button>
      </form>
    </div>
  )
}
