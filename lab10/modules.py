import math
import random
import requests
import matplotlib.pyplot as plt
from flask import Flask
from datetime import datetime, timedelta

#1
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"area of the circle: {area}")
#2
names = ["darina", "atai", "sultan"]
winner = random.choice(names)
print(f"the winner is: {winner}")
#3
now = datetime.now()
print(f"current time: {now}")

future_date = now + timedelta(days=7)
print(f"date after 7 days: {future_date}")

#3
response = requests.get("http://api.github.com")
print(response.status_code)
print(response.json())

#4

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Line graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, Flask!"
if __name__ == '__main__':
    app.run(debug=True)


