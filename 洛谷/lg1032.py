start, target = input().split()
rules = []
while True:
  try:
    text = input()
    if not text:
      break
    rules.append(text.split())
  except:
    break

queue = [(start, 0)]
used = set()
used.add(start)
find_ans = -1
while queue:
  s, step = queue.pop(0)
  # print(used)
  if step > 10:
    break
  if s == target:
    find_ans = step
    break
  for r in rules:
    nstrs = []
    lens = len(r[0])
    for i in range(len(s)):
      if s[i:i+lens] == r[0]:
        ns = s[:i] + r[1] + s[i+lens:]
        if not(ns in used):
          nstrs.append(ns)
    #print(nstrs)
    for ns in nstrs:
      used.add(ns)
      queue.append((ns, step + 1))
if find_ans == -1:
  print('NO ANSWER!')
else:
  print(find_ans)
