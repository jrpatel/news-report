## News Reporting tool

This tool is build using Python, it uses a PostgreSQL Database for Udacity NanoDegree program. 

## Installation

1. Make sure python is installed on your system.
2. Open terminal and cd to directory/locaton where you have downloaded project.
3. cd newsreport.
4. run "python report_generator.py"
5. it will ask for Choice. 
6. choose 1 for getting a report of Popular Articles, which would create a popularArticles.text file in the same          folder/directory with 3 artciles which have been accessed most in descending order with article name and total views, so most viewed article would be at  the top.
7. again it would ask for choice, choose 2 for getting a report of Popular Authors reports which would be for all the artciles wriitten by a particular author with its page views. authors with most page views gets to be at the top and so on. you willget a popularAuthors.text file created in the same directory/folder.
8. still it would let you choose 2 more times, choose 3 to learn On which days did more than 1% of requests lead to errors. it will     
   create a file errors.text with date and percentage. 
9. choose 4 to quit the program. you are free now!!!!!  :)

## Views

1. create view error_report as SELECT requests.day,100.0 * errors.error::numeric / requests.views::numeric
   AS percentage FROM requests, errors WHERE requests.day = errors.day 
   ORDER BY requests.day DESC;
2. create view errors as SELECT date(log."time") AS day, count(*) AS error FROM log WHERE log.status like
   '4%'  GROUP BY (date(log."time"))     ORDER BY (date(log."time")) DESC;
3. create view requests as SELECT date(log."time") AS day,   count(*) AS views FROM log                        
   GROUP BY (date(log."time")) ORDER BY (date(log."time")) DESC;

   
   
   
