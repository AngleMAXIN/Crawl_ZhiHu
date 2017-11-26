#/usr/bin/env python
# -*- python: utf-8 -*-

#请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           'Referer': 'https: // zhuanlan.zhihu.com /',
           'accept': 'application / json, text / plain, * / *',
           'Connection': 'keep - alive',
        'Authorization':'Bearer Mi4xMllDakF3QUFBQUFBQU1KTjZPV1FEQmNBQUFCaEFsVk5FQzhHV3dCWXczVGJ2dWhyVzV1VGpPeHV5Q1I3ZHZNWEFB|1511579920|6e267506f01001dd08087458d143d875a43069f3',
            'If-None-Match':'W/"df104a2ae3e6b6d752023e98b649e1da2dbbf5c0',
           'X-UDID':'AADCTejlkAyPTtFD1D1k-ELJZ_WTHF2hEic=|1508662375',
            'X-XSRF-TOKEN': "2|ba5d9a39|8f38fc5f8d6bfe589769f85fde70ae5b8f6eb7018a6bf814db38a95a836ffc0edb6ba20a|1511666997"
}
start_url = 'https://zhuanlan.zhihu.com/api/recommendations/columns?limit=8&offset=8&seed=7'

MONGO_URL = 'localhost'
MONGO_DB = 'ZhiHu'
MONGO_TABLE = 'zhihu'
count = 0