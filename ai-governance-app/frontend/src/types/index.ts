export interface Project {
  id: string
  name: string
  description: string
  team?: string
  business_unit?: string
  file_name?: string
  created_at: string
}

export interface Assessment {
  id: string
  project_id: string
  status: 'pending' | 'processing' | 'complete' | 'failed'
  rai_score?: number
  risk_tier?: string
  overall_confidence?: number
  requires_adrb?: boolean
  requires_ai_council?: boolean
  created_at: string
  completed_at?: string
}

export interface GraphNode {
  data: {
    id: string
    label: string
    type: 'domain' | 'question'
    confidence?: number
    risk_rating?: string
    gap_summary?: string
    standards?: string[]
    color?: string
  }
}

export interface GraphEdge {
  data: {
    id: string
    source: string
    target: string
    weight?: number
  }
}

export interface GraphData {
  nodes: GraphNode[]
  edges: GraphEdge[]
}

export interface GapItem {
  domain: string
  question_id: string
  question_text: string
  confidence: number
  risk_rating: string
  gap_description: string
  controls: string[]
  patterns: string[]
  standards: string[]
}

export interface ChatMessage {
  role: 'user' | 'assistant'
  content: string
}
