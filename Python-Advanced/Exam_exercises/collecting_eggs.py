from collections import deque

eggs = deque([int(s) for s in input().split(', ')])
papers = deque([int(s) for s in input().split(', ')])
filled_boxes = 0


while eggs and papers:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue
    if current_egg == 13:
        first_paper = papers.popleft()
        last_paper = papers.pop()
        papers.appendleft(last_paper)
        papers.append(first_paper)
        continue
    current_paper = papers.pop()
    if current_egg + current_paper <= 50:
        filled_boxes += 1

if filled_boxes:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(str(s) for s in eggs)}')
if papers:
    print(f'Pieces of paper left: {", ".join(str(s) for s in papers)}')