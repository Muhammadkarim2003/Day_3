name1 = input(">> ")
name2 = input(">> ")

name_cambinate = name1 + name2
name_cambinate_lower = name_cambinate.lower()

t = name_cambinate_lower.count("t")
r = name_cambinate_lower.count("r")
u = name_cambinate_lower.count("u")
e = name_cambinate_lower.count("e")

true = t + r + u + e

l = name_cambinate_lower.count("l")
o = name_cambinate_lower.count("o")
v = name_cambinate_lower.count("v")
e = name_cambinate_lower.count("e")

love = l + o + v + e

score = true + love

if score < 10 or 90 < score:
    print(f"Sizning balingiz {score}, Siz birga bolasiz")
elif score >= 40 and 50 >= score:
    print(f"Siz birgasiz")
else:
    print(f"sizning balingiz {score}")
