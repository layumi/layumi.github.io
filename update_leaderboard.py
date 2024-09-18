import os

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

"""
with open('./_pages/Awesome-Geolocalization.md', 'w') as file:
    file.write(metadataGEO)
os.system("curl -L https://raw.githubusercontent.com/layumi/University1652-Baseline/refs/heads/master/State-of-the-art/README.md >> ./_pages/Awesome-Geolocalization.md")



metadataAR="""---
title: \"Awesome reID\"
collection: pages
permalink: /Awesome-reID
author_profile: false
---

"""
with open('./_pages/Awesome-reID.md', 'w') as file:
    file.write(metadataAR)
os.system("curl -L https://raw.githubusercontent.com/layumi/Person_reID_baseline_pytorch/master/leaderboard/README.md  >> ./_pages/Awesome-reID.md")
