"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
In this task I experiment with Llama-3.3-70B-Instruct model and 3 variants of prompts (plain, xml, sandwich).
I observed, that for all queries model returned either "The Haymarket Vaults" for plain text 
or "The Albanach" for xml and sandwich.
Both of these venues (variations) are correct (comply with our requirements).
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
"The Holyrood Arms" is hardest distractor in my opinion, because this venue adds a new check,
whether model will be tricked with satisfied conditions for capacity and vegan, but no availability.
The other distractor "The New Town Vault" doesn't bring additional value, in terms of conditions 
it's the same as "The Guilford Arms" which is correctly not being picked by model.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
In this part we experimented with smaller model (gemma-2-2b-it) on a list of venues with distractors.
It was needed to show, that lighter model can easier make mistake.
However, that model was sufficient for our task: the result is correct for all 3 cases
and same venues were selected as for large model.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when signal-to-noise ratio is low, i.e. context is long, some useful information
is placed in the middle (and got less/no attention), dataset is not nicely formatted or have distractors.
Moreover this is useful technique for smaller models, that are likely to be distracted/hallicinate/make mistakes.
"""
