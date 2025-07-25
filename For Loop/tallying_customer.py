

"""
Problem 2: Tallying Customer Feedback Tags
The Scenario:
Imagine you are working on a customer support dashboard. When customers leave feedback, they often use single-word tags to describe their experience, like "fast", "helpful", "slow", "confusing", etc.

You have a long string containing all the tags from one day, separated by spaces. Your manager wants a report that shows how many times each specific tag was used. This will help the company understand what customers are saying most often.

Your Task:
Write a Python function called tally_feedback_tags that takes a single string of space-separated tags as an argument. The function should return a dictionary where:

The keys are the unique tags (words).

The values are the number of times each tag appeared in the string.
"""


def tally_feedback_tags(user_input):
    values = user_input.lower().split()
    feedback = {}
    for val in values:
        if val in feedback:
            feedback[val] += 1
        else:
            feedback[val] = 1
    return feedback
user_input = "good bad slow good bad slow bad"
print(tally_feedback_tags(user_input))