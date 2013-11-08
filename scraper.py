from __future__ import division
from optparse import OptionParser
from lxml import html
# from time import strftime
# today=strftime("%Y-%m-%d") #today's date

def getAppCategory():
    optionparser = OptionParser()

    optionparser.add_option('-c', '--category', dest='appCategory')

    (option, args) = optionparser.parse_args()

    if not option.appCategory:
        return optionparser.error('Application Category not provided.\n Usage: --url="path.to.appurl"')

    return { 'cat' : option.appCategory }


def get_ids_from_html(html_file_name):
    '''
    open the html from disk, 
    parse with lxml.html, 
    use xpath to get list of app IDs, 
    save
    '''
    #intialize local variables
    paragraphs=[]

    html_file=open(html_file_name)

    #use lxml to parse html
    doc = html.parse(html_file).getroot()
    html_file.close()

    #xpath makes a list of all the hrefs in elements of class "card-content-link"
    paragraphs=doc.xpath('//*[@id="main-content"]/article/p/text()')
    
    raw_text=""
    for p in paragraphs:
        raw_text+=p+"\n"
    print raw_text        
    ## print ids
    ## print str(len(ids))

    #Save it
    file_name=html_file_name+"_raw.txt"
    save_to_txt(raw_text,file_name)
    print "IDs from "+html_file_name + " were extracted into "+file_name


def save_to_txt(text,filename):
    f=open(filename,"w")
    f.write(text)
    f.close()




def main():
    # print __doc__

    # appCat = getAppCategory()

    # print appCat

    get_ids_from_html('example_input.html')


if __name__ == '__main__':
    main()
