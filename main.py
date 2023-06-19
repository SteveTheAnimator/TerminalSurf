import urllib.request

def fetch_page(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        return html
    except Exception as e:
        return str(e)

def main():
    while True:
        url = input("Enter a URL (or 'q' to quit): ")
        if url == 'q':
            break
        page = fetch_page(url)
        print(page)
        print()

if __name__ == "__main__":
    main()
