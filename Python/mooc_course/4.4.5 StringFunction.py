# 4.4.5 StringFunction.py

# str.lower() 转化为全小写
# str.upper() 转化为全大写
print("ABcd".lower())
print("ABcd".upper())

# str.spilt(sep=None) 将字符串输出列表 根据(sep)分割的部分
print("A,B,CD,E".split(","))

# str.count(sub) 返回字符串sub在原字符串中出现的次数
print("an apple a day".count("a"))

# str.replace(old, new) 以new相替换原字符串中old相
print("Python".replace("n", "n123.io"))

# str.center(width[,fillchr]) 根据宽度将字符串居中
print("python".center(20,"="))

# str.strip(chars) 去除字符串中chars中所列字符
print("= python=".strip(" np="))

# str.join(iter) 在iter每两个字符中插入一个str
print(",".join("AMDYES!"))