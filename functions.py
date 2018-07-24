import os
import numpy as np
import datetime
from datetime import date
import requests


def scraping(url, file='SecFile.txt'):
 
 # HTML recovery
 #link = "https://finance.yahoo.com/quote/CORN/history?period1=1463436000&period2=1526508000&interval=1d&filter=history&frequency=1d"
 link = "https://finance.yahoo.com/quote/REY.MI/history?period1=1431986400&period2=1526680800&interval=1d&filter=history&frequency=1d"
	
 f = requests.get(url)
 #print (f.text)

 text_file = open("SecFile.txt", "w")
 text_file.write(f.text)
 text_file.close()
 
 # HTML parsing
 with open(file, 'r+') as myfile:
   s = myfile.read()
   s=s[s.index("Volume")+6:]
   s=s[s.index("\"prices\":[{")+11:]
   s=s[:s.index("}],\"isPending\":")]
   #sostituisce alcuni campi per isolare i valori
   s=s.replace("},{","\n")
   s=s.replace("\"date\":","")
   s=s.replace("\"close\":","")
   s=s.replace("\"open\":","")
   s=s.replace("\"high\":","")
   s=s.replace("\"low\":","")
   s=s.replace("\"volume\":","")
   s=s.replace("\"adjclose\":","")  
   s=s.replace(",","  ")


  
 with open(file, "w") as text_file:
    text_file.write(s)

# cancella le linee dei dividendi...
 with open(file,"r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if "\"" not in line:
            f.write(line)
        f.truncate()  


 data = np.loadtxt(file)
 data=data.reshape(len(data),7)
 #swap the last two column...
 data[:, 5], data[:, 6] = data[:, 6], data[:, 5].copy()
 #save on file with two decimal rounded digits
 np.savetxt("SecFile.txt", data,fmt='%1.2f')
 #reload file with two decimal rounded digits
 data = np.loadtxt('SecFile.txt')
 
 # extract first row for next dates generator
 data_c=data[:,0]
 np.savetxt("row1.txt", data_c,fmt='%i')
 
 os.remove("SecFile.txt")	
 
 return data

def Dates_man():
 
 #----- dates management.... ------
 today = str(date.today().strftime("%Y,%m,%d"))
 #print(today)

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
    delta=((init-digit)/86400)	
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
	
	
def addDigit(s):
     
   s=s.replace(".0",".00")
   s=s.replace(".1",".10")
   s=s.replace(".2",".20")
   s=s.replace(".3",".30")
   s=s.replace(".4",".40")
   s=s.replace(".5",".50")
   s=s.replace(".6",".60")
   s=s.replace(".7",".70")
   s=s.replace(".8",".80")
   s=s.replace(".9",".90")
   return s
   
   
   
#---------- URLs generation... ----------#

def urlGenerator(code_1, code_2, titles):

 url=[]
 for i in range(len(titles)):
   url.append("https://finance.yahoo.com/quote/"+titles[i]+"/history?period1="+str(code_2)+"&period2="+str(code_1)+"&interval=1d&filter=history&frequency=1d")
   #print(url[i])
 return url
#----------------------------------------#


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
 
 all=np.core.defchararray.replace(all,",  ",", ")
 #tmp=all[:,[0,4]]
 tmp=all
 tmp=np.core.defchararray.replace(tmp,", "," ")
 tmp=np.core.defchararray.replace(tmp,"   ",",")
 #tmp=np.core.defchararray.replace(tmp,"   ",",")
 np.savetxt("csv.txt", tmp,fmt='%s', delimiter=",")
 np.savetxt("Stock_parsed.dat", all,fmt='%s', delimiter="   ")
 # remove tmp files...
 os.remove("row1.txt")
 
 
 
def saveResult(today, date_2, title):
 
 # adjust file for better viewing
 with open('Stock_parsed.dat', 'r+') as myfile:  
  s = myfile.read()  
  s=s.replace(".0\n","\n")
  #s=s.replace(",  ",", ")  
 
 # create new directory folder  
 dir="scraping/"+title+"/"+str(today)+"__"+str(date_2)+"/"
 dir=dir.replace(",",".")
 if not os.path.exists(dir):
    os.makedirs(dir)

 init_row="Date           Open    High    Low     Close   AdjCl   Volume\n"  
 tmp_row="Date,Open,High,Low,Close,Adj Close,Volume\n"

 with open(dir+title+".dat", "w") as text_file:
    text_file.write(init_row)
    text_file.write(s)      

 os.remove("Stock_parsed.dat")
 
 with open('CSV.txt', 'r+') as myfile:  
  s = myfile.read()  
 
 with open(dir+title+".csv", "w") as text_file:
    text_file.write(tmp_row)
    text_file.write(s)      
  
 os.remove("CSV.txt")