import trainer as tr
from main import process_test_url
from utils import Results, extract_url

def submit(link):
    url = extract_url(link)
    process_test_url(url, 'test_features.csv')
    return_ans = tr.gui_caller('url_features.csv', 'test_features.csv')
    a = str(return_ans).split()
    if int(a[1]) == 0:
        return Results.SAFE
        # answer = tkMessageBox.askquestion("Redirect","Do you want to visit the url?")
        # if answer == 'yes':
        #         webbrowser.open(url=E1.get(), new=1)
    elif int(a[1]) == 1:
        return Results.MALICIOUS
        # tkMessageBox.showinfo("URL Checker Result", "The URL " + url + " is Malicious")
        # answer_2 = tkMessageBox.askquestion("Redirect", "The url MALICIOUS, Do you still want to visit the url?")
        # if answer_2=='yes':
        #     webbrowser.open(url=E1.get(),new=1)
    else:
        # tkMessageBox.showinfo("URL Checker Result", "The URL " + url + " is Malware")
        # tkMessageBox.showwarning("Warning","Cant Redirect, url contains a malware")
        return Results.MALWARE