1. Before running the python notebook codes, import the datasets as follows. 

	Open cmd from the folder containing files.
	
	//Import the covid_acc.json into MongoDB using mongoimport command in command prompt. 
	mongoimport --jsonArray --db "dbname" --collection covid_acc --file covid_acc.json 

	//Import the covid_daily.json into MongoDB using mongoimport command in command prompt.
	mongoimport --jsonArray --db "dbname" --collection covid_daily --file covid_daily.json 	

	Make sure "states_india.geojson" is pasted in the home folder of python or 
	otherwise alter the code to specify local address of the said file. 
	This file is used in the code for plotting map of India.

2. After running the code for COVID map, it can take upto one minute for the map to render. 