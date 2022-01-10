# Trandig_BOT_simulation
This project consists of creating a bot that trades on the crypto-currency market. It is armed with three strategies "trend", "Trix" and "Alligator". But before using the bot, we will have to do some backtesting. 

First, we go to the "backtest.ipynb" file to understand the strategies and their performance, there is also a nice simulation part that shows the performance of the portfolio with each strategy.  

In the second time, when we understood all the strategies , you need to use one  for this bot ,and it takes a bit of manipulation in the script.


## Stratigies and simmulation  
   

 So in the first step we have three strategies. For each strategy we have a small presentation in the backtest book with the data visualization, which helps you to understand but I indicate that the optimization of the strategies is not the best because I did it with the manual method. 
 
With the simulation, we have three simulation functions, one function for each strategy, the function takes the money as input and a data frame with the time interval and the function returns the data frame with the trades, the portfolio, the return and the performance of the portfolio with each strategy and you can see the movements of the portfolio with the market evolution. 

### warning: in the crypto market the past tells us nothing about future so don’t be so confident   

* So there is a trend strategy where we  use the moving average of 200 and 600 to make decision  policy . 

      If you want to learn more : https://learn.bybit.com/trading/how-to-use-moving-average-to-trade-crypto/  

* The Trix strategy use a triple moving average and the average of the triple moving average to make decision policy : 

       For more information see the notebook or/and  see  : https://www.youtube.com/watch?v=HEq447LrOHY&ab_channel=TRADINGRUSH     

* Finally, there’s the Aligator stratgy  where we use five indicators  but in this project, this strategy is not opptimaised  but you can understand how it’s work 


## Use a Bottrend :  

You have a script "bottred.py"  in this repository, in the 20 lines you find  

    Strg='trix'    
 
So this you make you use a strategy that you want so like  if  Strg='trix'  you use Trix and if Strg='trend’ you use trend strtigy  
And also use your ftx token to have access are you account or subaccount 


And finally, you have to make your bot in a virtual machine in Amazon or google cloud for your bot run this script all times   


references : 

https://github.com/nicolasbonnici/cryptobot 
https://discord.com/channels/866447650291318835/866447650978660443 



