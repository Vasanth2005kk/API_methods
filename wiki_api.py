import requests

url="https://www.wikidata.org/w/api.php"
query="villupuram"#input("enter the qurey:")

params={
    "action":"wbsearchentities",
    "language":"en",
    "format":"json",
    "search":query
}

data=requests.get(url=url,params=params)

print(data.json()["search"][0]["description"])