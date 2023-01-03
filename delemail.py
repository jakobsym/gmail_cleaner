import ezgmail

keywords = ['Michaels', 'When I Work', 'Coursera', 'San Antonio Botanic.', 'GameStop', 'Experian', 
'Discount Tire', 'Cannaflower', 'Michaels Rewards','Flatbush', 'TurboTax', 'Medium',
'Shift', 'Gillman', 'Zoom', 'LinkedIn', 'The Green Solution', 'THRASHER', 'TradingView', 'Reebok', 'Duolingo', ]

querywords = ['Duolingo', 'Cavender', 'TRAVIS SCOTT', 'Spotify', 'Robinhood', 'FTX', 'Land Rover', 'Voyager', 
            'YouTube', 'FTP', 'Analytics Academy', 'Intuit', 'Handshake', 'Chegg', 'edX']


for i in querywords:
    emails = ezgmail.search(i, maxResults=300)
    for j in range(len(emails)):
        if len(emails) == 0:
            print("No \"{i}\" messages to delete, moving on to the next")
        else:
            emails[j].trash()
