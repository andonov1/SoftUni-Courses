n = int(input())
stacked_queries = []
for i in range(n):
    query_data = input().split()
    query_number = query_data[0]
    if query_number == '1':
        stacked_queries.append(int(query_data[1]))
    elif query_number == '2' and stacked_queries:
        stacked_queries.pop()
    elif query_number == '3' and stacked_queries:
        print(max(stacked_queries))
    elif query_number == '4' and stacked_queries:
        print(min(stacked_queries))

while stacked_queries:
    element = stacked_queries.pop()
    if stacked_queries:
        print(element, end=', ')
    else:
        print(element)