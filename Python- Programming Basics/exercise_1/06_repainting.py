quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
hours_work = int(input())
bag = 0.40
cost_nylon = float(quantity_nylon + 2) * 1.50
cost_paint = float(quantity_paint + 0.1 * quantity_paint) * 14.50
cost_thinner = quantity_thinner * 5
total_materials = float(cost_nylon + cost_paint + cost_thinner + bag)
cost_work = hours_work * (total_materials * 0.30)
total_cost = total_materials + cost_work
print(total_cost)
