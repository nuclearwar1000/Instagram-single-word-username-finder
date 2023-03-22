# Instagram-single-word-username-finder
Just a python web parser that checks instagram for single word usernames and prints whether its avaiable or not

Works incredibly simply, checks instagram urls picking from a list of english words,
then checks for a specific request which tells instagram whether or not the account exists by returning either a code 404 or 200 OK.

you can modify the number of names chosen by modifying the line "while x < ___:" (line 20) by default this is set to a value of 100.

It might be smart to use a vpn or run the code through a proxy ip to avoid any chances of getting blocked or timed out by instagram.
so far I haven't had to deal with that with this iteration, however it was a problem in older versions prior to posting.
