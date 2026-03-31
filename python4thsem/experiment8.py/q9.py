#Write a function to calculate simple interest
def calculate_si(principle, rate, time):
    si = (principle * rate * time) / 100
    return si

p = float(input())
r = float(input())
t = float(input())
print(calculate_si(p, r, t))