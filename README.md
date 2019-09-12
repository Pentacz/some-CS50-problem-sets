# Finance

Finance is a site where you can check, 'buy' and 'sell' New York Stock Exchange shares. You can register and login - site will remember login and require it to make transactions. At start you get 10 000 virtual dollars which you can use. Stock info is brought by API so you can get actual price of stock. Starting page has info about your cash and owned shares, while history shows every transaction you made.

Most important parts of finance are in python. There is also SQL, html, css and javascript (mostly using jquery to prompt JSON e.g.
username taken, password requirements)

In helpers.py there are defined functions made by CS50 staff to help execute some commands in application.py.
application.py is almost entirely made by me - Bartek Sikorski ;) - except first few lines (import etc), caching 
responses, login and logout. It defines rules of registration, checking passwords, and enables to quote, buy and check stocks.

In Static and Templates folders you can find layout and style made mostly but CS50 staff, but all the rest of htmls are entirely
made by me. Interesting ones are index and history.html as they make tables from finance.db (SQL), and registration and login.html
as those include AJAX JQuery.
