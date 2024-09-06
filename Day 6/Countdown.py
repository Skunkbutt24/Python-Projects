import time
countdown=int(input("Enter countdown time in seconds: "))
for n in range(countdown,0,-1):
    hour=int(n/3600)
    minute=int((n%3600)/60)
    second=int(n%60)
    print(f"{hour:2}:{minute:2}:{second:2}")
    time.sleep(1)
print("Time's Up !!!!!")