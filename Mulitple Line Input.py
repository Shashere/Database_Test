lines = []
while True:
    line = input('Enter Lines')
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
text1=text.split('\n')
print(text1)
