# 1- import the random module

import random
# 2- create the subjects of headline

while True:
    print("Choose Field for fake headline Generates")
    print("1. Bollywood related")
    print("2. Politics related")
    print("3. Sports related")
    print("4. Stock & Gold related")

    Field = int(input("Enter your field: "))

    if Field == 1:
        bollywood = ["Salman khan", "Sanjay Dutt", "Anushuka Sharma", "Aamir khan", "Soney Deol", "Arijit Singh", "Ranvir Kapoor"]
        bollywood_actions = ["affiars with", "arrested in", "married in", "lauched ", "latest movie hits ", "wants retired from ", "found died in"]
        bollywood_place_or_things = ["farm house", "Rajisthan", "a new project on 25-Nov", "nearly 1200 crore ", "Alia bhatt ", "bollywood carrier ", "near his villa"]

# 3 start the headline generation loop

        while True:
            subject = random.choice(bollywood)
            action = random.choice(bollywood_actions)
            place_or_thing = random.choice(bollywood_place_or_things)

            headline = f"BREAKING NEWS: {subject} {action} {place_or_thing} "
            print("\n" + headline)

            user_input = input("\nDo you want geneate another headline? (yes/no): ".strip().lower())
            if user_input == "no":
                break
        print("Thanks for using the Fake News Headline Generator. Have a fun day.....Program Closed")
    
    elif Field == 2:
        politics = ["Today, Parliament", "MP's", "Goverment", "Oppositon", "Minister"]
        politics_actions = ["accidently", "arrested in", "lauched", "lauched ", "took a ", "wants retired from ", "fallen"]
        politics_place_or_things = ["closed", "corruption", "a new project to devlopment", "new bill against government", "in india "]

        while True:
            subject = random.choice(politics)
            action = random.choice(politics_actions)
            place_or_thing = random.choice(politics_place_or_things)

            headline = f"BREAKING NEWS: {subject} {action} {place_or_thing} "
            print("\n" + headline)

            user_input = input("\nDo you want geneate another headline? (yes/no): ".strip().lower())
            if user_input == "no":
                break

        print("Thanks for using the Fake News Headline Generator. Have a fun day.....Program Closed")

    elif Field == 3:
        sports = ["Virat kohli", "IPL", "Neeraj ", "India", "Some players"]
        sports_actions = ["broke", "won gold", "will lauch", "lauched ", "took a ", "wants retired from ", "involved"]
        sports_place_or_things = ["the old record", "in March", "in javlin", "team for World Cup", "crime"]

        while True:
            subject = random.choice(sports)
            action = random.choice(sports_actions)
            place_or_thing = random.choice(sports_place_or_things)

            headline = f"BREAKING NEWS: {subject} {action} {place_or_thing} "
            print("\n" + headline)

            user_input = input("\nDo you want geneate another headline? (yes/no): ".strip().lower())
            if user_input == "no":
                break
        
        print("Thanks for using the Fake News Headline Generator. Have a fun day.....Program Closed")


    elif Field == 4:
        stock = ["Stock", "Gold", "Oil & LPG ", "Bitcoin currency", "Sensex"]
        stock_actions = ["crashed", "touches ", "out of limit", "lauched ", "high "]
        stock_place_or_things = ["to much today", "Mumbai", "the sky", "in INDIA", "day-by-day"]

        while True:
            subject = random.choice(stock)
            action = random.choice(stock_actions)
            place_or_thing = random.choice(stock_place_or_things)

            headline = f"BREAKING NEWS: {subject} {action} {place_or_thing} "
            print("\n" + headline)

            user_input = input("\nDo you want geneate another headline? (yes/no): ".strip().lower())
            if user_input == "no":
                break

        print("Thanks for using the Fake News Headline Generator. Have a fun day.....Program Closed")
    
    else:
        print("Invalid Input")
        