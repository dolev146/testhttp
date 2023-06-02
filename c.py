import requests

if __name__ == '__main__':
    b_rst = requests.get('http://localhost:5000/')
    print("test if http stream is blocked")
    print(b_rst.text)