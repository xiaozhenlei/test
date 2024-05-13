import http.client

conn = http.client.HTTPSConnection("xb.996321.xyz")
payload = ''
headers = {
   'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NiIsImlzcyI6IkNISUtBVEEiLCJ0eXBlIjoibG9naW4iLCJleHAiOjE3MTYwOTkyODV9.N1M6FRuCi2Grfgt45i61_Kfdo8uNtVSRMgRbl3MCbK0',
   'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/124.0.0.0'
}
conn.request("POST", "/user/sign", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
