"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
I’m sorry I am unable to understand you, could you please rephrase?
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £1000 deposit
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £1000 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?                                                                                                                                                                    
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "The issue is: a deposit of £1000 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  can you arrange hotel for the speakers?
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
I asked to book a hotel for speakers. Since it was out of scope task I was informed that I can't get help with that.
In the meantime, CALM tried to return the conversation to venue booking flow. 
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
The difference was that LangGraph still tried to help with my request, providing additional information about where
I can get information about train schedule.
While the LangGraph just explicitly told that it's out of scope task and tried to return to venue booking flow.
The common part is that both acknowledged, that this is out of scope task, that they can't help with.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I did uncomment Cutoff Guard lines and run the retrain command.
After that I start the server and chat. I didn't change flag to always True, because I was testing 11pm, so escalation
should be raised natively. And it did: "The issue is: it is past 16:45 — insufficient time to process the confirmation 
before the 5 PM deadline".
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
Whole flow is now in one place – flows.yml, so it is simpler to manage.
After ValidateBookingConfirmationForm deprecation, llm handles number extraction. That work was delegated, and
it actually brings some benefits. I managed to book for "fifty" guests, "ten" vegans, that was not an option for
ValidateBookingConfirmationForm.
So LLM is responsible for language understanding, intents and slots extractions. 
Python is still responsible for business rules, escalation (e.g. max guests, max deposits, etc). 
The new approach is less deterministic, due to llm.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
CALM has deterministic behaviour with defined flow, business rules, escalations.
Also the way we interact with CALM like dialog between human, instead of constructing whole prompt at the beginning,
we're being asked multiple questions to gather all required details. Also, it keeps dialog state.
The answer is deterministic, CALM wouldn't go to execute out of script task.

LangGraph is more flexible, but it is not deterministic, we don't know how many and which tools will be used, etc.
Also user should provide the whole information in one go (prompt), because it doesn't support asking clarification
questions.
LangGraph is more universal, e.g. if we introduce new tool for train schedules, no other changes are required to
provide users that information. Or LangGraph can answer "base knowledge" questions.

Each agent are different in that way, that can be considered as a limitation. From my prospective, this agents should
be used in different situations, so limitation turns into feature.
"""
