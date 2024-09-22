def mad_libs():
    # Story template
    # story = """Once upon a time, in a far-off land called {}, there lived a {} {} named {}. One day, {} decided to embark on a {} journey to find the legendary {}. Along the way, {} met a {} {} and a {} {}. Together, they faced {} {} and overcame {} {}. In the end, {} found the {} and lived {} ever after."""
    print('Welcome to mad lib game\nLets start with these questions')
    # Prompt user for words
    words = {
        "place": input("Enter a location: "),
        "proper_noun": input("Enter a proper noun: "),
        "noun": input("Enter a person's name: "),
        "pronoun": input("Enter a pronoun: "),
        "adverb": input("Enter an adverb: "),
        "animal": input("Enter an animal name: ")
        
 
 
 
#        "verb": input("Enter a verb: "),

#        "plural_noun": input("Enter a plural noun: "),
#        "past_tense_verb": input("Enter a past tense verb: "),
#        "color": input("Enter a color: "),
#        "number": input("Enter a number: "),
    }

    # Story template
    story = f"""Once upon a time, in a far-off land called {words["place"]}, there lived a {words["proper_noun"]} who's named {words["noun"]}.\n  One day, {words["pronoun"]} decided to embark on a {words["adverb"]} journey to find the legendary. Along the way, {words["pronoun"]} met a {words["proper_noun"]} and a human. Together, they faced the {words["animal"]} and overcame the challenge. In the end, {words["pronoun"]} found the {words["proper_noun"]} and lived {words["pronoun"]} ever after."""


    # Print the filled story
    print(story)

