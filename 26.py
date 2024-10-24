import os
import time
# for i in os.walk('.'):
#     #print(i)
a = os.path.join("dimad\PycharmProjects\pythonProject4\.venv\Lib", "1.txt")
print(a)
a = os.path.getmtime("1.txt")
a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a))
print(a)
a = os.path.getsize("1.txt")
print(a)
a = os.path.dirname(r"dimad\PycharmProjects\pythonProject4\.venv\Lib\1.txt")
print(a)