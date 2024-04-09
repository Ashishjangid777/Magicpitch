from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Scrape(BaseModel):
    name: str
    organization: str

class Scrape_results(BaseModel):
    job_id: str


@app.get("/")
async def read_root():
    return {"Hello": "Hello World"}

@app.post("/scrape")
async def scrape(body: Scrape):
    name = body.dict()['name']
    organization_name = body.dict()['organization']
    orgnization_id = orgnization(organization_name)

    cookies = {
        'remember_token_leadgenie_v2': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTJNVFJtT1RVNFpqQTFOV0V5TURGaFptTmtaalUyTmw5c1pXRmtaMlZ1YVdWamIyOXJhV1ZvWVhOb0lnPT0iLCJleHAiOiIyMDI0LTA1LTA5VDA4OjE2OjI0Ljc2OFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdG9rZW5fbGVhZGdlbmllX3YyIn19--753a6deea27410ad773be2151225d28f925afcdc',}

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://app.apollo.io',
        'referer': 'https://app.apollo.io/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-csrf-token': 'jNaxtiAFNCZaJdwwyPOvnMgGPik-NQTAiGJ35PQEJ9V04VjQCexnPNYLVvKqhFsUADRIR7UUzpYYcjPFAKol2Q',
    }

    all_ids = []
    page_number = 1
    while page_number <= 5:
        try:
            json_data = {
                'finder_table_layout_id': None,
                'finder_view_id': f'{orgnization_id}',
                'page': f'{page_number}',
                'q_keywords': f'{name}',
                'display_mode': 'explorer_mode',
                'per_page': 25,
                'open_factor_names': [],
                'num_fetch_result': 2,
                'context': 'people-index-page',
                'show_suggestions': False,
                'ui_finder_random_seed': '50phd9a0ifr',
                'cacheKey': 1712650831983,
            }

            response = requests.post('https://app.apollo.io/api/v1/mixed_people/search', cookies=cookies, headers=headers, json=json_data).json()
            all_ids.extend([data['id'] for data in response['people']])
            page_number+=1
        except:
            page_number+=1
            continue

    return {"ID": list(set(all_ids))}

@app.get("/scrape_results")
async def scrape_results(body: Scrape_results):
    emp = emp_data(body.dict()['job_id'])
    return {"Data": emp}


def orgnization(comp_name):
    cookies = {
        'mutiny.user.session_number': '1',
        'zp__utm_medium': '(none)',
        'zp__initial_utm_medium': '(none)',
        'zp__initial_utm_source': '(direct)',
        '_gcl_au': '1.1.1728192262.1712650210',
        '_ga': 'GA1.1.687701363.1712650210',
        '__hstc': '21978340.56fdcf71ed2a4a545d26a5174c9ce03b.1712650209520.1712650209520.1712650209520.1',
        'hubspotutk': '56fdcf71ed2a4a545d26a5174c9ce03b',
        '__hssrc': '1',
        '_fbp': 'fb.1.1712650213426.1029964714',
        '__q_state_xnwV464CUjypYUw2': 'eyJ1dWlkIjoiNTk5MTA2MmYtM2IzOC00NDBiLWE3NTAtNWVjOGM0ZDY4NDU2IiwiY29va2llRG9tYWluIjoiYXBvbGxvLmlvIiwibWVzc2VuZ2VyRXhwYW5kZWQiOmZhbHNlLCJwcm9tcHREaXNtaXNzZWQiOmZhbHNlLCJjb252ZXJzYXRpb25JZCI6IjEzNzEyMjc4NjYxMjI4MDY0NzMifQ==',
        '_clck': '10bvuvv%7C2%7Cfks%7C0%7C1560',
        '_cioanonid': '0a1738d2-7dc4-8b90-0347-d4796cb41049',
        'ZP_Pricing_Split_Test_Variant': '23Q4_EC_Z59',
        'zp__initial_referrer': 'https://accounts.google.com/',
        'zp__utm_source': 'accounts.google.com',
        'ps_mode': 'trackingV1',
        '_hjSession_3601622': 'eyJpZCI6IjhmZGNmNmQ4LTNkZWMtNGY1NC04OTMyLTQ0NjE1NjUyNWMyMiIsImMiOjE3MTI2NTAyOTM4MTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxfQ==',
        '_hjSessionUser_3601622': 'eyJpZCI6IjRlNDA0OTRmLWJkNGMtNTY0OS1hZjM3LWVmNGZiNDJjZDQ4ZCIsImNyZWF0ZWQiOjE3MTI2NTAyOTM4MTQsImV4aXN0aW5nIjp0cnVlfQ==',
        'remember_token_leadgenie_v2': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTJNVFJtT1RVNFpqQTFOV0V5TURGaFptTmtaalUyTmw5c1pXRmtaMlZ1YVdWamIyOXJhV1ZvWVhOb0lnPT0iLCJleHAiOiIyMDI0LTA1LTA5VDA4OjE2OjI0Ljc2OFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdG9rZW5fbGVhZGdlbmllX3YyIn19--753a6deea27410ad773be2151225d28f925afcdc',
        'ZP_LATEST_LOGIN_PRICING_VARIANT': '23Q4_EC_Z59',
        'intercom-device-id-dyws6i9m': 'b545af1b-70e0-4c96-97fe-7a9c30019f5d',
        '_cioid': '6614f958f055a201afcdf566',
        '__stripe_mid': '07a10ad3-d5d3-4484-bf78-b3ad32d547cf25db0f',
        '__stripe_sid': '7103d2a8-72cc-48f3-b096-4f8ba68d1c806f1222',
        '_ga_76XXTC73SP': 'GS1.1.1712650210.1.1.1712650775.60.0.715036812',
        'amplitude_id_122a93c7d9753d2fe678deffe8fac4cfapollo.io': 'eyJkZXZpY2VJZCI6ImFiNjQ4NzFmLWRjMmMtNDU5Ni1iZWZiLTQ0YWM0YzJmNWQyZlIiLCJ1c2VySWQiOiI2NjE0Zjk1OGYwNTVhMjAxYWZjZGY1NjYiLCJvcHRPdXQiOnRydWUsInNlc3Npb25JZCI6MTcxMjY1MDIwOTIyNywibGFzdEV2ZW50VGltZSI6MTcxMjY1MDc3NjQxNiwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6Niwic2VxdWVuY2VOdW1iZXIiOjl9',
        '__hssc': '21978340.7.1712650209521',
        'intercom-session-dyws6i9m': 'dkJKUER6b2JhVXBOdjBLVzU3dmpyOHNrTlNRelc0Y1dRbXFxWXNKUWNaMlpOQ2VGeHZQNWJWMjJaSGlUVW9mMC0tSlJac0VHM0R6RHBNUkp4M2FUcmNLZz09--6dc4a8d018afb12f4817de9256cae59f2910db6b',
        '_clsk': 'yza00p%7C1712651611621%7C4%7C0%7Ck.clarity.ms%2Fcollect',
        'GCLB': 'COD546eRudvZ7wEQAw',
        'X-CSRF-TOKEN': 'CZELa6dEqbH1fkNmWJOiDp9Isy1DeMWqJBYIfeaLvQjxpuINjq36q3lQyaQ65FaGV3rFQ8hZD_y0BkxcEiW_BA',
        '_leadgenie_session': 'X6G8Ss8yPZQVQzL4wqwxgK0%2F%2FP39qGkd2MDQDvmBI0PHi1ev3tff6v1ml2%2BEnXULM5DSzj%2BK6ymmPLAJ9qi5asTQGRUxRUiOvd3FF%2FJco4On%2FODu8sCqeTCwEyKS1OpCeQxfJyMNsm5Lr6JhKqaxIlo%2BJfS7ZCywsjRW%2BjBcmXkYjVx3S6dlWnSV%2BBPZ%2FZKMdA8sd96C6gBDJzms%2FGJEEUXPYrtJlhWEkSntYT0ac2E7Hc2W%2FJ6MDQznqbj%2FWKrmG0t2q8eMpS1ch8FX2GQv2ynm8jJsVp7EuqI%3D--B57joDKfJpxKv%2F7T--mP7E7gkdMq6YNlanxEAL%2FA%3D%3D',
        '_dd_s': 'rum=0&expire=1712652749465',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://app.apollo.io',
        'referer': 'https://app.apollo.io/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-csrf-token': 'CZELa6dEqbH1fkNmWJOiDp9Isy1DeMWqJBYIfeaLvQjxpuINjq36q3lQyaQ65FaGV3rFQ8hZD_y0BkxcEiW_BA',
    }

    json_data = {
        'q_organization_fuzzy_name': f'{comp_name}',
        'display_mode': 'fuzzy_select_mode',
        'cacheKey': 1712651850407,
    }

    response = requests.post('https://app.apollo.io/api/v1/organizations/search', cookies=cookies, headers=headers, json=json_data).json()
    company = [orgniz['id'] for orgniz in response['organizations'] if orgniz['name'].lower() == comp_name.lower()][0]
    return company

def emp_data(emp_id):

    cookies = {
        'remember_token_leadgenie_v2': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTJNVFJtT1RVNFpqQTFOV0V5TURGaFptTmtaalUyTmw5c1pXRmtaMlZ1YVdWamIyOXJhV1ZvWVhOb0lnPT0iLCJleHAiOiIyMDI0LTA1LTA5VDA4OjE2OjI0Ljc2OFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdG9rZW5fbGVhZGdlbmllX3YyIn19--753a6deea27410ad773be2151225d28f925afcdc',
        }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'content-type': 'application/json',
        'dnt': '1',
        'referer': 'https://app.apollo.io/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://app.apollo.io/api/v1/people/{emp_id}?cacheKey=1712663817572', cookies=cookies, headers=headers).json()
    return response['person']

