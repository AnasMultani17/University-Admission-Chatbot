import re
import pandas as pd

input_path = "data/cleaned_text.txt"
output_path = "data/cleaned_dataset.csv"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

lines = [line.strip() for line in text.split("\n") if line.strip()]

faqs = []
current_q = None
current_a = []

for line in lines:
    if re.match(r"(?i)^q[:\-–. ]", line) or line.endswith("?"):
        if current_q and current_a:
            faqs.append({"question": current_q, "answer": " ".join(current_a).strip()})
            current_a = []
        current_q = re.sub(r"(?i)^q[:\-–. ]", "", line).strip()
    elif re.match(r"(?i)^a[:\-–. ]", line):
        continue
    else:
        current_a.append(line)

if current_q and current_a:
    faqs.append({"question": current_q, "answer": " ".join(current_a).strip()})

df = pd.DataFrame(faqs)
df.to_csv(output_path, index=False)

print(f"✅ Extracted {len(faqs)} FAQ pairs and saved to {output_path}")
