#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re


os.system('rm -r ../_publications/*')
os.system('rm -r ../_authors/*')
#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "proceeding": {
        "file" : "proceedings.bib",
        "venuekey": "booktitle",
        "venue-pretext": "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
        
    },
    "journal":{
        "file": "pubs.bib",
        "venuekey" : "journal",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    } 
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)



for pubsource in publist:    
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        try:
            pub_year = f'{b["year"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")

            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            #html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")
            html_filename = url_slug[0:8] + pub_year
            #Build Citation from text
            citation = ""
            allauthor = ""
            doi = ""
            single_authors = []
            if "doi" in b.keys():
                doi = b["doi"]
            
            for author in bibdata.entries[bib_id].persons["author"]:
                citation = citation+" "+author.first_names[0]+" "+author.last_names[0]+", "
                #allauthor = allauthor +" "+author.first_names[0]+" "+author.last_names[0]+", "
                allauthor = allauthor+"<a href=\"https://zdzheng.xyz/authors/"+ author.first_names[0]+"-"+author.last_names[0]+"\">" + author.first_names[0]+" "+author.last_names[0] + "</a>" +", "
                authors_filename = author.first_names[0]+"-"+author.last_names[0].replace('*','')+".md"
                single_authors.append(authors_filename)
                if not os.path.isfile("../_authors/" + authors_filename):
                    with open("../_authors/" + authors_filename, 'w') as f:
                        single_author = "---\ntitle: \""   + author.first_names[0]+" "+author.last_names[0]  + '"\n'
                        f.write(single_author)
                        f.write("""collection: authors""")
                        f.write("""\npermalink: /authors/""" +author.first_names[0]+"-"+author.last_names[0])
                        f.write("\n---")                        
            allauthor =  allauthor[0:-2]
            allauthor = allauthor.replace("Zhedong Zheng","<strong>Zhedong Zheng</strong>")
            #citation title
            citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            #add venue logic depending on citation type
            venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")

            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."
            
            for single_author in single_authors:
                with open("../_authors/" + single_author, 'a') as f:
                    f.write("\n <li>" + html_escape(citation) + "'" + "<a href='https://zdzheng.xyz/publication/"+html_filename + "'>[Link]</a> </li>")

            ## YAML variables
            md = "---\ntitle: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
            
            md += """collection: """ +  publist[pubsource]["collection"]["name"]

            md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
            
            note = False
            if "note" in b.keys():
                if len(str(b["note"])) > 5:
                    md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
                    note = True

            md += "\ndate: " + str(pub_date) 

            md += "\ndoi: " + doi

            md += "\nvenue: '" + html_escape(venue) + "'"
            
            url = False
            if "url" in b.keys():
                if len(str(b["url"])) > 5:
                    md += "\npaperurl: '" + b["url"] + "'"
                    url = True
            
            blog = False        
            if "blog" in b.keys():
                if len(str(b["blog"])) > 5:
                    md += "\nblog: '" + b["blog"] + "'"
                    blog = True

            code = False
            if "code" in b.keys():
                if len(str(b["code"])) > 5:
                    md += "\ncode: '" + b["code"] + "'"
                    code = True

            md += "\nauthor: '" + allauthor + "'"
            if "doi" in b.keys():
                md += "\ncitation: '" + html_escape(citation) + ' DOI: ' + str(doi) +"'"
            else:
                md += "\ncitation: '" + html_escape(citation) + "'"

            if "abs" in b.keys():
                md += "\nabs: '" + b["abs"] + "'"
            md +="\npub_year: '" + html_escape(pub_year)+"'"

            bibx = "\nbib: >\n    " + bibdata.entries[bib_id].to_string('bibtex')[:-3] + "\n    }\n"
            md += bibx.replace(',\n', ',  \n')
            md += "\n---"

            
            ## Markdown description for individual page
            if note:
                md += "\n" + html_escape(b["note"]) + "\n"

            #if url:
            #    md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
            #else:
            #    md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"

            md_filename = os.path.basename(md_filename)
            
            with open("../_publications/" + md_filename, 'w') as f:
                f.write(md)

            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue
