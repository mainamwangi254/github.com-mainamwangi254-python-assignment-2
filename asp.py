marks = 29.9
results = ""
if marks < 30:
    results = "failed"
elif marks > 75:
    results = "unknown"
else:
    results = "passed"
 
print(results)