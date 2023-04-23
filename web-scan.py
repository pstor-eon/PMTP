import requests
import ssl

def check_website(url):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return True
    except:
        return False
    
url = "" # 웹 사이트 
if check_website(url):
    print("안전한 사이트입니다.")
else:
    print("안전하지 않은 사이트입니다.")
