!pip install faker pandas

import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(42)

rows = []
for _ in range(100000):
    rows.append({
        "order_id": fake.uuid4(),
        "order_date": fake.date_between(start_date='-6M', end_date='today'),
        "customer_id": fake.uuid4(),
        "product_category": random.choice(["Electronics", "Clothing", "Home", "Toys", "Books"]),
        "order_amount": round(random.uniform(5.0, 500.0), 2),
        "payment_method": random.choice(["Credit Card", "PayPal", "Gift Card", "Apple Pay"])
    })

df = pd.DataFrame(rows)
df.to_csv("orders.csv", index=False)
df.head()
 

