import { useEffect, useRef } from 'react'
import cytoscape from 'cytoscape'
import type { GraphData } from '../types'

interface Props {
  data: GraphData
}

export default function GovernanceGraph({ data }: Props) {
  const containerRef = useRef<HTMLDivElement>(null)
  const cyRef = useRef<cytoscape.Core | null>(null)

  useEffect(() => {
    if (!containerRef.current || data.nodes.length === 0) return

    if (cyRef.current) {
      cyRef.current.destroy()
    }

    cyRef.current = cytoscape({
      container: containerRef.current,
      elements: [...data.nodes, ...data.edges],
      style: [
        {
          selector: 'node[type="domain"]',
          style: {
            'background-color': 'data(color)',
            label: 'data(label)',
            color: '#fff',
            'font-size': 11,
            'font-weight': 'bold',
            width: 50,
            height: 50,
            'text-valign': 'center',
            'text-halign': 'center',
            'text-wrap': 'wrap',
            'text-max-width': 60,
          },
        },
        {
          selector: 'node[type="question"]',
          style: {
            'background-color': 'data(color)',
            label: 'data(label)',
            color: '#fff',
            'font-size': 8,
            width: 24,
            height: 24,
            'text-valign': 'bottom',
            'text-halign': 'center',
            'text-margin-y': 4,
            'text-wrap': 'wrap',
            'text-max-width': 80,
          },
        },
        {
          selector: 'edge',
          style: {
            'line-color': '#334155',
            width: 1.5,
            'curve-style': 'bezier',
            opacity: 0.6,
          },
        },
        {
          selector: 'node:selected',
          style: {
            'border-width': 2,
            'border-color': '#818cf8',
          },
        },
      ],
      layout: {
        name: 'cose',
        animate: true,
        animationDuration: 600,
        nodeRepulsion: () => 8000,
        nodeOverlap: 20,
        idealEdgeLength: () => 80,
        gravity: 0.3,
      },
      userZoomingEnabled: true,
      userPanningEnabled: true,
    })

    return () => {
      cyRef.current?.destroy()
    }
  }, [data])

  return (
    <div ref={containerRef} className="w-full h-full rounded-xl bg-slate-950" />
  )
}
