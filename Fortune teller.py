import random
b=input("Do you want to know your fortune of the day:")
def fort():
    a=input("Enter your name:")

    if b=='yes':
        print("Your fortune for the day is:")
        fortune=['An old love will come back to you.','You have a secret admirer.','Your love life will soon be happy and harmonious.',"You're intoxicating when you do what you love.",'Follow what you love and see what turns up.','You should def go for it','Everything that is was first a dream.','Enter unknown territory','Do what you love. The rest will fall into place.'
        , 'Be passionate and totally worth the chaos.','Follow what calls you','Love yourself hard.',
        'Focus on the magic of things;yourself.','Set yourself up to experience what you love.',
        'Make self care a non-negotiable.','Some things are just too heavy to haul around.','To be found, stop hiding.',
         'Self acceptance>self improvement.','All you need is love.','You will die alone and poorly dressed.',
        "If you look back, you'll soon go that way.",'You will be hungry again in one hour.',"Don't behave with cold manners.",
        'Never forget a friend. Especially if he owes you.',"You think it's a secret, but they know it.","Don't pursue happiness-create it.",
        'Nothing is so much to be feared as fear.','The real kindness comes from within you.','Fear is interest paid on a debt you mat not owe.',
        'He who throws mud loses ground.','To avoid criticism, do nothing, say nothing, be nothing.', 'Be not afraid of growing slowly, be afraid only of standing still.',
        "It's amazing how much good you can do it if you don't care who gets the credit.",'Yes by calling full, you created emptiness.',
        "Happiness isn't an outside job, it's an inside job."]
        print(random.choice(fortune))
    else:
        print("Have a nice day!!")
        exit()
    print("Do you want to continue?")
    c=input("Type 'yes or 'no':")
    if c=='yes':
        fort()
    else:
        print("Have a nice day!!")
        exit()
fort()