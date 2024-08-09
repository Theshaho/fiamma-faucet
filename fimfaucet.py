import time,requests

wallet = 'fiamma...'

url = f'https://testnet-faucet.fiammachain.io/send/fiamma/{wallet}'

def get_faucet():
        res = requests.get(url)
        print(res.json())

while True:
        try:
                get_faucet()
        except Exception as e:
                print(f'execption:',e)

        time.sleep(3600)
