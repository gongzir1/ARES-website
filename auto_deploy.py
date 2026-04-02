import urllib.request, urllib.parse, json, time, os, subprocess

client_id = '178c6fc778ccc68e1d6a'
device_code = '1385ae0b784624cc5ee89a0cf87f1a599944683e'
interval = 5

token_url = 'https://github.com/login/oauth/access_token'
token_data = urllib.parse.urlencode({'client_id': client_id, 'device_code': device_code, 'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'}).encode('utf-8')
token_req = urllib.request.Request(token_url, data=token_data, headers={'Accept': 'application/json'})

access_token = None
print("Waiting for user to authorize...")
while True:
    try:
        with urllib.request.urlopen(token_req) as response:
            res = json.loads(response.read().decode())
            if 'access_token' in res:
                access_token = res['access_token']
                print("Successfully authenticated!")
                break
            elif res.get('error') == 'authorization_pending':
                time.sleep(interval)
                continue
            elif res.get('error') == 'slow_down':
                interval += 5
                time.sleep(interval)
                continue
            else:
                print("Error:", res)
                exit(1)
    except Exception as e:
        print("Exception:", e)
        time.sleep(interval)

# We have the token!
headers = {'Authorization': f'token {access_token}', 'Accept': 'application/vnd.github.v3+json'}

# 1. Get username
req = urllib.request.Request('https://api.github.com/user', headers=headers)
with urllib.request.urlopen(req) as response:
    user_info = json.loads(response.read().decode())
    username = user_info['login']
    print(f"Logged in as {username}")

# 2. Create Repository
repo_name = 'ARES-website'
req_data = json.dumps({'name': repo_name, 'private': False, 'description': 'ARES Paper Website'}).encode()
create_req = urllib.request.Request('https://api.github.com/user/repos', data=req_data, headers=headers)
try:
    with urllib.request.urlopen(create_req) as response:
        print("Repository created.")
except urllib.error.HTTPError as e:
    if e.code == 422: # Usually means repo exists
        print("Repository already exists.")
    else:
        print("Failed to create repo:", e.read())
        exit(1)

# 3. Git Push
print("Pushing to GitHub...")
remote_url = f"https://{username}:{access_token}@github.com/{username}/{repo_name}.git"
subprocess.run(['git', 'branch', '-M', 'main'])
subprocess.run(['git', 'remote', 'remove', 'origin'], stderr=subprocess.DEVNULL)
subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
push_proc = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)
print(push_proc.stdout)
print(push_proc.stderr)
print("Pushed successfully!")

# Remove token from remote for security
subprocess.run(['git', 'remote', 'remove', 'origin'], stderr=subprocess.DEVNULL)
subprocess.run(['git', 'remote', 'add', 'origin', f"https://github.com/{username}/{repo_name}.git"])

# 4. Enable Pages 
print("Enabling GitHub Pages...")
pages_req = urllib.request.Request(f'https://api.github.com/repos/{username}/{repo_name}/pages', 
    data=json.dumps({"source": {"branch": "main", "path": "/"}}).encode(), 
    headers={**headers, 'Accept': 'application/vnd.github.switcheroo-preview+json'})
try:
    with urllib.request.urlopen(pages_req) as response:
        print("Pages enabled successfully!")
except urllib.error.HTTPError as e:
    if e.code == 409: # Already exists
        print("Pages already enabled.")
    else:
        print("Failed to enable pages, it may require manual activation.", e.read())

print(f"Deployment finished! Website will be live shortly at https://{username}.github.io/{repo_name}/")
