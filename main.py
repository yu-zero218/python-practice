import requests

res = requests.get("https://api.github.com")

print("ステータス：", res.status_code)
print("レスポンス：", res.json())
