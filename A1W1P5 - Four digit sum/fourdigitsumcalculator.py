numbers = input()
output = ""
answer = 0
for i in range(4):
    output += (f"{numbers[i]}+")
    answer += int((numbers[i]))
output = output[:-1]
output += "="
output += str(answer)
print(output)
