import itchat
import csv

itchat.auto_login()
#itchat.send('好玩的itchat', toUserName='filehelper')

friends = itchat.get_friends(update=True)
"""
for friend in friends:
    print(friend)
"""

fp = open('friend1.csv','w',newline='',encoding='utf-8')
writer = csv.writer(fp)

writer.writerow(['NickName','Sex','Province','City','Signature'])

for friend in friends[1:]:
    writer.writerow([friend['NickName'],friend['Sex'],friend['Province'],friend['City'],friend['Signature']])

itchat.logout()