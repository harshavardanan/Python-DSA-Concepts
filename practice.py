def stringMatch(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
        else:
            return -1

print("hi")
haystack = "sadbutsad"
needle = "sad"
print(stringMatch(haystack, needle))