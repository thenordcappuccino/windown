import sys, json, time
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
def showiso(isoname):
    iso = {
        'Windows81': '52',
        'Win10Education': '1056',
        'Win10HomeAndPro': '1060',
        'Win10HomeChina': '1061'
    }
    x = json.dumps(iso)
    x = json.loads(x)
    if(isoname == ''):
        for isos in iso:
            print(isos)
    else:
        opts = Options()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows Phone 10.0;  Android 6.0.1; Nokia; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Mobile Safari/537.36 Edge/14.14348")
        browser = Firefox(profile, firefox_options=opts)
        iso = x[isoname]
        print(iso)
        product = "document.getElementById('product-edition').innerHTML = `<option value='" + str(iso) + "' selected='selected'>dio</option>`"
        print(product)
        browser.get("https://www.microsoft.com/it-it/software-download/windows10ISO")
        time.sleep(2)
        browser.execute_script(product)
        browser.find_element_by_id('submit-product-edition').click()
        time.sleep(5)

if __name__ == '__main__':
    usage = "windows iso downloader\nusage:\n./" + sys.argv[0] + " --showiso\n./" + sys.argv[0] + " windowsISONAME"
    if(len(sys.argv) == 1):
        print(usage)
    elif(len(sys.argv) == 2):
        if(sys.argv[1] == "--showiso"):
            print('available iso:')
            showiso('')
            exit(0)
        try:
            showiso(sys.argv[1])
        except Exception as e:
            print(e)
            print('iso not found.')
    else:
        print(usage)
        exit(1)
