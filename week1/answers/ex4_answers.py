"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = """
It seems there are no Edinburgh venues currently available that can accommodate 300 people with vegan options. Would you like to:

1. Search for venues with a lower capacity?
2. Look for venues without vegan requirements?
3. Check availability for a different date?

Let me know how you'd like to proceed.
"""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I was required to update the only one line in sovereign_agent/tools/mcp_venue_server.py (The Albanach venue status 
from "available" to "full").
The final output wasn't changed, however in intermediate calls for q1 I observed, that tool_result output was
different (2 and 1 matches respectively). Thus thinking flow was slightly changed (no need to choose if only 1 option
is available).
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 8   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
In MCP tools are being retrieved dynamically, so if new tool is added or remove, existing code don't require any manual
updates. In opposite, in hardcoded approach, if we want to add new tool, we need to update code manually 
(add new function and update tool list).
Moreover, MCP is universal protocol, that can be easily plugged to other agents.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- Planner (upstream layer): Strong-reasoning model that orchestrates whole flow of the task and breaks it to subgoals.
- Executor (autonomous loop layer): ReAct loop with list of tools, to make research and select venues, 
that satisfy initial request. After venue is booked, generation of flyers and sending invitations.
- Memory store (shared layer): Storage, responsible for keeping conversation history, states, tools call history, etc.
- Handoff bridge (shared layer): Pass information from part1 (LangGraph) to part2 (Rasa) to make a reservation.
Connection may be bidirectional, in case reservation failed, so we can try with other options.
- Rasa (structured agent layer): Making a call to venue and reports the success/failure/other. 
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph agent plays role of the research, calling tools for gathering additional information to satisfy our request.
The Rasa agent is responsible for handling human friendly/human-style dialog or conversation with real people,
that will perfectly work for interacting via chat or phone (with additional s2t and t2s setups).
Swapping will feel wrong, because Rasa is deterministic, with defined flow, that works perfect to complete scripted
task, but it's not suitable for research.
LangGraph doesn't have defined flow (more ways for improvisation), interaction should be given in one prompt,
that wouldn't work for interactions via phone.
"""