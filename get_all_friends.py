import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser
from time import time, localtime
import csv


def login(username, password):
    Browser = RoboBrowser(parser='html.parser', cache=True, multiplier=True)
    Browser.open('https://m.facebook.com')
    form = Browser.get_form('login_form')
    form['email'].value = username
    form['pass'].value = password
    Browser.submit_form(form, submit=form['login'])
    form = Browser.get_form(action='/login/device-based/update-nonce/')
    if form:
        Browser.submit_form(form)
        return Browser
    else:
        return None


def getAllFriends(Browser: RoboBrowser, writeToCSV=False, FileName='FacebookFriends.csv'):
    Browser.open('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController')
    friendsAccounts = {}
    firstTime = True
    csvFile = csvFile = open(FileName, 'w') if writeToCSV else None
    writer = csv.DictWriter(csvFile, fieldnames=['Username', 'Account Url']) if writeToCSV else None
    writer.writeheader() if writeToCSV else None

    while True:
        if firstTime:
            friendsCenter = list(Browser.find('div', {'id': 'friends_center_main'}).children)
            friendsContent = friendsCenter[2]
            nextPageCursor = friendsCenter[3].find('a')['href'] if len(friendsCenter) > 3 else None
            firstTime = False
        else:
            friendsCenter = list(Browser.find('div', {'id': 'friends_center_main'}).children)
            friendsContent = friendsCenter[1]
            nextPageCursor = friendsCenter[2].find('a')['href'] if len(friendsCenter) > 2 else None
        for item in friendsContent:
            friend = item.find('a')
            friendName = friend.text if friend.text not in friendsAccounts else friend.text + str(localtime(time()).tm_sec)
            friendsAccounts[friendName] = 'https://m.facebook.com' + friend['href']
            if writeToCSV:
                writer.writerow({'Username': friendName, 'Account Url': friendsAccounts[friendName]})
        if not nextPageCursor:
            break
        else:
            browser.open('https://m.facebook.com' + nextPageCursor)

    csvFile.close() if csvFile else None
    return friendsAccounts


def writeFriendsToCSV(fileName: "string", friendsDict: dict):
    inputFile = open(fileName + '.csv' if fileName else 'friends.csv', 'a+')
    writer = csv.DictWriter(inputFile, fieldnames=['Username', 'Facebook Profile'])
    writer.writeheader()
    for friendData in friendsDict.items():
        writer.writerow({'Username': friendData[0], 'Facebook Profile': friendData[1]})


browser = login('username', 'password')
friends = getAllFriends(browser, True)
