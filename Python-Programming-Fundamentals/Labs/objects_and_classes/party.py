class Party:
    def __init__(self):
        self.people = []


command = input()
party_visitors = Party()
while command != 'End':
    party_visitors.people.append(command)
    command = input()
print(f"Going: {', '.join(party_visitors.people)}")
print(f'Total: {len(party_visitors.people)}')
