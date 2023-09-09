from flask import Flask,request,make_response
import requests
import os

app = Flask(__name__)
headers={

  "Referer": "https://lovesomecommunity.com/",

  "User-Agent": "Android"
}

headers = {
        'Accept': 'image/gif, image/x-bitmap, image/jpeg, image/pjpeg,text/html,application/xhtml+xml',
        'Connection': 'Keep-Alive',
        'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36',
'referer' : "https://stream.crichd.vip/"
    }

@app.route("/")
def credit():
    return " Made With ❤️ By Proximity BD "

@app.route("/auto/<string:channel_id>.m3u8")
def handle_auto(channel_id):
    url=f"https://lovesomecommunity.com/embedcr.php?player=desktop&live={channel_id}
    res=requests.get(url,headers=headers).text
 
    
 
   
    ara=res.splitlines()
    for i,line in enumerate(ara):
        if ".ts" in line:
            ara[i]="/ts?id="+line[11:]
    print("\n".join(ara))
    
    return "\n".join(ara)
   
@app.route("/ts")
def handle_ts():
    ts_id = request.args.get("id")    


    
    response = requests.get( ts_id,headers=headers)
    print(response)
    
    return response.content
   
  

        

    



if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
