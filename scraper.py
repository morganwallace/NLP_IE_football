from __future__ import division
from optparse import OptionParser
from lxml import html
from urllib import urlopen
import time
# from time import strftime
# today=strftime("%Y-%m-%d") #today's date

def getAppCategory():
    optionparser = OptionParser()

    optionparser.add_option('-c', '--category', dest='appCategory')

    (option, args) = optionparser.parse_args()

    if not option.appCategory:
        return optionparser.error('Application Category not provided.\n Usage: --url="path.to.appurl"')

    return { 'cat' : option.appCategory }


def get_report_text(html_file_name):
    '''
    open the html from disk or url, 
    parse with lxml.html, 
    use xpath to get list of paragraphs, 
    save it.
    '''
    #intialize local variables
    paragraphs=[]

    # #if url not local file path
    if html_file_name[:4]=="http":
        html_file = urlopen(html_file_name)
    else: #local file
        html_file=open(html_file_name)

    #use lxml to parse html
    doc = html.parse(html_file).getroot()
    html_file.close()

    #xpath makes a list of all the hrefs in elements of class "card-content-link"
    paragraphs=doc.xpath('//*[@id="main-content"]/article/p/text()')
    title=doc.xpath('//*[@id="main-content"]/article/header/hgroup/h1/text()')[0]
    
    #Put paragraphs in one big string
    raw_text=""
    for p in paragraphs:
        raw_text+=p+"\n"
    # print raw_text        


    #Save it
    file_name="reports/"+title+"_raw.txt"
    save_to_txt(raw_text,file_name)
    print "IDs from "+html_file_name + " were extracted into "+file_name


def save_to_txt(text,filename):
    f=open(filename,"w")
    f.write(text.encode("ascii","replace"))
    f.close()




def main():
    # print __doc__

    # appCat = getAppCategory()
    # print appCat

    #pass local file or url to this function
    reports_file=open('report_links.txt','r')
    for report_url in reports_file.readlines():
        get_report_text(report_url)
        time.sleep(.5)#be polite



if __name__ == '__main__':
    main()
