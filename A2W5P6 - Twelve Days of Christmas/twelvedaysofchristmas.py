def next_verse(verse_number: int) -> str:
    days = ["1st", "2nd", "3rd", "4th", "5th", "6th",
            "7th", "8th", "9th", "10th", "11th", "12th"]
    gifts = [
        "A partridge in a pear tree",
        "Two turtledoves",
        "Three French hens",
        "Four calling birds",
        "Five gold rings (five golden rings)",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming"
    ]
    header = f"On the {days[verse_number - 1]} day of Christmas, my true love sent to me "
    current_gifts = gifts[:verse_number][::-1]
    if verse_number == 1:
        return header + current_gifts[0]
    else:
        main_list = ", ".join(current_gifts[:-1])
        return f"{header}{main_list} And {current_gifts[-1]}"


if __name__ == "__main__":
    for day in range(1, 13):
        print(next_verse(day))