What happens when a request enters the system?

The request flow is designed to be deterministic around execution, with LLMs used only for reasoning and not for direct system control.



[ User ]
   |
   | HTTP POST /analyze
   v
[ FastAPI API ]
   |
   | validated request
   v
[ Agent Orchestrator ]
   |
   | context query
   v
[ RAG Engine ]
   |
   | embeddings search
   v
[ Vector DB (FAISS) ]
   |
   | relevant docs
   v
[ LLM ]
   |
   | reasoning output
   v
[ Decision Engine ]
   |
   | tool call
   v
[ Tool Executor ]
   |
   | result
   v
[ API Response ]




Step by step Explanation: 
1) User sends request -
HTTP POST with JSON playload
e.g - incident description or query

2) FastApi API Layer - 
Receives the request
Performs schema validation using Pydantic
Handles authentication and rate limiting

3) Agent Orchestrator - 
Acts as the brain of the system
Determines which agent should handle the request
Maintains execution state

4) RAG Engine -
Builds semantic context
Converts input into embeddings
Queries vector database

5) Vector Database -
Stores embeddings of documents, runbooks, or code
Returns top relevant chunks

6) LLM Reasoning Engine -
Combines:
   User input
   Retrieved context
Produces a structured reasoning output

7) Decision Engine -
Interprets LLM output
Decides:
   Severity
   Suggested action
   Whether automation is allowed

8) Tool Executor -
Executes safe actions
Fully controlled & auditable

9) Response to User -
Structured response
Includes explanation + action taken/suggested