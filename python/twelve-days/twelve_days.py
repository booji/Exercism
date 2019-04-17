def recite(start_verse, end_verse):
    lyrics = []
    num = {1: ['first','a Partridge in a Pear Tree.'],
           2: ['second', 'two Turtle Doves,'],
           3: ['third','three French Hens,'],
           4: ['fourth','four Calling Birds,'],
           5: ['fifth', 'five Gold Rings,'],
           6: ['sixth', 'six Geese-a-Laying,'],
           7: ['seventh', 'seven Swans-a-Swimming,'],
           8: ['eighth', 'eight Maids-a-Milking,'],
           9: ['ninth', 'nine Ladies Dancing,'],
           10: ['tenth', 'ten Lords-a-Leaping,'],
           11: ['eleventh', 'eleven Pipers Piping,'],
           12: ['twelfth', 'twelve Drummers Drumming,']}

    for verse in range(start_verse,end_verse+1):
        carol = f"On the {num[verse][0]} day of Christmas my true love gave to me:"
        for day in range(verse,0,-1):
            if verse != 1 and day == 1:
                carol += ' and'
            carol += f" {num[day][1]}"
            
        carol = str(carol)
        lyrics.append(carol)

    return lyrics
