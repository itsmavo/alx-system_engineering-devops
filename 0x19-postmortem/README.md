# Postmortem

On the Sunday of 04/06/2023, approximately 17:00(GMT+3) Kenyan Time, there was a series of repeated power outages. This led to a system-wide server outage with most servers having the showing users' the error 404 ('Oops something went wrong there'), when the expected the result would be a login screen.

I## Debugging
The issue was not discover until 0600hrs by Brian (GOATED Sys Admin) when he noted that traffic from other branches were being routed to the back up servers and the WI-FI was not working. He began error solving.

1. He ran a script on all the servers using `ps aux`. Checking `apache 2` process - `root` and `www-data` - they were unresponsive.

2. He restarted all servers and perfomed a `curl` - got a 200 OK! (Is it though?)
3. On try login into the company site with his credentials. - 'Incorrect Username / Password' Strange!
4. Looked into the database server, online, a simple `mysql> SHOW TABLES;` - Nothing
5. So began running schema scripts on the db server preparing for the massive data import that was about happen. Setting up the db tables for backup to do its thing.
6. Finally, relaxing letting `scp` do its thing from the back-up server (transferring files) - Why isn't the WI-FI working?

