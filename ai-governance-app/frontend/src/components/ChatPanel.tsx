import { useState, useRef, useEffect } from 'react'
import { sendMessage } from '../utils/api'
import type { ChatMessage } from '../types'
import { Send, Bot, User } from 'lucide-react'
import ReactMarkdown from 'react-markdown'

interface Props {
  projectId: string
}

export default function ChatPanel({ projectId }: Props) {
  const [history, setHistory] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [history])

  const handleSend = async () => {
    if (!input.trim() || loading) return
    const msg = input.trim()
    setInput('')
    setHistory(h => [...h, { role: 'user', content: msg }])
    setLoading(true)
    try {
      const res = await sendMessage(projectId, msg, history)
      setHistory(h => [...h, { role: 'assistant', content: res.response }])
    } catch {
      setHistory(h => [...h, { role: 'assistant', content: 'Sorry, something went wrong. Please try again.' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex flex-col h-full">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto space-y-4 p-4">
        {history.length === 0 && (
          <div className="text-center text-slate-500 text-sm py-8">
            <Bot className="mx-auto mb-2 text-slate-700" size={32} />
            Ask me about this project's governance gaps, risk ratings, or what to do next.
          </div>
        )}
        {history.map((msg, i) => (
          <div key={i} className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : ''}`}>
            {msg.role === 'assistant' && (
              <div className="w-7 h-7 rounded-full bg-indigo-600 flex items-center justify-center shrink-0 mt-0.5">
                <Bot size={14} />
              </div>
            )}
            <div
              className={`max-w-[85%] rounded-xl px-4 py-2.5 text-sm ${
                msg.role === 'user'
                  ? 'bg-indigo-600 text-white'
                  : 'bg-slate-800 text-slate-200'
              }`}
            >
              {msg.role === 'assistant' ? (
                <ReactMarkdown className="prose prose-sm prose-invert max-w-none">
                  {msg.content}
                </ReactMarkdown>
              ) : (
                msg.content
              )}
            </div>
            {msg.role === 'user' && (
              <div className="w-7 h-7 rounded-full bg-slate-700 flex items-center justify-center shrink-0 mt-0.5">
                <User size={14} />
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div className="flex gap-3">
            <div className="w-7 h-7 rounded-full bg-indigo-600 flex items-center justify-center">
              <Bot size={14} />
            </div>
            <div className="bg-slate-800 rounded-xl px-4 py-2.5">
              <div className="flex gap-1">
                {[0, 1, 2].map(i => (
                  <div key={i} className="w-1.5 h-1.5 bg-slate-500 rounded-full animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />
                ))}
              </div>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="border-t border-slate-800 p-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && !e.shiftKey && handleSend()}
            placeholder="Ask about this project's governance gaps..."
            className="flex-1 bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
          />
          <button
            onClick={handleSend}
            disabled={loading || !input.trim()}
            className="btn-primary px-3"
          >
            <Send size={16} />
          </button>
        </div>
      </div>
    </div>
  )
}
