Things tested, Can you explain simple technical concepts clearly ?
Can you write safe beginner-to-junior level code
Do you understand backend logic and database basics
Can you avoid common bugs
Can you learn a stack you are not yet strong in

My strongest hands-on stacks are python and javascript, but I'm comfortable with backend logic, functions, arrays, SQL, forms, state and web application concepts. I have been preparing specifically around PHP fundamentals and I am confident I can ramp up quickly

== vs ===
include/ require
sessions vs cookies
functions with validation and defaults
arrays and filtering
SQL joins
grouped queries
Gmail filtering query
DateTime
simpe react

direct, simple. practical , with one example

1. PHP fundamentals
== vs ===
== compares values after PHP may convert types
=== compares both value and type
== and === are comparison operators, == is loose while === is strict example in a comparison between 5 and '5', == will return true while === will return false

B include, require, include_once, require_once
include: warnings when file is missing, script continues
require: fatal error if file is missing, script stops
_once: same as above but prevents duplicate loading
 I use require when the file is essential, like configuration, database connection, pr core functions. I use include for optional files such as reusable sidebar or banner. The _once versions help avoid redeclaring classes or functions if a file gets loaded multiple times
 require 'config.php'; app cannot run without config
 require_once 'Database.php'; avoid class redeclaration
 include 'views/sidebar.php'; optional layout piece
 include_once 'helpers.php'; optional helper file loaded safely 
 if a misisng file should break the application, I use require. if the page can still continue in some limited way, I user include

 sessions vs cookies
 session data is store on the server, 
 cookie data is stored in the browser
 cookies can persist longer
 sessions are generally more secure for sensitive state
 essions store data on the server and only keep a session identifer in the browser, which makes them better for things like login state. Cookies store data in the client browser, so they are useful for preferences like them or remembered language, but they should not store sensitive information directly
 use cases, session: authenticated user login
 cookie: 'remember dark mode'

 session usually stays unti browser closes or session expires
 cookie can have explicit expiration date
 for sensitive data, I would avoid storing it directly in cookies

 Functions and loan calculation
