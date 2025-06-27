import os

os.system('cd markdown_generator; python pubsFromBib.py; cd ..')
os.system('cd ACMMM2023Workshop; git pull origin main; cd ..')
os.system('cd ACMMM2024Workshop-UAV; git pull origin main; cd ..')
os.system('cd ACMMM2025Workshop-UAV; git pull origin main; cd ..')
os.system('cd MORE2024; git pull origin main; cd ..')
os.system('cd MORE2025; git pull origin main; cd ..')

metadataREID="""---
title: \"Pytorch ReID\"
collection: pages
permalink: /Pytorch-ReID
author_profile: false
---

"""
with open('./Pytorch-ReID/README.md', 'w') as file:
    file.write(metadataREID)
os.system("curl -L https://raw.githubusercontent.com/layumi/Person_reID_baseline_pytorch/master/README.md >> ./Pytorch-ReID/README.md")



metadataDA="""---
title: \"Awesome Segmentation Domain Adaptation\"
collection: pages
permalink: /Awesome-SegDA
author_profile: false
---

"""
with open('./_pages/Awesome-Segmentation-Domain-Adaptation.md', 'w') as file:
    file.write(metadataDA)
os.system("curl -L https://raw.githubusercontent.com/layumi/Seg-Uncertainty/master/awesome-SegDA/README.md  >> ./_pages/Awesome-Segmentation-Domain-Adaptation.md")


metadataGEO="""---
title: \"Awesome Geo-localization\"
collection: pages
permalink: /Awesome-Geo-localization
author_profile: false
---
<style>
table, th, td {
  border: 1px solid black;
}
</style>
"""
with open('./Awesome-Geolocalization/README.md', 'w') as file:
    file.write(metadataGEO)
os.system("curl -L https://raw.githubusercontent.com/layumi/University1652-Baseline/refs/heads/master/State-of-the-art/README.md >> ./Awesome-Geolocalization/README.md")



metadataAR="""---
title: \"Awesome reID\"
collection: pages
permalink: /Awesome-reID
author_profile: false
---
<style>
table, th, td {
  border: 1px solid black;
}
</style>
"""
with open('./Awesome-reID/README.md', 'w') as file:
    file.write(metadataAR)

os.system("curl -L https://raw.githubusercontent.com/layumi/Person_reID_baseline_pytorch/master/leaderboard/README.md  >> ./Awesome-reID/README.md")

os.system("git add .; git commit -m 'auto update'; git push")

