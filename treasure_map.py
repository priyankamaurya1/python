
row1= ['😀' "😃" '😄']
row2= ['😁' "😆" '😅']
row3= ['😂' "🤣" '🥰']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
treasure=(input("where you want to store your treasure"))
# horizontal=int(treasure[0])
horizontal=int(treasure[0])
vertical=int(treasure[1])
col=map[horizontal-1]
# print(col)
col[vertical-1] ="x"



