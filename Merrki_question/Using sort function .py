unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# Output :-[0, 3, 4, 6, 7, 8, 9, 15, 34, 56]
def function(unorder_list):                                
    i=0
    while i<len(unorder_list):
        unorder_list.sort()
        i=i+1
    print(unorder_list)
function(unorder_list)