import random
import uuid
from datetime import datetime, timezone


def generate_order():
    order = {
        "order_id": str(uuid.uuid4()),
        "customer_id": random.randint(1, 100),
        "amount": round(random.uniform(10, 500), 2),
        "status": "created",
        "event_time": datetime.now(timezone.utc).isoformat(),
    }

    return order


def main():
    for _ in range(5):
        order = generate_order()
        print(order)


if __name__ == "__main__":
    main()