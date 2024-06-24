<h1>StockBot API:</h1><br/>
A REST CRUD API for the data found used in Politician Stock Tracker (AKA StockBot). That project can also be found on my GitHub. <br/><br/>
<p>Current Features:<br />
GET commands to retrieve information from trades, stocks, members, newestDate, and oldestDate. <br />
Filters for stocks and trades. <br/>
Authorization for specific commands<br/>
POST commands to add rows to memebers, stocks, trades, newestDate, and oldestDate. </p>

Can be run using the command: python3 -m uvicorn app.main:app --reload

Use http://localhost:8000/docs to try it out!
