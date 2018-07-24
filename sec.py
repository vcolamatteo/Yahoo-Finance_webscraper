from functions import*



#titles=["REY.MI", "CORN", "AAPL"]
titles=["CORN", "UGA", "NDAQ", "FB", "RDS-A"]

for i in range(len(titles)):
 
 print("scraping ", titles[i], " stock quotes in action...", end='', flush=True)
 
 # dates management....
 today, date_1, code_1, date_2, code_2 = Dates_man()

 # URL generation for querying web....
 url=urlGenerator(code_1, code_2, titles)

 #print(url[0])
 #print(url[1])
 #print(url[2])

 # web scraping & HTML parsing
 data=scraping(url[i])


 # convert dates from original codes
 code2Dates(date_1, code_1, data)

 #all=np.chararray.replace(all,".0\n","\n")
 #all=np.chararray.replace(all,",  ",", ")

 # adjust file for better viewing & save final data
 saveResult(today, date_2, titles[i])
 print("done!") 
 
print("\nScarping process fully completed!")