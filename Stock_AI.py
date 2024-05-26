
#___What do I need___
# * AI that decides whether the stocks its looking at would bring pos return, neg return, or no change
# * AI that then uses that decide to trade in it, figuring out when to pull out and when not to. 
# * Maybe an algorithm that finds out how well our model is performing

#___Steps___
# * #1 AI: using chat GPT api, I'll make an AI that gets told a stock market, a value to invest with,
#       and a given timeframe.
#       
# * #2 AI: Using linear trendlines, this AI will build shapes on the stocks graph and determine if it's pattern 
#          shows up as a listed pattern to look out for. If it is, it will then output what amount to raise 
#          the investment amount and whether to actually invest or not
#        
#          
#___Actual program___
# * First asks for where to invest, then it searches through Chat GPT to figure out what to invest from 0-200 
#   into the market
# * Then it actually checks the past and recent market to decide when to put in and when to put out. 
#   (the amount that this ai returns to take out/put in is directly related to what the first statement says.)

# * Using split screen webrowsers, monitor 8 markets.
# * Will be able to start from command prompt
# * 
# * 

# Using software simulation:
# * Enter in file name of the application into the cmd prompt
# * Enter in the name of the market that is being considered, and the investment amount
# * While the program is searching through Chat GPT api to determine the invest amount ratio, it will open up
#   the selected stock into a webbrowser. If the api returns that it's not worth it to invest, it will tell 
#   the user. 
# * After having both the amount ratio and the web broswer properly opened, it will ask the user if
#   they are sure to continue will the investment.
# * Then it will monitor that stock through the webbrowser and make according investments and pull outs.  
# * The program will allow for multiple webbrowsers and possibly stacking webbroswers untop of each other to
#   monitor more stocks using clock cycles.

#___Step 1___:
# Allowing the user to enter the name of the market and the investment amount

def __main__():
    
