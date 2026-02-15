from memory.technique_store import technique_store
from memory.TECHNIQUES import TECHNIQUES

texts = []
metadatas = []

for tech in TECHNIQUES:
    text = f"""
Technique: {tech['name']}
When to use: {tech['when_to_use']}
Core idea: {tech['core_idea']}
Time complexity: {tech['time']}
Space complexity: {tech['space']}
Common mistakes: {tech['mistakes']}
""".strip()

    texts.append(text)
    metadatas.append({
        "name": tech["name"],
        "domain": "DSA",
        "type": "algorithmic-technique"
    })

technique_store.add_texts(texts=texts, metadatas=metadatas)
technique_store.persist()

print(f"[MEMORY] Seeded {len(texts)} techniques")
