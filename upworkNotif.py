import requests
from twilio.rest import Client
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)

def call_me(account_sid,auth_token):
    
    client = Client(account_sid, auth_token)

    call = client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to="+905373505440",
    from_="+15084440053"
    )

    print(call.sid)
call_me()
url = "https://www.upwork.com/api/v3/rooms/rooms/simplified?limit=20&callerOrgId=1635941522425393153"
payload = {}
headers = {
  'authority': 'www.upwork.com',
  'accept': 'application/json',
  'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
  'authorization': 'bearer oauth2v2_4640459327591c3c64d57e9ea915475c',
  'content-type': 'application/json',
  'cookie': 'visitor_id=212.253.217.141.1695134495681000; _cq_duid=1.1695134495.7qR8gypVeUoNdqBS; _tt_enable_cookie=1; _ttp=vsN-bhg_HyzalPn4xwo8VaNbewF; G_ENABLED_IDPS=google; spt=56e8a7bc-e660-4f4e-abbd-b7f623838421; __pdst=5ec3dd6c006f4014a59084005ce05c73; _zitok=3973506955eebefc89ad1695134498; g_state={"i_l":0}; OptanonAlertBoxClosed=2023-09-19T14:41:46.846Z; recognized=aef681ff; _ga_KSM221PNDX=deleted; ftr_ncd=6; forterToken=dfecfc65f2db4131b83f37c6806d0790_1695732236880_18183_UDF4_9ck; _gcl_au=1.1.1272736179.1704122904; __cflb=02DiuEXPXZVk436fJfSVuuwDqLqkhavJaxgxqFPPvj9q5; _gid=GA1.2.256939602.1706285356; console_user=aef681ff; current_organization_uid=1635941522425393153; company_last_accessed=d1029890502; 3d37617bsb=oauth2v2_6005d7930ec56fc7895f3dffe2e15a7b; device_view=full; 6836cbbsb=oauth2v2_c57f8b3fb08cf4b8e35826d48fed6a90; d09c4e0asb=oauth2v2_160a28358210d17dc40e45eb06b8f843; a529faf4sb=oauth2v2_fc14bb5c95f50942e7f736f007e1a2a5; _ga_KSM221PNDX=deleted; UniversalSearchNuxt_vt=oauth2v2_1dc0454361fe8752bf8e830a36e0fd1c; e32350f7sb=oauth2v2_cbce417fe543eef07c2e8c0aac417e2a; DA_aef681ff=f0cd061d85e5ded0aa9069715dd1c7fd7f072d7a03076fc986edfd7a8a10f10b; __zlcmid=1K0mS2cKkUvWkbx; _ga_SB157S2R94=GS1.2.1706303063.1.1.1706303075.48.0.0; profile_vv_gql_token=oauth2v2_b73a9ab20c078b9eb72f9e615d4ffb0c; att_vt=oauth2v2_1e4ece0e3ce15358b331c97c3c80d3b2; country_code=TR; cookie_prefix=; cookie_domain=.upwork.com; _cfuvid=2Q2a.UB18rhAAT5nmXhzx2ym.7ZFTGvUs9G_sykykic-1706346517171-0-604800000; user_uid=1635941522425393152; master_access_token=368bc5c9.oauth2v2_dd19216bf16e0a41dc71af5c7afa4c43; oauth2_global_js_token=oauth2v2_21a690b474efecd0e210aed5fa3917df; 2325f0e8sb=oauth2v2_3b9bfb009bea5db52707a8c8c5ed557d; user_oauth2_slave_access_token=368bc5c9.oauth2v2_dd19216bf16e0a41dc71af5c7afa4c43:1635941522425393152.oauth2v2_96e1a19de72f316fadb4ba6b1e23ff34; _cq_suid=1.1706346519.R2lfCIUdFHVW2OWQ; IR_gbd=upwork.com; asct_vt=oauth2v2_9e402c668e8c8858cfd63343c9ab4f7d; __cf_bm=LGw4peXIvEuLnAFmKpggH5aaRtQ7LaAlY0fM8F2Vqdk-1706350862-1-AZ9w35uIqkfsqoUAbO33RXCWZPcxQG85AHrykuARE4O3//aEG5DKEyX7EPreLreTjvE7d02PVhQQ06/XJNlbW5E=; _sp_ses.2a16=*; _upw_ses.5831=*; ftr_blst_1h=1706351481663; _dc_gtm_UA-62227314-1=1; vjd_gql_token=oauth2v2_65fdd8db859a9e27aa4b207909e0172c; _sp_id.2a16=e8f349cb-3608-4db7-aec3-63c78ab04c2f.1695680989.12.1706351530.1706346901.814e8faa-3083-440f-9340-d9558b59a191; _ga=GA1.1.753351783.1695134496; _rdt_uuid=1695134497337.4c17d5ba-92c2-416b-8b3a-5523146ae913; IR_13634=1706351530461%7C0%7C1706351482174%7C%7C; _uetsid=57e05650bc6511eeb67c132db4ad8dd6; _uetvid=a32902f056fa11ee854e290f231856bc; XSRF-TOKEN=3a5c3c3d5802ba34ad5b04b6fcc47f9c; AWSALB=u/FRCwQ2V5BP11MFzHsSlTdQC1GUSGh4y+1wPb0sL+K85a1BwpjzN2umTp1kWIov5Ojf1rsqbmIuyxMRgVx/Qho+w0oEbamvje6T//gHyZHxk+N8U/viWraVhY/x; AWSALBCORS=u/FRCwQ2V5BP11MFzHsSlTdQC1GUSGh4y+1wPb0sL+K85a1BwpjzN2umTp1kWIov5Ojf1rsqbmIuyxMRgVx/Qho+w0oEbamvje6T//gHyZHxk+N8U/viWraVhY/x; umq=854; _upw_id.5831=a39e8044-a568-4a67-ba91-b0e5d96b96cb.1695134496.40.1706351539.1706303634.3f09e99e-91f1-45cd-b5b9-3de7e9ec7f28.f28026db-d80f-4065-9ce6-4f7392e30e24.15eb0e3f-cab1-4ab6-9039-590e0d5d9024.1706346519122.347; _ga_KSM221PNDX=GS1.1.1706351482.45.1.1706351539.0.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jan+27+2024+13%3A32%3A19+GMT%2B0300+(GMT%2B03%3A00)&version=202305.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=cab1f0f9-c95b-4d22-b346-1c51c1b8693c&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=TR%3B35; enabled_ff=air2Dot76,^!RMTAir3Hired,TONB2256Air3Migration,^!CI10270Air2Dot5QTAllocations,FLSAir3,^!RMTAir3Home,CI9570Air2Dot5,^!CLOBSNAIR3,^!CLOBJNAIR3,^!air2Dot76Qt,^!CLOBJPGV2RJP,CI11132Air2Dot75,^!CI10857Air3Dot0,^!SSINavUser,^!RMTAir3Talent,^!i18nGA,OTBnrOn,^!CI12577UniversalSearch,i18nOn,SSINavUserBpa,JPAir3,^!MP16400Air3Migration; forterToken=dfecfc65f2db4131b83f37c6806d0790_1706351539782_18183_UDF43_14ck; __cf_bm=Zv6xkjrvjKRhIXN5CBVrPkQRnX6UsqUauHLWtHeq1Co-1706351578-1-Abe4vawdF/d7R+lKUP6zdw7XNUCCK6QpoDf+ecxMrwVfyRhJORhQbcfuyH5opOUxm1NQTCQuhQwmss0te2Z3Ql4=; _cfuvid=tXA2s3gDFTawWhz40y7A2o5_qwL8FyL5pa5BW5dUu60-1706351578955-0-604800000',
  'referer': 'https://www.upwork.com/ab/messages/rooms/',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.225", "Google Chrome";v="120.0.6099.225"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-viewport-width': '854',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'vnd-eo-orguid': '1635941522425393153',
  'x-upwork-accept-language': 'en-US',
  'x-upwork-api-tenantid': '1635941522425393153'
}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text)
rooms=json_data["rooms"]
for room in rooms:
    if("Upwork" in room["roomName"]):
        continue
    elif(room["numUnread"]!=0):
        call_me()
        break
    print(room["roomName"],room["numUnread"])    
