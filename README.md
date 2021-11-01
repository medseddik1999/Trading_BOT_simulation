# Trendig_BOT_simulation
this project is about creating a bot that does trading in the market of crypto money and he is armed with strategies "trend" or "Trix" or "alligator"   but before using the bot we should do a backtest so there is three strategies to use. 

 The first is to go to backtest.ipynb chek this notebook to understand the strategies and if you want to use them there is also a nice simulation part about these strategies which tell you what did you will get if you put money in the past.   

The second time, when you understand all strategies  you use what you need  put you need to one little manipulation in the script, i will tell what and how  

Finally, you can use this to do something more interesting and you will happy if you tell me 


## Stratigies and simmulation  
   

 So, in its first step, we have three strategies, so for one strategy we have a little presentation in the notebook backtest with data visualisation, who help you to understand but I tell you also the optimisation of strategies is not the best because I do that with manual way. 
 
With simulation, we have three functions of simulation one function for strategy  so function take input usdt and a data frame with interval date time  and the function return data frame with operations, portfolio, return  and performance of the portfolio with each strategy  and you can how your portfolio move with the market 

### warning: in the crypto market the past tell us nothing about future so don’t be so happy  

So there is a trend strategy we use in this tool we use the moving average of 200 and 600 and we make decision with this tolls we have our decision set  

If you want to learn more : https://learn.bybit.com/trading/how-to-use-moving-average-to-trade-crypto/  

The Trix strategy  is using a triple moving average  and the average of the triple moving average and with these two tolls we made a set of decision : 

For more information see the notebook or/and  see  : https://www.youtube.com/watch?v=HEq447LrOHY&ab_channel=TRADINGRUSH     

Finally, there’s the Aligator stratgy  where we use five indicators  but in this project, this strategy is not opptimaised  but you can understand how it’s work 


## Use a Bottrend :  

You have a script bottred.py  in this repository, in the first lines you find  

Strg='trix'    
 
And also use your ftx token to have access are you account or subaccount 
So this you make you use a strategy that you want so like  if  Strg='trix'  you use Trix and Strg='trend’ 
 
And finally, you have to make your bot in a virtual machine in Amazon or google cloud for your bot work all times 

