''' Lambdas, map, filter
Scenario: You're building a data pipeline for an e-commerce backend. Orders come in as raw dicts. You need to clean, filter, and transform them using functional tools — no loops allowed anywhere.
Here's your starting data:
pythonorders = [
    {"id": 1, "amount": 250.5,  "status": "completed", "customer": "alice"},
    {"id": 2, "amount": 89.0,   "status": "pending",   "customer": "bob"},
    {"id": 3, "amount": 4500.0, "status": "completed", "customer": "charlie"},
    {"id": 4, "amount": 15.0,   "status": "cancelled", "customer": "dave"},
    {"id": 5, "amount": 1200.0, "status": "completed", "customer": "eve"},
]
Tasks — all in one file, no loops:
Task A — Using filter + a lambda, get only the "completed" orders.
Task B — Using map + a lambda, transform each completed order into this shape:
python{"order_id": 1, "total": 250.5, "customer": "ALICE"}   # customer uppercased
Task C — Using sorted + a lambda as the key, sort the transformed orders by total descending.
Task D — Write a standalone lambda apply_discount that takes (order, pct) — e.g. pct=10 — and returns a new dict with total reduced by that percentage. Apply it to the first result from Task C using map.
Task E — Chain A → B → C as a single expression (no intermediate variables). One line.'''

pythonorders = [
    {"id": 1, "amount": 250.5,  "status": "completed", "customer": "alice"},
    {"id": 2, "amount": 89.0,   "status": "pending",   "customer": "bob"},
    {"id": 3, "amount": 4500.0, "status": "completed", "customer": "charlie"},
    {"id": 4, "amount": 15.0,   "status": "cancelled", "customer": "dave"},
    {"id": 5, "amount": 1200.0, "status": "completed", "customer": "eve"},
]

# Task A — Using filter + a lambda, get only the "completed" orders.
task_a = list(filter(lambda x: x["status"]=="completed",pythonorders))
print(task_a)

# Task B — Using map + a lambda, transform each completed order into this shape: 
# python{"order_id": 1, "total": 250.5, "customer": "ALICE"}   # customer uppercased

task_b = list(map(lambda x: {
    "order_id":x["id"],
    "total":x["amount"],
    "customer":x["customer"].upper()
    },task_a))
print(task_b)

# Task C — Using sorted + a lambda as the key, sort the transformed orders by total descending.

task_c = list(sorted(pythonorders, key=lambda x: x["total"], reverse=True))
print(task_c)

# Task D — Write a standalone lambda apply_discount that takes (order, pct) — e.g. pct=10 — and returns a new dict with total reduced by that percentage. Apply it to the first result from Task C using map.

apply_discount = lambda order, pct: {
    **order,
    "total": round(order["total"] * (1 - pct / 100), 2)
}

task_d = list(
    map(
        lambda order: apply_discount(order, 10),
        [task_c[0]]
    )
)

print(task_d)

# Task E — Chain A → B → C as a single expression (no intermediate variables). One line.'''

task_e = sorted(
    map(
        lambda order: {
            "order_id": order["id"],
            "total": order["amount"],
            "customer": order["customer"].upper()
        },
        filter(
            lambda order: order["status"] == "completed",
            orders
        )
    ),
    key=lambda order: order["total"],
    reverse=True
)

print("\nTask E:")
print(task_e)