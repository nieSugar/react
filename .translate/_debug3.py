hp = r"D:\Personal\Downloads\react\019 - Complex State with useReducer - ui.dev.html"
with open(hp, "r", encoding="utf-8", errors="replace") as f:
    h = f.read()
idx = h.find("For resetting")
# Print with escape chars for readability
seg = h[idx-80:idx+600]
print(repr(seg))
print()
print("--- rendered ---")
print(seg)