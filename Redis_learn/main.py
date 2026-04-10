import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# r.set("name","shiv")
print(r.get("name"))
print(r.exists("name"))
# # print(r.ping())
# r.delete("name")
# print(r.get("name"))
# print(r.exists("name"))


# r.set("otp", "abc123", ex=10)
print(r.get("otp"))

def login(user):
    if r.exists(user):
        return f"cached user: {r.get(user).decode()}"
    else:
        r.set(user, user, ex=30)
        return "new login stored in cache"

print(login("shiv"))



## DATA_STRUCTURES

# Type	         Use Case
# String	         simple key-value
# List	         queue, logs
# Hash	         objects (like dict)
# Set	             unique values
# Sorted Set	     ranking, leaderboard