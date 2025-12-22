How does intelligence actually work inside the system?

This diagram breaks down the internal architecture of an AI agent and clearly separates machine learning, retrieval, reasoning, and execution.
LLMs are used as reasoning engines, not as decision-makers, which ensures safety and predictability.



[ Input ]
   |
   v
[ Intent Classifier ] (ML)
   |
   v
[ Context Builder ]  (RAG)
   |
   v
[ LLM Reasoning ]   (LLM)
   |
   v
[ Action Planner ]
   |
   v
[ Guardrails ]
   |
   v
[ Tool Executor ]



Component explanation:
1) Input Parser - 
Normalizes raw input
Extracts metadata

2) Intent Classifier (ML) - 
Traditional ML model
Determines task type
Keeps logic deterministic

3) Context Builder (RAG) - 
Fetches relevant domain knowledge
Prevents hallucinations

4) LLM Reasoning Engine - 
Performs natural language reasoning
Generates explanations and plans

5) State Manager - 
Tracks agent execution state
Enables retries and multi-step reasoning

6) Action Planner - 
Converts reasoning into structured steps

7) Guardrails - 
Safety checks
Approval workflows
Dry-run support

8) Tool Executor - 
Executes code or infra actions
Logs everything