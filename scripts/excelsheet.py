import pandas as pd
import random

# Helper functions to generate random data
def random_name():
    first_names = ["John", "Jane", "Robert", "Alice", "Michael", "Emily", "William", "Linda"]
    last_names = ["Smith", "Doe", "Brown", "Johnson", "Davis", "Clark"]
    return random.choice(first_names) + " " + random.choice(last_names)

def random_phone_number():
    if random.choice([True, False]):
        # Returning some incorrect phone numbers for testing
        return "123456"
    return f"+44{random.randint(1000000000, 9999999999)}"

def random_street_address():
    streets = ["Main St", "High St", "King St", "Queen St", "Elm St"]
    return f"{random.randint(1, 100)} {random.choice(streets)}"

def random_email(name):
    domains = ["gmail.com", "yahoo.com", "example.com"]
    return f"{name.split()[0].lower()}.{random.randint(10,99)}@{random.choice(domains)}"

def random_city():
    cities = ["London", "Manchester", "Birmingham", "Leeds", "Liverpool", "1234"]  # 1234 is an incorrect city for testing
    return random.choice(cities)

def random_marketing_consent():
    return random.choice([0, 1, 2, 3])  # 3 is an incorrect value for testing

def random_customer_id():
    return random.randint(10, 2000)

# Generate sample data
num_samples = 100

data = {
    "full_name": [random_name() for _ in range(num_samples)],
    "phone": [random_phone_number() for _ in range(num_samples)],
    "street_address#1": [random_street_address() for _ in range(num_samples)],
    "email": [],
    "city": [random_city() for _ in range(num_samples)],
    "marketing_consent": [random_marketing_consent() for _ in range(num_samples)],
    "customer_id": [random_customer_id() for _ in range(num_samples)]
}

# Ensure email corresponds to name
for name in data["full_name"]:
    data["email"].append(random_email(name))

# Create DataFrame and save to Excel
df = pd.DataFrame(data)
df.to_excel("sample_data.xlsx", index=False)
