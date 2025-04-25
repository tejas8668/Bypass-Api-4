from flask import Flask, request, jsonify
import time
import cloudscraper
import cfscrape
from bs4 import BeautifulSoup

app = Flask(__name__)

delay = 7

def Seturl_in(url):
    try:
        time.sleep(delay)
        client = cloudscraper.create_scraper(allow_brotli=False)
        DOMAIN = "https://set.seturl.in"
        url = url[:-1] if url[-1] == "/" else url
        code = url.split("/")[-1]
        final_url = f"{DOMAIN}/{code}"
        ref = "https://wahanmitra24.com/"
        h = {"referer": ref}

        resp = client.get(final_url, headers=h)
        if resp.status_code != 200:
            return f"Something went wrong :( Status code: {resp.status_code}"

        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}

        time.sleep(8)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)

        if r.status_code == 200:
            return r.json()["url"]
        else:
            return "Something went wrong :( Failed to fetch final URL."

    except Exception as e:
        return f"Something went wrong :( Error: {str(e)}"

def MOdijiurl_com(url):
    try:
        time.sleep(delay)
        client = cloudscraper.create_scraper(allow_brotli=False)
        DOMAIN = "https://modijiurl.com/"
        url = url[:-1] if url[-1] == "/" else url
        code = url.split("/")[-1]
        final_url = f"{DOMAIN}/{code}"
        ref = "https://mazakisan.com/"
        h = {"referer": ref}

        resp = client.get(final_url, headers=h)
        if resp.status_code != 200:
            return f"Something went wrong :( Status code: {resp.status_code}"

        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}

        time.sleep(8)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)

        if r.status_code == 200:
            return r.json()["url"]
        else:
            return "Something went wrong :( Failed to fetch final URL."

    except Exception as e:
        return f"Something went wrong :( Error: {str(e)}"

def Inshorturl(url):
    try:
        time.sleep(delay)
        client = cloudscraper.create_scraper(allow_brotli=False)
        DOMAIN = "https://inshorturl.com/"
        url = url[:-1] if url[-1] == "/" else url
        code = url.split("/")[-1]
        final_url = f"{DOMAIN}/{code}"
        ref = "https://jnvharidwar.org/"
        h = {"referer": ref}

        resp = client.get(final_url, headers=h)
        if resp.status_code != 200:
            return f"Something went wrong :( Status code: {resp.status_code}"

        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}

        time.sleep(8)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)

        if r.status_code == 200:
            return r.json()["url"]
        else:
            return "Something went wrong :( Failed to fetch final URL."

    except Exception as e:
        return f"Something went wrong :( Error: {str(e)}"

def yorurl_com(url):
    try:
        time.sleep(delay)
        client = cloudscraper.create_scraper(allow_brotli=False)
        DOMAIN = "https://go.yorurl.com/"
        url = url[:-1] if url[-1] == "/" else url
        code = url.split("/")[-1]
        final_url = f"{DOMAIN}/{code}"
        ref = "https://financebolo.com/"
        h = {"referer": ref}

        resp = client.get(final_url, headers=h)
        if resp.status_code != 200:
            return f"Something went wrong :( Status code: {resp.status_code}"

        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}

        time.sleep(8)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)

        if r.status_code == 200:
            return r.json()["url"]
        else:
            return "Something went wrong :( Failed to fetch final URL."

    except Exception as e:
        return f"Something went wrong :( Error: {str(e)}"

def Short2url(url):
    try:
        time.sleep(delay)
        client = cloudscraper.create_scraper(allow_brotli=False)
        DOMAIN = "https://last.techyuth.xyz/" #https://link.short2url.in/s8vct
        url = url[:-1] if url[-1] == "/" else url
        code = url.split("/")[-1]
        final_url = f"{DOMAIN}/{code}"
        ref = "https://links.rcccn.in/"
        h = {"referer": ref}

        resp = client.get(final_url, headers=h)
        if resp.status_code != 200:
            return f"Something went wrong :( Status code: {resp.status_code}"

        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}

        time.sleep(8)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)

        if r.status_code == 200:
            return r.json()["url"]
        else:
            return "Something went wrong :( Failed to fetch final URL."

    except Exception as e:
        return f"Something went wrong :( Error: {str(e)}"

def just2earn(url):
    try:
        time.sleep(delay)
        client = cloudscraper.create_scraper(allow_brotli=False)
        DOMAIN = "https://go.just2earn.com/" #https://link.short2url.in/s8vct
        url = url[:-1] if url[-1] == "/" else url
        code = url.split("/")[-1]
        final_url = f"{DOMAIN}/{code}"
        ref = "https://dvjobs.in/"
        h = {"referer": ref}

        resp = client.get(final_url, headers=h)
        if resp.status_code != 200:
            return f"Something went wrong :( Status code: {resp.status_code}"

        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}

        time.sleep(8)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)

        if r.status_code == 200:
            return r.json()["url"]
        else:
            return "Something went wrong :( Failed to fetch final URL."

    except Exception as e:
        return f"Something went wrong :( Error: {str(e)}"

@app.route('/api/decode_url', methods=['GET'])
def decode_seturl():
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    if "seturl.in" in url:
        final_link = Seturl_in(url)
    elif "modijiurl.com" in url:
        final_link = MOdijiurl_com(url)
    elif "inshorturl.com" in url:
        final_link = Inshorturl(url)
    elif "yorurl.com" in url:
        final_link = yorurl_com(url)
    elif "short2url.in" in url:
        final_link = Short2url(url)
    elif "just2earn.com" in url:
        final_link = just2earn(url)
    else:
        return jsonify({"error": "Unsupported URL domain"}), 400

    return jsonify({"final_url": final_link})

if __name__ == '__main__':
    app.run(debug=True)
