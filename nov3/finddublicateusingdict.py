
s = input("Enter a string: ")

s = s.lower()

counts = {}
for ch in s:
	if ch.isspace():

		continue
	counts[ch] = counts.get(ch, 0) + 1

found = False
for ch, cnt in counts.items():
	if cnt > 1:
		print(f"{ch}: {cnt}")
		found = True

if not found:
	print("No duplicate characters found.")

