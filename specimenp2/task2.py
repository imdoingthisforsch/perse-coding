n = input("please write a number here: ")
w = input("please write a word here: ").strip() # not counting spaces as letter (i got from chatGPT)
if len(w) > int(n):
    print("MORE")
elif len(w) < int(n):
    print("FEWER")
else:
    print("MATCH")
