from pygooglenews import GoogleNews
import csv

#initialization
gn = GoogleNews()

#function to search for news
def get_titles(search):
    stories = []
    search = gn.search(search)
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'title': item.title,
            'link': item.link
        }
        stories.append(story)
    return(stories)

#keywords to look up and export later
keywords = ['Shell plc',
'Royal Dutch Shell',
'Shell',
'Shell Global',
'Shell oil production',
'Shell gas operation',
'Shell renewable energy',
'Shell retail business',
'Shell lubricants',
'Shell results',
'Shell dividend',
'Shell CEO',
'Ben van beurden',
'Shell signs',
'Shell CCS',
'Shell carbon capture',
'Shell offshore',
'Shell net zero',
'Shell project',
'Shell solar',
'Shell cashflow',
'Shell capacity',
'Shell O&G',
'Shell buys',
'Shell acquires',
'Shell JV',
'Shell joint venture',
'Shell gas prices',
'Shell EV',
'Shell electricity',
'Shell charging stations',
'Shell environment',
'Shell regulation',
'Shell stock',
'Shell FTSE',
'Shell teams up with',
'Shell renewables',
'Shell buy target',
'Shell rumours',
'Shell sustainability',
'Shell news',
'Shell buyback',
'Royal Dutch Shell Global',
'Royal Dutch Shell oil production',
'Royal Dutch Shell gas operation',
'Royal Dutch Shell renewable energy',
'Royal Dutch Shell retail business',
'Royal Dutch Shell lubricants',
'Royal Dutch Shell results',
'Royal Dutch Shell dividend',
'Royal Dutch Shell CEO',
'Royal Dutch Shell signs',
'Royal Dutch Shell CCS',
'Royal Dutch Shell carbon capture',
'Royal Dutch Shell offshore',
'Royal Dutch Shell net zero',
'Royal Dutch Shell project',
'Royal Dutch Shell solar',
'Royal Dutch Shell cashflow',
'Royal Dutch Shell capacity',
'Royal Dutch Shell O&G',
'Royal Dutch Shell buys',
'Royal Dutch Shell acquires',
'Royal Dutch Shell JV',
'Royal Dutch Shell joint venture',
'Royal Dutch Shell gas prices',
'Royal Dutch Shell EV',
'Royal Dutch Shell electricity',
'Royal Dutch Shell charging stations',
'Royal Dutch Shell environment',
'Royal Dutch Shell regulation',
'Royal Dutch Shell stock',
'Royal Dutch Shell FTSE',
'Royal Dutch Shell teams up with',
'Royal Dutch Shell renewables',
'Royal Dutch Shell buy target',
'Royal Dutch Shell rumours',
'Royal Dutch Shell sustainability',
'Royal Dutch Shell news',
'Royal Dutch Shell buyback',
'Royal Dutch Shell biofuel',
'Shell biofuel',
'Shell natural gas',
'Royal Dutch Shell natural gas',
'Shell LNG',
'Royal Dutch Shell LNG',
'Court orders Shell',
'Shell appeals',
'Court orders Royal Dutch Shell ',
'Royal Dutch Shell  appeals',
'Shell industry leading',
'Royal Dutch Shell industry leading',
'Royal Dutch Shell court',
'Shell court',
'Royal Dutch Shell fined',
'Shell fined',
'Royal Dutch Shell to pay',
'Shell to pay',
'Shell lobbied',
'Royal Dutch Shell lobbied',
'Royal Dutch Shell hires',
'Shell hires',
'Royal Dutch Shell CEO on',
'Shell CEO on',
'Shell divests',
'Royal Dutch Shell divests'
]

#iterating through keywords and appending results to csv file
for word in keywords:
    to_exp = get_titles(word)
    list = []
    for entry in to_exp:
        list.append(entry.values())

    with open('UnlabeledDataset.csv', 'a') as test_file:
        file_writer = csv.writer(test_file)
        file_writer.writerows(list)





