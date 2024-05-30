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


coauthor_dict={}
coauthor_dict['yi-yang'] = 'https://zdzheng.xyz/files/yi-yang.jpeg'
coauthor_dict['liang-zheng'] = 'https://zdzheng.xyz/files/liang-zheng.jpg'
coauthor_dict['zhun-zhong'] = 'https://zdzheng.xyz/files/zhun-zhong.jpg'
coauthor_dict['zhiding-yu'] = 'https://zdzheng.xyz/files/zhiding-yu.jpeg'
coauthor_dict['xiaodong-yang'] = 'https://zdzheng.xyz/files/xiaodong-yang.jpg'
coauthor_dict['yutian-lin'] = 'https://zdzheng.xyz/files/yutian-lin.jpeg'
coauthor_dict['yunchao-wei'] = 'https://zdzheng.xyz/files/yunchao-wei.jpeg'
coauthor_dict['tat-seng-chua'] = 'https://zdzheng.xyz/files/tat-seng-chua.jpeg'
coauthor_dict['xiaohan-wang'] = 'https://zdzheng.xyz/files/xiaohan-wang.jpeg'
coauthor_dict['tingyu-wang'] = 'https://zdzheng.xyz/files/tingyu-wang.jpeg'
coauthor_dict['xin-yu'] = 'https://zdzheng.xyz/files/xin-yu.jpeg'
coauthor_dict['chuchu-han'] = 'https://zdzheng.xyz/files/chuchu-han.jpeg'
coauthor_dict['wei-ji'] = 'https://zdzheng.xyz/files/wei-ji.jpeg'
coauthor_dict['bingwen-hu'] = 'https://zdzheng.xyz/files/bingwen-hu.jpeg'
coauthor_dict['ping-liu'] = 'https://zdzheng.xyz/files/ping-liu.jpeg'
coauthor_dict['yu-wu'] = 'https://zdzheng.xyz/files/yu-wu.jpeg'
coauthor_dict['yaxiong-wang'] = 'https://zdzheng.xyz/files/yaxiong-wang.jpeg'
coauthor_dict['xuanmeng-zhang'] = 'https://zdzheng.xyz/files/xuanmeng-zhang.jpeg'
coauthor_dict['ruijie-quan'] = 'https://zdzheng.xyz/files/ruijie-quan.jpg'
coauthor_dict['qingji-guan'] = 'https://zdzheng.xyz/files/qingji-guan.jpeg'
coauthor_dict['mu-chen'] = 'https://zdzheng.xyz/files/mu-chen.jpeg'
coauthor_dict['linchao-zhu'] = 'https://zdzheng.xyz/files/linchao-zhu.jpeg'
coauthor_dict['zhiming-luo'] = 'https://zdzheng.xyz/files/zhiming-luo.jpeg'
coauthor_dict['jinliang-lin'] = 'https://zdzheng.xyz/files/jinliang-lin.jpeg'
coauthor_dict['leigang-qu'] = 'https://zdzheng.xyz/files/leigang-qu.jpeg'
coauthor_dict['yifan-sun'] = 'https://zdzheng.xyz/files/yifan-sun.jpeg'
coauthor_dict['tao-ruan'] = 'https://zdzheng.xyz/files/tao-ruan.jpeg'
coauthor_dict['hao-fei'] = 'https://zdzheng.xyz/files/hao-fei.jpeg'
coauthor_dict['hongxia-yang'] = 'https://zdzheng.xyz/files/hongxia-yang.jpeg'
coauthor_dict['shuai-bai'] = 'https://zdzheng.xyz/files/shuai-bai.jpeg'
coauthor_dict['chang-zhou'] = 'https://zdzheng.xyz/files/chang-zhou.jpeg'
coauthor_dict['errui-ding'] = 'https://zdzheng.xyz/files/errui-ding.jpeg'
coauthor_dict['nenggan-zheng'] = 'https://zdzheng.xyz/files/nenggan-zheng.jpg'

aff_dict={}
aff_dict['Yi-Yang'] = 'Professor @ ZJU'
aff_dict['Tat-Seng-Chua'] = 'Professor @ NUS'
aff_dict['Linchao-Zhu'] = 'AP @ ZJU'
aff_dict['Liang-Zheng'] = 'Senior Lecturer @ ANU'
aff_dict['Zhun-Zhong'] = 'AP @ the University of Trento'
aff_dict['Zhiding-Yu'] = 'Senior Scientist @ Nvidia'
aff_dict['Yutian-Lin'] = 'AP @ Wuhan University'
aff_dict['Yunchao-Wei'] = 'Professor @ Beijing Jiaotong University'
aff_dict['Tingyu-Wang'] = 'AP @ Hangzhou Dianzi University'
aff_dict['Xuanmeng-Zhang'] = 'PhD Student @ UTS'
aff_dict['Leigang-Qu'] = 'PhD Student @ NUS'
aff_dict['Mu-Chen'] = 'PhD Student @ UTS'
aff_dict['Xu-Zhang'] = 'PhD Student @ ZJU'
aff_dict['Yifan-Sun'] = '@ Baidu Research'
aff_dict['Errui-Ding'] = '@ Baidu Research'


html_filename_total = []

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
            if html_filename in html_filename_total:
                html_filename += '_1'
            html_filename_total.append(html_filename)
            #Build Citation from text
            citation = ""
            allauthor = ""
            doi = ""
            keywords=" "
            single_authors = []
            if "doi" in b.keys():
                doi = b["doi"]
            
            lower_title = clean_title.lower()
            if "re-identification" in lower_title or "reidentification" in lower_title or "retrieval" in lower_title:
                keywords += "object re-identification, " 
                keywords += "image retrieval, "
                
            if "person" in lower_title or "pedestrian" in lower_title or "human" in lower_title:
                keywords += "person re-id, "
                keywords += "person retrieval, "
                keywords += "person search, "
                
            if "adaptation" in lower_title or "domain" in lower_title:
                keywords += "domain adaptation, "
                
            if "geo-localization" in lower_title:
                keywords += "visual geo-localization, " 
                
                
            for author in bibdata.entries[bib_id].persons["author"]:
                #print(author)
                citation = citation+" "+author.first_names[0]+" "+author.last_names[0]+", "
                #allauthor = allauthor +" "+author.first_names[0]+" "+author.last_names[0]+", "
                coname = author.first_names[0]+"-"+author.last_names[0].replace('*','')
                coname = coname.lower()
                if author.first_names[0]=="Zhedong":
                    allauthor = allauthor+"<strong><a href=\"https://zdzheng.xyz/authors/"+ author.first_names[0]+"-"+author.last_names[0].replace('*','')+"\" class=\"author\">" + author.first_names[0]+" "+author.last_names[0] + "</a></strong>" +", "
                elif coname in coauthor_dict: # add icon
                    allauthor = allauthor + "<a href=\"https://zdzheng.xyz/authors/"+ author.first_names[0]+"-"+author.last_names[0].replace('*','')+"\" class=\"author\"> <img src= \"" + coauthor_dict[coname] + "\" alt=\"%s\""%coname + " style=\"border-radius: 50%; height:20px; width:20px\">" + author.first_names[0]+" "+author.last_names[0] + "</a>" +", "
                else:
                    allauthor = allauthor+"<a href=\"https://zdzheng.xyz/authors/"+ author.first_names[0]+"-"+author.last_names[0].replace('*','')+"\" class=\"author\">" + author.first_names[0]+" "+author.last_names[0] + "</a>" +", "
                authors_filename = author.first_names[0]+"-"+author.last_names[0].replace('*','')+".md"
                single_authors.append(authors_filename)
                if not os.path.isfile("../_authors/" + authors_filename):
                    with open("../_authors/" + authors_filename, 'w') as f:
                        single_author = "---\ntitle: \""   + author.first_names[0]+" "+author.last_names[0]  + '"\n'
                        f.write(single_author)
                        f.write("""collection: authors""")
                        f.write("""\npermalink: /authors/""" +author.first_names[0]+"-"+author.last_names[0])
                        f.write("""\nauthor_profile: false""")
                        #coname = author.first_names[0]+"-"+author.last_names[0]
                        if coname in coauthor_dict:
                            f.write("""\nimg: """ + coauthor_dict[coname])
                        f.write("\n---") 
                        if coname in aff_dict:
                            f.write("""\n<i>""" + aff_dict[coname]+ """</i>""")
                        #    f.write("\n <img " + "src='"+coauthor_dict[coname] + "', alt='" + coname + "', width=30%"+ ">")                       
            allauthor =  allauthor[0:-2]
            #allauthor = allauthor.replace("Zhedong Zheng","<strong>Zhedong Zheng</strong>")
            #citation title
            citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            #add venue logic depending on citation type
            venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")

            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."
            
            for single_author in single_authors:
                with open("../_authors/" + single_author, 'a') as f:
                    f.write("\n <li>" + html_escape(citation) + "<a href='https://zdzheng.xyz/publication/"+html_filename + "'>[Link]</a> </li>")

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

            md += "\nkeywords:" + keywords
             
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

            video = False
            if "video" in b.keys():
                if len(str(b["video"])) > 5:
                    md += "\nvideo: '" + b["video"] + "'"
                    video = True

            code = False
            if "code" in b.keys():
                if len(str(b["code"])) > 5:
                    md += "\ncode: '" + b["code"] + "'"
                    code = True

            md += "\nauthor: '" + allauthor + "'"
            md += "\nsqlauthor: '" +  '{"@type": "Person","name": "' + '{"@type": "Person","name": "'.join(name.replace('.md','"}, ').replace('-',' ') for name in single_authors) 
            md = md[0:-2]+ "'" # remove the final dot
            if "doi" in b.keys():
                md += "\ncitation: '" + html_escape(citation) + ' DOI: ' + str(doi) +"'"
            else:
                md += "\ncitation: '" + html_escape(citation) + "'"

            if "abs" in b.keys():
                md += "\nabs: '" + b["abs"] + "'"
            md +="\npub_year: '" + html_escape(pub_year)+"'"

            bibx = "\nbib: >\n    " + bibdata.entries[bib_id].to_string('bibtex')[:-3] + "\n    }\n"
            md += bibx.replace(',\n', ',<br>').replace('<br>    ','<br>')
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
