import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch data from an API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to fetch data: {response.status_code}")

# Step 2: Convert data to a DataFrame
df = pd.DataFrame(data)

# Step 3: Simple Visualization
# Visualize the count of posts per user
user_post_counts = df['userId'].value_counts()

user_post_counts.plot(kind='bar', color='skyblue', figsize=(8, 5))
plt.title("Number of Posts Per User")
plt.xlabel("User ID")
plt.ylabel("Number of Posts")
plt.xticks(rotation=0)
plt.show()
