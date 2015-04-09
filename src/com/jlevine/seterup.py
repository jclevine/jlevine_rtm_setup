import rtm

APIKEY = ''
SHARED_SECRET = ''
TOKEN = ''

if __name__ == '__main__':
    my_rtm = rtm.createRTM(APIKEY, SHARED_SECRET, TOKEN)
    time = my_rtm.timelines.create()

    smart_smartlists = [
        {'name': 'important', 'filter': 'tag:iu OR tag:inu'},
        {'name': 'not_important', 'filter': 'tag:niu OR tag:ninu'},
        {'name': 'somewhat_important', 'filter': 'tag:siu OR tag:sinu'},
        {'name': 'due_now', 'filter': 'dueBefore:tomorrow'},
        {'name': 'not_yet', 'filter': 'location:waiting AND NOT list:due_now'},
        {'name': 'important_can_do', 'filter': 'list:important AND NOT list:not_yet'},
        {'name': 'somewhat_important_can_do', 'filter': 'list:somewhat_important AND NOT list:not_yet'},
        {'name': 'not_important_but_due', 'filter': 'list:not_important AND list:due_now'},
        {'name': 'general', 'filter': 'list:important_can_do OR list:not_important_but_due OR list:somewhat_important_can_do'}
    ]

    dumb_lists = ['All Tasks', 'Personal', 'Study', 'Work']
    all_lists = my_rtm.lists.getList()
    dumb_list_ids = [dumb_list.id for dumb_list in all_lists.lists.list if dumb_list.name in dumb_lists]

    for dumb_list_id in dumb_list_ids:
        my_rtm.lists.delete(timeline=time.timeline, list_id=dumb_list_id)

    for smart_smartlist in smart_smartlists:
        my_rtm.lists.add(timeline=time.timeline, **smart_smartlist)
