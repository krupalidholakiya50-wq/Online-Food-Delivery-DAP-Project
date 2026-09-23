import urllib.request
import json
import os

url = 'https://api.github.com/search/repositories?q=food+delivery+dataset&sort=stars&order=desc'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        repos = json.loads(resp.read().decode('utf-8'))['items']
        for r in repos[:15]:
            c_url = f"https://api.github.com/repos/{r['full_name']}/contents"
            c_req = urllib.request.Request(c_url, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                with urllib.request.urlopen(c_req, timeout=5) as c_resp:
                    c_files = json.loads(c_resp.read().decode('utf-8'))
                    for f in c_files:
                        if isinstance(f, dict) and f.get('name', '').endswith('.csv'):
                            print('Found CSV:', r['full_name'], '->', f['name'], '->', f['download_url'])
            except Exception:
                pass
except Exception as e:
    print('Error:', e)
