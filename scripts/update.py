#!/usr/bin/env python3
"""Refresh GitHub top-50 lists by category. Python standard library only."""
import datetime, json, os, pathlib, time, urllib.parse, urllib.request, urllib.error
ROOT=pathlib.Path(__file__).resolve().parents[1]
categories=json.loads((ROOT/'categories.json').read_text(encoding='utf-8'))
headers={'Accept':'application/vnd.github+json','User-Agent':'OpenSource-Atlas','X-GitHub-Api-Version':'2022-11-28'}
if os.getenv('GITHUB_TOKEN'): headers['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
result={'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'categories':[]}
for cat in categories:
    query=cat['query']+' fork:false archived:false'
    url='https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':query,'sort':'stars','order':'desc','per_page':50})
    req=urllib.request.Request(url,headers=headers)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req,timeout=40) as response: payload=json.load(response)
            break
        except urllib.error.HTTPError as exc:
            if exc.code not in (403,429) or attempt == 3: raise
            print('Rate limit, waiting 90 seconds',flush=True)
            time.sleep(90)
    rows=[]
    for rank,r in enumerate(payload['items'],1):
        rows.append({'rank':rank,'name':r['full_name'],'url':r['html_url'],'description':r.get('description') or '', 'stars':r['stargazers_count'],'language':r.get('language') or '', 'license':(r.get('license') or {}).get('spdx_id') or 'Unknown','updated_at':r.get('pushed_at') or '', 'topics':r.get('topics') or []})
    result['categories'].append({'id':cat['id'],'name':cat['name'],'name_en':cat['name_en'],'group':cat['group'],'group_name':cat['group_name'],'group_name_en':cat['group_name_en'],'repositories':rows,'total_count':payload.get('total_count',0)})
    print(cat['id'],len(rows),flush=True)
    time.sleep(7)
(ROOT/'docs'/'data.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
