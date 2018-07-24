import os
import numpy as np
import datetime
from datetime import date
import requests


def Dates_man():
 
 #----- dates management.... ------
 today = str(date.today().strftime("%Y,%m,%d"))
 print(today)

 #date_1 = datetime.datetime.strptime(today, "%Y,%m,%d") + datetime.timedelta(days=1)
 date_1 = datetime.datetime.strptime(today, "%Y,%m,%d")
 date_2=(addYears(date_1, -3)) 
 code_1=digit_initial_date_for_query(date_1)
 #print(code_1)

 ##### genero il codice della data iniziale (3 anni di diff...)
 numDays=(date_1-date_2).days
 code_2=code_1-numDays*86400
 #print ("ffffff   ",code_1,code_2)

 date_2=date_2.strftime("%Y,%m,%d")
 
 return today, date_1, code_1, date_2, code_2 

 

def addYears(d, years):
    try:
#Return same day of the current year        
        return d.replace(year = d.year + years)
    except ValueError:
#If not same day, it will return other, i.e.  February 29 to March 1 etc.        
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%b %d, %Y")
    d2 = datetime.datetime.strptime(d2, "%b %d, %Y")
    return abs((d2 - d1).days)		
		
		
def codeGenerator(digit, init):
    delta=int((init-digit)/86400)	
    print("delta:  ", delta)
    return(init+delta)

#genera il code da inserire nell'url per la data odierna...	
def digit_initial_date_for_query(current_date):

    digit_init=976089600
    d_init = str(date(2000,12,6).strftime("%Y,%m,%d"))
    d_init=datetime.datetime.strptime(d_init, "%Y,%m,%d")
    delta_days=(current_date-d_init).days
    #print("AAAAAA:  ",delta_days)
    date_query_today=digit_init+(86400*delta_days)
    #print("quesy code:   ",date_query_today)
    return (date_query_today)
	

def dateGenerator(date_1,code_1, code_2):	
    delta_days=((code_1-code_2)/86400)	
    date_2=date_1 - datetime.timedelta(days=delta_days)    
    date_2=date_2.strftime('%b %d, %Y')
    #print("date_2:  ", date_2)	
    return (date_2)

def code2Dates(date_1,code_1, data):
 #--------- dates -----------

 new_dates=[]
 
 # convert all column data....
 with open("row1.txt","r+") as f:
     new_f = f.readlines()
     f.seek(0)
     for line in new_f:
        new_dates.append(dateGenerator(date_1,code_1,int(line)))		
		 
 data=np.delete(data,0,1)
 all = data.astype(np.str)

 all=np.insert(all, 0, new_dates, axis=1)   		

 for i in range(all.shape[0]):
    for j in range(all.shape[1]-1):  # sulle colonne non considero l'ultima perche sono per forza degli interi...
        if (all[i][j][len(all[i][j])-2]=="."):
           all[i][j]=np.core.defchararray.add(all[i][j],"0")        
 
 np.savetxt("Stock_parsed.dat", all,fmt='%s', delimiter="   ")
 # remove tmp files...
 os.remove("row1.txt")
 
 
today, date_1, code_1, date_2, code_2 =Dates_man()

print(date_1, code_1, date_2, code_2)

print(dateGenerator(date_1,code_1,1526909400))