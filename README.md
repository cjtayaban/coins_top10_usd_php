# Top 10 Coins Based on Market Cap
    #### Video Demo: https://youtu.be/FR3kdNXhDGM
    #### Description:
    This is a python project that takes the USD and PHP prices of the top 10 coins based on market cap using the coingecko.com API. The results are extracted in a .csv file. And the PHP prices of the coins are compared using a bar graph generated in a .pdf file.
The libraries that need to be installed before running the python script are listed in requirements.txt
The project.py is the file that contains the functions required to execute this project.

The test_project.py is used to test if the all the functions are working.
The program will generate exactly two files. The first one is a .csv file which contains the ID, Name, Symbol, USD Price, and the PHP Price of the top 10 coins based on market cap that are displayed in https://www.coingecko.com/. The second file is a .pdf file that displays a bar graph that compares the PHP prices of the top 10 coins.

I used the coingecko.com Coins List with Market Data API (https://api.coingecko.com/api/v3/coins/markets) because I need to filter the coins based on market cap. I decided to get only the top 10 coins since there are so many coins available for trading in the market. The documentation of this API can be found in this website (https://docs.coingecko.com/v3.0.1/reference/coins-markets)

I have passed exactly 3 parameters to the API to get exactly what I want to be displayed in the output. They were sort, vs_currency, and per_page. With sort parameter, I passed the value “market_cap_desc” to get the coins in descending order from highest market cap to lowest. With the vs_currency parameter, I passed the value “usd” for the coins_usd() function and then the value “php” for the coins_php() function. This will make sure that I get the conversions in both currencies that I want to display. For the per_page parameter, I passed the value 10 because I only want to display a small set of data for this project.
This program does not accept any system arguments or any user input. It is expected that if you run the file, it will just generate the .csv and .pdf files as a result. If you want more coins to be displayed, the parameters that were passed in the API should be changed. For this project, I hard-coded it to be exactly 10 items.
The name of the files is formatted as "coins_top10_usd_php_” + <date today> + .csv/.pdf
For testing the accuracy of the results, in test.py, I used the unittest.mock library. I cannot hard code the values in assert because the data from the API is constantly changing. The documentation can be found in this website https://docs.python.org/3/library/unittest.mock.html
For the mock response data, I have entered exactly 10 coins similar to what I am expecting for the .csv file to generate. For the prices, I just entered a value of 1 just for a placeholder since the data is constantly changing. I just made sure that the values I need are being returned as a. json response before I can parse the data to be extracted in the .csv file and the bar graph from the .pdf file.

For the bar graph, I have used the matplotlib library.
