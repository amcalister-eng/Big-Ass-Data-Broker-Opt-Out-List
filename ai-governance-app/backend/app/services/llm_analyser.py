"""
LLM analysis service using Claude claude-sonnet-4-6 to score project proposals
against governance assessment questions.
"""
import json
import anthropic
from app.core.config import settings

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)


SYSTEM_PROMPT = """You are an AI governance expert analyst embedded in a governance mapping tool.
Your job is to analyse project proposal documents against specific governance assessment questions
and return structured JSON scores.

For each question you must:
1. Read the provided project text carefully
2. Assess how well the project material addresses the question
3. Return a confidence score from 0.0 (not addressed at all) to 1.0 (fully and explicitly addressed)
4. Provide a brief evidence quote from the text if addressed, or null if not found
5. Provide a gap_summary explaining what is missing (if confidence < 0.8)

Always return valid JSON only. Do not include markdown fences or explanatory text outside the JSON.
"""

ANALYSIS_PROMPT_TEMPLATE = """Project text:
---
{project_text}
---

Assess the following governance questions and return a JSON array:

{questions_json}

Return format (array of objects matching input question IDs):
[
  {{
    "question_id": "string",
    "confidence": 0.0-1.0,
    "evidence": "exact quote or null",
    "gap_summary": "what is missing or null if fully addressed"
  }}
]"""


async def analyse_against_questions(
    project_text: str,
    questions: list[dict],
    chunk_index: int = 0,
) -> list[dict]:
    """
    Analyse project text against a batch of governance questions.
    questions: list of {question_id, question_text, domain, risk_weight}
    Returns list of {question_id, confidence, evidence, gap_summary}
    """
    questions_json = json.dumps(
        [{"question_id": q["question_id"], "question_text": q["question_text"]} for q in questions],
        indent=2,
    )

    prompt = ANALYSIS_PROMPT_TEMPLATE.format(
        project_text=project_text[:5500],
        questions_json=questions_json,
    )

    message = client.messages.create(
        model=settings.claude_model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
        system=SYSTEM_PROMPT,
    )

    raw = message.content[0].text.strip()
    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw)


RAI_SCORECARD_PROMPT = """You are assessing an AI project against the RAI (Responsible AI) Risk Scorecard.

Project description:
---
{project_text}
---

Based on the project description, determine which risk factors apply.
Return a JSON object with exactly this structure:
{{
  "triggered_factors": [
    {{"factor_id": "string", "factor_name": "string", "score": number, "reasoning": "string"}}
  ],
  "mitigating_factors": [
    {{"factor_id": "string", "factor_name": "string", "score": number, "reasoning": "string"}}
  ]
}}

Only include factors that genuinely apply based on evidence in the project text.
Do not include markdown fences. Return valid JSON only.

Available risk factors (positive scores = higher risk):
- LGL_EFF: Legal effect on person = +10
- HIGH_AUT: High autonomy / autonomous decision making = +10
- BIO: Biometrics processing = +5
- EXT_CUST: External customers affected = +2
- LARGE_SCALE: Large scale processing (>10k individuals) = +3
- VULNERABLE: Vulnerable cohorts (minors, elderly, etc.) = +4
- THIRD_PARTY: Third party data sharing = +2
- REAL_TIME: Real-time or near-real-time processing = +2
- NEW_TECH: Novel or unproven technology = +3
- SENSITIVE: Sensitive data categories (health, financial, location) = +4

Mitigating factors (negative scores = lower risk):
- POC_ONLY: Proof of concept only, no production = -1
- HUMAN_LOOP: Strong human-in-the-loop controls = -2
- INTERNAL_ONLY: Internal staff only, no customer impact = -1
- EXISTING_APPROVAL: Existing approved model/system being extended = -1
"""


async def calculate_rai_scorecard(project_text: str) -> dict:
    message = client.messages.create(
        model=settings.claude_model,
        max_tokens=2048,
        messages=[{"role": "user", "content": RAI_SCORECARD_PROMPT.format(project_text=project_text[:4000])}],
    )
    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw)


CHATBOT_SYSTEM = """You are a project-scoped AI governance advisor.
You have access to:
1. The project proposal document uploaded by the team
2. The governance assessment results including gaps, risk scores, and recommendations

Answer questions about THIS project's governance status only.
Be specific, reference actual gaps found in the assessment, and recommend concrete next steps.
If asked about general governance topics unrelated to this project, redirect the user to focus on their project.
Always cite which governance domain or standard you are referring to.
"""


def chat_with_project(
    project_text: str,
    assessment_summary: str,
    conversation: list[dict],
) -> str:
    context_message = f"""Project document summary:
{project_text[:3000]}

Assessment findings summary:
{assessment_summary}
"""
    messages = [{"role": "user", "content": context_message}, {"role": "assistant", "content": "Understood. I have reviewed the project document and assessment findings. How can I help?"}]
    messages.extend(conversation)

    response = client.messages.create(
        model=settings.claude_model,
        max_tokens=1024,
        system=CHATBOT_SYSTEM,
        messages=messages,
    )
    return response.content[0].text
