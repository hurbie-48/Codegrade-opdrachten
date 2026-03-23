def count_passes(**kwargs):
    count = 0
    for resultaat in kwargs.values():
        if resultaat == "Pass":
            count += 1
    return count

result = count_passes(math="Fail", science="Fail", history="Pass", english="Pass")
print(f"Aantal behaalde vakken: {result}")