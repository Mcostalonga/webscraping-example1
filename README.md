# Using "requests" and "Beautiful Soup" for web scraping.

In this folder you will find two .py files

1. WebScraping-IBOVESPA.py; and
2. IBOV-Graph.

The first one will get data from IBOV (Bovespa Index) and save it into a .csv file. You can set the time to get the data. For default, it will request and get new data every 20 seconds. You can set it inside the while loop (changing the x value in time.sleep(x)). The function "indice_IBOVESPA()" use the requests and beuatiful soup modules and "atualizarIBOV()" store the data into the .csv file.

IBOV-Graph creates a graph from the .CSV file. If you use PyCharm, you can run both scripts at the same time (First (1), then (2)).
