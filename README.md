# Yahoo!Finance webscraper


<h5>An ultimate web scraping solution for <i>Yahoo!Finance</i> historical stocks gathering...</h5>
<br>
<img src="http://vcolamatteo.altervista.org/wp-content/uploads/2018/07/yahoo_plus_python.png">


<br><p><h4 align="justify">From about September 2017 Yahoo! stopped traditional ways of doing automatic queries for getting historical stocks series.
This code, being able to go over the limitations, can scrape over the web site and collect in a text format (both a <i>.csv</i> and 
<i>.dat</i> file for each needed title) all the avaible info about stocks (<i>Date, Open, High, Low, Close, Adjusted Close, Volume</i>).</h4></p>
<br><br><br>
<b><h2>Be careful</h2> </b> 
<b>Keep in Mind </b>this is just a demo version of the code, so it has no running options and, by deafult, it is able to download
stocks present in in <i>sec.py</i> file (line <b>6</b>).
<pre>titles=["CORN", "UGA", "NDAQ", "FB", "RDS-A"]</pre> 
Then each title the time window considered is <b>3</b> years, and you could change it at line <b>78</b> of <i>functions.py</i> file:
<pre>
date_2=(addYears(date_1, -3))
</pre>
<p align="justify">For all this kind of reasons, it should be clear the main point of strength of this code is not its performance...So if you have to use it 
for downloading a lot of stocks titles you firstly have to put your hands on it for a review, keeping always in mind there's a <b>bottleneck</b> 
with your speed network...</p>

<br>
<b><h2>Main purpose</h2> </b> 
<p align="justify">This code has been posted just for trying you to solve any troubles about querying <i>Yahoo!Finance</i> servers and so it clearly needs to be 
adapted to fit your activity at best. So, feel free to change this few lines of code and reuse it as just as you think it is better...<br>
At the end (but surely not at the least!) I would be grateful to you if you'd share with me your impovements for this code...<br><b>Thanks in advance!</b></p>


<br><br>
<b><h2>Other Info</h2> </b> 
<p>Code entirely written in <b>Python 3.5.1</b>. Feel fre to contact me at: <b>v.colamatteo@yahoo.it</b></p>.
