from locust import task, HttpUser, between
import random


class ItemUser(HttpUser):
    wait_time = between(1, 3)
    token = None

    def on_start(self):
        response = self.client.post(
            '/authorize',
            json={'name': 'YourName'}
        )
        self.token = response.json().get('token', None)

    @task(1)
    def get_all_items(self):
        self.client.get(
            '/objects',
            headers={'Authorization': self.token} if self.token else {}
        )

    @task(3)
    def get_one_item(self):
        random_id = random.choice([1, 2, 3, 4])
        self.client.get(
            f'/objects/{random_id}',
            headers={'Authorization': self.token} if self.token else {}
        )

    @task(2)
    def create_item(self):
        payload = {
            "name": f"MODEL {random.randint(100, 999)}",
            "data": {
                "generation": f"{random.randint(100, 200)}th",
                "capacity GB": random.randint(1000, 6000)
            }
        }
        self.client.post(
            '/objects',
            json=payload,
            headers={'Authorization': self.token} if self.token else {}
        )

    @task(2)
    def update_item(self):
        item_id = random.choice([1, 2, 3, 4])
        payload = {
            "name": "UPDATED MODEL 2024",
            "data": {
                "generation": "15th",
                "capacity GB": 5000
            }
        }
        self.client.put(
            f'/objects/{item_id}',
            json=payload,
            headers={'Authorization': self.token} if self.token else {}
        )

    @task(2)
    def partially_update_item(self):
        item_id = random.choice([1, 2, 3, 4])
        payload = {
            "data": {
                 "generation": "Updated Gen"
            }
        }
        self.client.patch(
            f'/objects/{item_id}',
            json=payload,
            headers={'Authorization': self.token} if self.token else {}
        )

    @task(2)
    def delete_item(self):
        item_id = random.choice([1, 2, 3, 4])
        self.client.delete(
            f'/objects/{item_id}',
            headers={'Authorization': self.token} if self.token else {}
        )
