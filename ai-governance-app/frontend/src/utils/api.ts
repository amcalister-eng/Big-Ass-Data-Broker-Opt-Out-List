import axios from 'axios'
import type { Project, Assessment, GraphData, GapItem, ChatMessage } from '../types'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api',
})

// Projects
export const createProject = async (formData: FormData): Promise<Project> => {
  const res = await api.post('/projects', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return res.data
}

export const listProjects = async (): Promise<Project[]> => {
  const res = await api.get('/projects')
  return res.data
}

export const getProject = async (id: string): Promise<Project> => {
  const res = await api.get(`/projects/${id}`)
  return res.data
}

// Assessments
export const startAssessment = async (projectId: string): Promise<Assessment> => {
  const res = await api.post(`/assessments/${projectId}/start`)
  return res.data
}

export const getAssessment = async (id: string): Promise<Assessment> => {
  const res = await api.get(`/assessments/${id}`)
  return res.data
}

export const getGraphData = async (assessmentId: string): Promise<GraphData> => {
  const res = await api.get(`/assessments/${assessmentId}/graph`)
  return res.data
}

export const getGaps = async (assessmentId: string): Promise<GapItem[]> => {
  const res = await api.get(`/assessments/${assessmentId}/gaps`)
  return res.data
}

// Chat
export const sendMessage = async (
  projectId: string,
  message: string,
  history: ChatMessage[],
): Promise<{ response: string; sources: string[] }> => {
  const res = await api.post('/chat', { project_id: projectId, message, history })
  return res.data
}

// Reports
export const downloadReport = (assessmentId: string) => {
  window.open(`/api/reports/${assessmentId}/pdf`, '_blank')
}
