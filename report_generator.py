# Client Code for Genrating a Report
import newsdb


def get_popular_articles_report():
    """ This method gets a list of popular articles from newsdb module
    and sends it to a method for writing a file along with the file name.
    """
    filename = "popularArticles.text"
    articles = newsdb.get_popular_articles()
    if len(articles) != 0:
        write_file(filename, articles)
    else:
        print("Sorry, No record found!!!")


def get_popular_authors_report():
    """ This method gets a list of popular authors from newsdb module
    and sends it to a method for writing a file along with the file name.
    """
    filename = "popularAuthors.text"
    authors = newsdb.get_popular_authors()
    print(authors)
    if len(authors) != 0:
        write_file(filename, authors)
    else:
        print("Sorry, No record found!!!")


def get_error_report():
    """ This method gets a list of errors from newsdb module
    and sends it to a method for writing a file along with the file name.
    """
    filename = "errors.text"
    errors = newsdb.bad_day()
    if len(errors) != 0:
        write_file(filename, errors)
    else:
        print("Sorry, No record found!!!")


def write_file(filename, list):
    """ This method takes list and file name as a argument , post-process the list
    of tuples, and writes seqientially into a file.
    """
    f = open(filename, "w")
    s = " -- "
    for line in list:
        t = s.join(str(i) for i in line)
        f.write(t + "\n")
    f.close()


if __name__ == '__main__':  # here when main program starts it takes user's
    # input for getting reports.
    print('choose option for getting report')
    print('1: Get Popular Articles Report')
    print('2: Get Popular Authors Report')
    print('3: Get Bad Day Report')
    print('4: Quit Reporting Tool')
    for i in range(4):  # loop will run only 4 times
        choice = int(input("Enter your Choice: "))
        if choice == 1:  # get popular articles report.
            get_popular_articles_report()
        elif choice == 2:  # get popular authors report.
            get_popular_authors_report()
        elif choice == 3:  # get popular errors report.
            get_error_report()
        elif choice == 4:  # exit the program gracefully.
            quit()
        else:
            print("wrong choice,must be a keyboard's fault!!!!")
