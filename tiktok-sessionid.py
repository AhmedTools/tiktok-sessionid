from requests import get
session = input('- ')
url = 'https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?scene=normal&multi_login=1&account_sdk_source=app&passport-sdk-version=19&os_api=25&device_type=A5010&ssmix=a&manifest_version_code=2018093009&dpi=191&carrier_region=JO&uoo=1&region=US&app_name=musical_ly&version_name=7.1.2&timezone_offset=28800&ts=1628767214&ab_version=7.1.2&residence=SA&cpu_support64=false&current_region=JO&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=2018093009&_rticket=1628767221573&device_platform=android&iid=7396386396296286392&build_number=7.1.2&locale=en&op_region=SA&version_code=200705&timezone_name=Asia%2FShanghai&cdid=f61ca549-c9ee-450b-90da-8854423b74e7&openudid=3e5afbd3f6dde322&sys_region=US&device_id=7296396296396396393&app_language=en&resolution=576*1024&device_brand=OnePlus&language=en&os_version=7.1.2&aid=1233&mcc_mnc=2947'
headers={'Host': 'api16-normal-c-alisg.tiktokv.com', 'Cookie': 'sessionid='+session,'Accept-Encoding': 'gzip, deflate',
'User-Agent': 'com.zhiliaoapp.musically/2022107060 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.10.0.2)'}
re = get(url,headers=headers).json()
print(re)
