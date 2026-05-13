import { useEffect, useState, useCallback } from 'react'
import { useParams } from 'react-router-dom'
import { getAssessment, getGraphData, getGaps, downloadReport } from '../utils/api'
import type { Assessment, GraphData, GapItem } from '../types'
import GovernanceGraph from '../components/GovernanceGraph'
import DomainRadar from '../components/DomainRadar'
import GapsTable from '../components/GapsTable'
import ChatPanel from '../components/ChatPanel'
import { Download, RefreshCw, AlertTriangle, CheckCircle, Loader2 } from 'lucide-react'

type Tab = 'graph' | 'gaps' | 'chat'

const RISK_COLORS: Record<string, string> = {
  critical: 'text-red-400',
  high: 'text-orange-400',
  medium: 'text-yellow-400',
  low: 'text-emerald-400',
}

export default function AssessmentPage() {
  const { assessmentId } = useParams<{ assessmentId: string }>()
  const [assessment, setAssessment] = useState<Assessment | null>(null)
  const [graphData, setGraphData] = useState<GraphData>({ nodes: [], edges: [] })
  const [gaps, setGaps] = useState<GapItem[]>([])
  const [tab, setTab] = useState<Tab>('graph')
  const [polling, setPolling] = useState(true)

  const fetchAll = useCallback(async () => {
    if (!assessmentId) return
    const a = await getAssessment(assessmentId)
    setAssessment(a)
    if (a.status === 'complete') {
      setPolling(false)
      const [g, gps] = await Promise.all([getGraphData(assessmentId), getGaps(assessmentId)])
      setGraphData(g)
      setGaps(gps)
    } else if (a.status === 'failed') {
      setPolling(false)
    }
  }, [assessmentId])

  useEffect(() => {
    fetchAll()
  }, [fetchAll])

  useEffect(() => {
    if (!polling) return
    const id = setInterval(fetchAll, 4000)
    return () => clearInterval(id)
  }, [polling, fetchAll])

  const statusIcon = () => {
    if (!assessment) return null
    if (assessment.status === 'complete') return <CheckCircle size={16} className="text-emerald-400" />
    if (assessment.status === 'failed') return <AlertTriangle size={16} className="text-red-400" />
    return <Loader2 size={16} className="animate-spin text-indigo-400" />
  }

  const riskColor = RISK_COLORS[assessment?.risk_tier || 'low'] || 'text-slate-400'

  return (
    <div className="flex flex-col h-screen">
      {/* Header */}
      <div className="border-b border-slate-800 px-6 py-4 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-3">
          {statusIcon()}
          <div>
            <div className="font-semibold text-slate-200">
              {assessment?.status === 'processing' ? 'Running Assessment...' :
               assessment?.status === 'complete' ? 'Assessment Complete' :
               assessment?.status === 'failed' ? 'Assessment Failed' : 'Loading...'}
            </div>
            {assessment?.status === 'complete' && (
              <div className="text-xs text-slate-500">
                RAI Score: <span className={`font-bold ${riskColor}`}>{assessment.rai_score?.toFixed(1)}</span>
                {' · '}Risk Tier: <span className={`font-bold ${riskColor} uppercase`}>{assessment.risk_tier}</span>
                {assessment.requires_adrb && <span className="ml-2 badge-high">ADRB Required</span>}
                {assessment.requires_ai_council && <span className="ml-2 badge-critical">AI Council Required</span>}
              </div>
            )}
          </div>
        </div>
        {assessment?.status === 'complete' && (
          <button
            onClick={() => downloadReport(assessmentId!)}
            className="btn-primary flex items-center gap-2"
          >
            <Download size={15} /> Download PDF Report
          </button>
        )}
      </div>

      {/* Processing spinner */}
      {(assessment?.status === 'pending' || assessment?.status === 'processing') && (
        <div className="flex-1 flex flex-col items-center justify-center gap-4">
          <Loader2 size={40} className="animate-spin text-indigo-500" />
          <div className="text-slate-400 text-sm">
            Analysing project proposal against {100}+ governance requirements...
          </div>
          <div className="text-slate-600 text-xs">This takes 1–2 minutes. The graph will populate automatically.</div>
        </div>
      )}

      {assessment?.status === 'failed' && (
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <AlertTriangle size={40} className="mx-auto text-red-400 mb-3" />
            <div className="text-slate-300 font-medium">Assessment Failed</div>
            <div className="text-slate-500 text-sm mt-1">Check that your document was uploaded correctly and try again.</div>
          </div>
        </div>
      )}

      {assessment?.status === 'complete' && (
        <div className="flex-1 flex flex-col min-h-0">
          {/* Summary row */}
          <div className="grid grid-cols-4 gap-4 px-6 py-4 border-b border-slate-800 shrink-0">
            <div className="card py-3">
              <div className={`text-2xl font-bold ${riskColor}`}>{assessment.rai_score?.toFixed(0)}</div>
              <div className="text-xs text-slate-500 mt-0.5">RAI Risk Score</div>
            </div>
            <div className="card py-3">
              <div className={`text-2xl font-bold uppercase ${riskColor}`}>{assessment.risk_tier}</div>
              <div className="text-xs text-slate-500 mt-0.5">Risk Tier</div>
            </div>
            <div className="card py-3">
              <div className="text-2xl font-bold text-red-400">{gaps.length}</div>
              <div className="text-xs text-slate-500 mt-0.5">Gaps Found</div>
            </div>
            <div className="card py-3">
              <div className="text-2xl font-bold text-emerald-400">
                {Math.round((assessment.overall_confidence || 0) * 100)}%
              </div>
              <div className="text-xs text-slate-500 mt-0.5">Overall Coverage</div>
            </div>
          </div>

          {/* Tabs */}
          <div className="border-b border-slate-800 px-6 shrink-0">
            <div className="flex gap-1">
              {([
                { key: 'graph', label: 'Graph View' },
                { key: 'gaps', label: `Gaps (${gaps.length})` },
                { key: 'chat', label: 'Ask AI' },
              ] as const).map(t => (
                <button
                  key={t.key}
                  onClick={() => setTab(t.key)}
                  className={`px-4 py-3 text-sm font-medium border-b-2 transition-colors ${
                    tab === t.key
                      ? 'border-indigo-500 text-indigo-400'
                      : 'border-transparent text-slate-500 hover:text-slate-300'
                  }`}
                >
                  {t.label}
                </button>
              ))}
            </div>
          </div>

          {/* Tab content */}
          <div className="flex-1 min-h-0 overflow-hidden">
            {tab === 'graph' && (
              <div className="h-full flex gap-4 p-6">
                <div className="flex-1 min-w-0">
                  <GovernanceGraph data={graphData} />
                </div>
                <div className="w-72 shrink-0">
                  <div className="card h-full flex flex-col">
                    <h3 className="font-semibold text-slate-300 text-sm mb-3">Domain Coverage</h3>
                    <DomainRadar gaps={gaps} />
                    <div className="mt-4 space-y-1.5 text-xs">
                      <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-emerald-500 shrink-0" /> ≥80% covered</div>
                      <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-amber-500 shrink-0" /> 50–79% partial</div>
                      <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-red-500 shrink-0" /> &lt;50% gap</div>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {tab === 'gaps' && (
              <div className="h-full overflow-y-auto p-6">
                <div className="max-w-4xl">
                  <div className="flex items-center justify-between mb-4">
                    <h2 className="font-semibold text-slate-200">Governance Gaps — ordered by risk</h2>
                    <span className="text-sm text-slate-500">{gaps.length} gaps identified</span>
                  </div>
                  <GapsTable gaps={gaps} />
                </div>
              </div>
            )}

            {tab === 'chat' && (
              <div className="h-full">
                <ChatPanel projectId={assessment.project_id} />
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}
