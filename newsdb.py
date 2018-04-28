# "Database code" for the News Reporting
import psycopg2

DBNAME = "news"


def get_popular_articles():
    """This method connects to a database a fetches the result of top 3 polular
    articles name with its views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select a.title, count(*) as views from log l, articles a where\
              l.path like '/article/%'and l.status='200 OK' and\
              REPLACE(l.path, '/article/','')  = a.slug group by l.path,\
              a.title order by views desc limit 3;")
    articles = c.fetchall()
    db.close()
    print (articles)
    return articles


def get_popular_authors():
    """This method connects to a database a fetches the result of authors
    name and page views in order of name with most page views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select  a.name, sum(r.views) as views from  (select count(*)\
             as views , a.title, a.author from log l, articles a where l.path\
             like '/article/%' and l.status='200 OK'  and\
             Replace(l.path,'/article/','') = a.slug group by l.path, a.title,\
             a.author  order by views desc) r,authors a where r.author = a.id\
             group by a.name order by views desc;")
    authors = c.fetchall()
    db.close()
    print (authors)
    return authors


def bad_day():
    """This method connects to a database a fetches the date
    and perncetage of errors when more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select day , percentage from error_report where\
       percentage > 1;")
    errors = c.fetchall()
    db.close()
    print (errors)
    return errors
