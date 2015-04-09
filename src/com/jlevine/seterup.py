import rtm

# TODO: jlevine - Squash this commit and all the previous stupid Markdown issue commits together.
#       I should be embarrassed.
# TODO: jlevine - Maybe find a way to get these constants dynamically from the user on the command-line.
APIKEY = ''
SHARED_SECRET = ''
TOKEN = ''

# TODO; jlevine - Move each section into a function.
if __name__ == '__main__':
    my_rtm = rtm.createRTM(APIKEY, SHARED_SECRET, TOKEN)
    time = my_rtm.timelines.create()

    # TODO: jlevine - Maybe use dotted-map for consistency with RTM API.

    general_filter = 'list:important_can_do OR list:not_important_but_due OR list:somewhat_important_can_do'

    list_5_error_filter = """
    NOT (
         list:0_due_soon OR list:1_urgent_important OR list:2_urgent
      OR list:3_important OR list:4_somewhat_important OR list:not_important
      OR location:waiting
    )
    """

    smart_smartlists = [
        {'name': 'important', 'filter': 'tag:iu OR tag:inu'},
        {'name': 'not_important', 'filter': 'tag:niu OR tag:ninu'},
        {'name': 'somewhat_important', 'filter': 'tag:siu OR tag:sinu'},
        {'name': 'due_now', 'filter': 'dueBefore:tomorrow'},
        {'name': 'not_yet', 'filter': 'location:waiting AND NOT list:due_now'},
        {'name': 'important_can_do', 'filter': 'list:important AND NOT list:not_yet'},
        {'name': 'somewhat_important_can_do', 'filter': 'list:somewhat_important AND NOT list:not_yet'},
        {'name': 'not_important_but_due', 'filter': 'list:not_important AND list:due_now'},
        {'name': 'general', 'filter': general_filter},
        {'name': '0_due_soon', 'filter': 'dueBefore:"1 week" and list:general'},
        {'name': '1_urgent_important', 'filter': 'tag:iu and list:general'},
        {'name': '2_urgent', 'filter': 'list:general AND (tag:iu OR tag:siu)'},
        {'name': '3_important', 'filter': 'list:important and list:general'},
        {'name': '4_somewhat_important', 'filter': 'list:general and list:somewhat_important'},
        {'name': '5_error', 'filter': list_5_error_filter}
    ]

    dumb_lists = ['All Tasks', 'Personal', 'Study', 'Work']
    all_lists = my_rtm.lists.getList()
    all_list_name_set = {rtm_list.name for rtm_list in all_lists.lists.list}
    dumb_list_ids = [dumb_list.id for dumb_list in all_lists.lists.list if dumb_list.name in dumb_lists]

    for dumb_list_id in dumb_list_ids:
        my_rtm.lists.delete(timeline=time.timeline, list_id=dumb_list_id)

    for smart_smartlist in smart_smartlists:
        does_list_already_exist = smart_smartlist['name'] in all_list_name_set
        if not does_list_already_exist:
            my_rtm.lists.add(timeline=time.timeline, **smart_smartlist)

    # TODO: jlevine - Uncomment (and verify) when RTM API supports adding locations.
    #                 Until then, you'll have to do it on your own. :(
    # TODO: jlevine - Don't try to make duplicate locations.
    # required_locations = [
    #     {'address': 'anywhere', 'latitude': '0', 'longitude': '0', 'name': 'anywhere', 'viewable': '1', 'zoom': '9'},
    #     {'address': 'home', 'latitude': '0', 'longitude': '0', 'name': 'home', 'viewable': '1', 'zoom': '9'},
    #     {'address': 'internet', 'latitude': '0', 'longitude': '0', 'name': 'internet', 'viewable': '1', 'zoom': '9'},
    #     {'address': 'out', 'latitude': '0', 'longitude': '0', 'name': 'out', 'viewable': '1', 'zoom': '9'},
    #     {'address': 'phone', 'latitude': '0', 'longitude': '0', 'name': 'phone', 'viewable': '1', 'zoom': '9'},
    #     {'address': 'waiting', 'latitude': '0', 'longitude': '0', 'name': 'waiting', 'viewable': '1', 'zoom': '9'},
    #     {'address': 'work', 'latitude': '0', 'longitude': '0', 'name': 'work', 'viewable': '1', 'zoom': '9'}
    # ]
    # for required_location in required_locations:
    #     my_rtm.locations.add(timeline=time.timeline, **required_location)
