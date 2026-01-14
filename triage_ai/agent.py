class NexusTriage:
    def __init__(self):
        # Keywords that signal immediate life threats
        self.critical_keywords = ['trapped', 'bleeding', 'heart', 'breathing', 'fire', 'crushed']
        self.urgent_keywords = ['water', 'food', 'broken', 'child', 'cold', 'stuck']

    def analyze_message(self, text):
        """Categorizes messages into Priority Tiers."""
        text = text.lower()
        score = 0
        
        # Scoring Logic
        for word in self.critical_keywords:
            if word in text: score += 10
        for word in self.urgent_keywords:
            if word in text: score += 5

        # Priority Assignment
        if score >= 10:
            return "🔴 TIER 1: CRITICAL (Immediate Rescue Required)"
        elif score >= 5:
            return "🟡 TIER 2: URGENT (Medical/Supply Aid Needed)"
        else:
            return "🟢 TIER 3: WELFARE (General Update/Safe)"

# --- LIVE DEMO SCRIPT ---
triage = NexusTriage()

messages = [
    "I am trapped under a fallen pillar and bleeding.",
    "My child is hungry and we need water.",
    "The road is blocked but we are safe for now."
]

print("--- NEXUS-ZERO AI TRIAGE RESULTS ---")
for msg in messages:
    print(f"MESSAGE: {msg}")
    print(f"RESULT:  {triage.analyze_message(msg)}\n")