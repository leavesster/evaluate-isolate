sandbox = {}
script = '''
import time

for i in range(5):
    print("Script is running...")
b=5
'''
eval(compile(script, '<string>', 'exec'), sandbox)
print(sandbox['b'])