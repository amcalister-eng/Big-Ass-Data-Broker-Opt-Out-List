import type { GapItem } from '../types'
import { ChevronDown, ChevronUp } from 'lucide-react'
import { useState } from 'react'
import clsx from 'clsx'

interface Props {
  gaps: GapItem[]
}

const riskBadge = (r: string) => {
  const map: Record<string, string> = {
    critical: 'badge-critical',
    high: 'badge-high',
    medium: 'badge-medium',
    low: 'badge-low',
  }
  return map[r] || 'badge-low'
}

const confidenceBar = (c: number) => {
  const pct = Math.round(c * 100)
  const color = c >= 0.8 ? 'bg-emerald-500' : c >= 0.5 ? 'bg-amber-500' : 'bg-red-500'
  return (
    <div className="flex items-center gap-2">
      <div className="flex-1 bg-slate-700 rounded-full h-1.5">
        <div className={`h-1.5 rounded-full ${color}`} style={{ width: `${pct}%` }} />
      </div>
      <span className="text-xs text-slate-400 w-8 text-right">{pct}%</span>
    </div>
  )
}

export default function GapsTable({ gaps }: Props) {
  const [expanded, setExpanded] = useState<string | null>(null)

  const sorted = [...gaps].sort((a, b) => a.confidence - b.confidence)

  return (
    <div className="space-y-2">
      {sorted.map(gap => (
        <div key={gap.question_id} className="border border-slate-800 rounded-xl overflow-hidden">
          <button
            onClick={() => setExpanded(expanded === gap.question_id ? null : gap.question_id)}
            className="w-full text-left px-4 py-3 flex items-start gap-3 hover:bg-slate-800/50 transition-colors"
          >
            <span className={riskBadge(gap.risk_rating)}>{gap.risk_rating}</span>
            <div className="flex-1 min-w-0">
              <div className="text-sm text-slate-300 font-medium leading-tight mb-1">{gap.question_text}</div>
              <div className="text-xs text-slate-500">{gap.domain}</div>
            </div>
            <div className="w-32 shrink-0 mt-0.5">
              {confidenceBar(gap.confidence)}
            </div>
            <div className="text-slate-600 shrink-0 mt-0.5">
              {expanded === gap.question_id ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
            </div>
          </button>

          {expanded === gap.question_id && (
            <div className="px-4 pb-4 border-t border-slate-800 bg-slate-900/50 space-y-3 pt-3">
              {gap.gap_description && (
                <div>
                  <div className="text-xs font-semibold text-slate-500 uppercase mb-1">Gap</div>
                  <div className="text-sm text-slate-300">{gap.gap_description}</div>
                </div>
              )}
              {gap.controls?.length > 0 && (
                <div>
                  <div className="text-xs font-semibold text-slate-500 uppercase mb-1">Recommended Controls</div>
                  <ul className="space-y-1">
                    {gap.controls.map((c, i) => (
                      <li key={i} className="text-sm text-slate-300 flex gap-2">
                        <span className="text-indigo-400 shrink-0">→</span> {c}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
              {gap.patterns?.length > 0 && (
                <div>
                  <div className="text-xs font-semibold text-slate-500 uppercase mb-1">Governance Patterns</div>
                  <div className="flex flex-wrap gap-1.5">
                    {gap.patterns.map((p, i) => (
                      <span key={i} className="text-xs bg-indigo-950/50 text-indigo-300 border border-indigo-900 px-2 py-0.5 rounded">{p}</span>
                    ))}
                  </div>
                </div>
              )}
              {gap.standards?.length > 0 && (
                <div>
                  <div className="text-xs font-semibold text-slate-500 uppercase mb-1">Standards</div>
                  <div className="flex flex-wrap gap-1.5">
                    {gap.standards.map((s, i) => (
                      <span key={i} className="text-xs bg-slate-800 text-slate-400 border border-slate-700 px-2 py-0.5 rounded">{s}</span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      ))}
    </div>
  )
}
