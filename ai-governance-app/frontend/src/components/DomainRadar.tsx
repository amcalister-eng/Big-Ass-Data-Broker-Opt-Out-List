import {
  RadarChart,
  Radar,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
  Tooltip,
} from 'recharts'
import type { GapItem } from '../types'

interface Props {
  gaps: GapItem[]
}

export default function DomainRadar({ gaps }: Props) {
  // Compute average confidence per domain
  const byDomain: Record<string, number[]> = {}
  gaps.forEach(g => {
    byDomain[g.domain] = byDomain[g.domain] || []
    byDomain[g.domain].push(g.confidence)
  })

  const data = Object.entries(byDomain).map(([domain, confs]) => ({
    domain: domain.replace(' & ', '\n& '),
    score: Math.round((confs.reduce((a, b) => a + b, 0) / confs.length) * 100),
  }))

  if (data.length === 0) return null

  return (
    <ResponsiveContainer width="100%" height={280}>
      <RadarChart data={data}>
        <PolarGrid stroke="#334155" />
        <PolarAngleAxis dataKey="domain" tick={{ fontSize: 10, fill: '#94a3b8' }} />
        <PolarRadiusAxis angle={30} domain={[0, 100]} tick={{ fontSize: 9, fill: '#475569' }} />
        <Radar
          name="Coverage"
          dataKey="score"
          stroke="#6366f1"
          fill="#6366f1"
          fillOpacity={0.35}
          strokeWidth={2}
        />
        <Tooltip
          contentStyle={{ background: '#0f172a', border: '1px solid #334155', borderRadius: 8, fontSize: 12 }}
          formatter={(v: number) => [`${v}%`, 'Coverage']}
        />
      </RadarChart>
    </ResponsiveContainer>
  )
}
