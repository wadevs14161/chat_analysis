import re

file = open('[LINE] 尻尻車車群的聊天.txt', 'r')

line_count = 0
message_count = 0
pass_count = 0
url_count = 0
sticker_count = 0
users = []
users_msg_count = {}
 
while True:
    line_count += 1
 
    # Get next line from file
    line = file.readline()
    if "unsent" in line or "已收回訊息" in line:
        continue
    if "上午" in line or "下午" in line:
        message_count += 1
        x = re.split("\s", line)
        if x[1] and x[1] not in users:
            users.append(x[1])
        if x[1] and x[1] not in users_msg_count:
            users_msg_count[x[1]] = 0
        elif x[1] and x[1] in users_msg_count:
            users_msg_count[x[1]] += 1

    if "趴斯" in line or "pass" in line or "帕斯" in line:
        pass_count += 1
    if "http" in line:
        url_count += 1
    if "貼圖" in line:
        sticker_count += 1
 
    # if line is empty
    # end of file is reached
    if not line:
        break

print("Total :", line_count, "lines")
print("Total messages:", message_count)
print("Total stickers:", sticker_count)
print("Total 趴斯:", pass_count)
print("Total urls:", url_count)
print(users)
print(users_msg_count)

file.close()