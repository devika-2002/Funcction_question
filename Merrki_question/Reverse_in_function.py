reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# O/P:-["D", "R", "A", "M", "E", "B", "A", "A", "Z"]
def reverse():
    i=0
    while i<len(reverse_list):
        reverse_list.reverse()
        i=i+1
    print(reverse_list)
reverse()
