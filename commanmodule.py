#ques 1
import datetime as dt
print(dt.date.today())

#ques2
import webbrowser
youtube=input("enter your search:")
webbrowser.open_new_tab('https://www.youtube.com/=%s'%youtube)

#ques3
import os
path="D:\python\assignment\comman module"
filename=listdir('.')
i=1
for file in filename:
        a=input("name of file")
        os.rename(os.path.join(path,file),os.path.join(path,a+'.jpg'))
        i=i+1
