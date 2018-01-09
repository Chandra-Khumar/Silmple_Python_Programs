import pandas as pd
frame1 = pd.DataFrame({'key':range(5),'frame1':['a','b','c','d','e']})
frame2 = pd.DataFrame({'key':range(2,7),'frame2':['g','f','t','s','w']})
s = pd.merge(frame1,frame2,on='key')
t = pd.concat([frame1, frame2],axis = 1)
print(t)