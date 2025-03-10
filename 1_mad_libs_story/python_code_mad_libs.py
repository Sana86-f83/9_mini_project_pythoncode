# Mad Libs Story Template
story = """
In our Python class, the [adjective1] teacher [verb1]ed a [noun1] on the [noun2]. 
The students were [adjective2] and [verb1]ed [adverb1] to understand the [noun2]. 
Suddenly, the [noun2] started [verb2]ing, and everyone [verb3]ed [adverb2] to the [place]. 
It was a [adjective3] day in Python class!
"""

# Function to get user input
def get_word(prompt):
    return input(prompt)

# Get user input for each placeholder
adjective1 = get_word("Enter an adjective: ")
verb1 = get_word("Enter a verb: ")
noun1 = get_word("Enter a noun: ")
noun2 = get_word("Enter another noun: ")
adjective2 = get_word("Enter another adjective: ")
verb2 = get_word("Enter another verb: ")
adverb1 = get_word("Enter an adverb: ")
verb3 = get_word("Enter another verb: ")
adverb2 = get_word("Enter another adverb: ")
place = get_word("Enter a place: ")
adjective3 = get_word("Enter one more adjective: ")

# Replace placeholders with user input
story = story.replace("[adjective1]", adjective1)
story = story.replace("[verb1]", verb1)
story = story.replace("[noun1]", noun1)
story = story.replace("[noun2]", noun2)
story = story.replace("[adjective2]", adjective2)
story = story.replace("[verb2]", verb2)
story = story.replace("[adverb1]", adverb1)
story = story.replace("[verb3]", verb3)
story = story.replace("[adverb2]", adverb2)
story = story.replace("[place]", place)
story = story.replace("[adjective3]", adjective3)

# Display the final story
print("\nHere's your Mad Libs story:\n")
print(story)