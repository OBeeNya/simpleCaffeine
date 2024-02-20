import win32com.client, time

while (1):
    win32com.client.Dispatch('WScript.Shell').SendKeys('{F15}')
    time.sleep(60)
