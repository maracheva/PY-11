# Метод groups.get
CODE_GROUP = '''
var i = 0;
var group = [];
var offset = 0;
while(i < 2){
var resp = API.groups.get({
                    "user_id": %s,
                    "offset": offset,
                    "extended": %s,
                    "fields": "members_count, deactivated, status"
});
group.push(resp);
i = i + 1;
offset = offset + 1000;
}
return group;
'''

# Метод friends.get
CODE_FRIENDS = '''
var i = 0;
var friend = [];
var offset = 0;
while(i < 2){
var resp = API.friends.get({
                        "user_id": %s,
                        "offset": offset,
                        "fields": "status"
});
friend.push(resp);
i = i + 1;
offset = offset + 1000;
}
return friend;
'''

# Метод groups.isMember
CODE_ISMEMBER = '''
var group_id = Args.group_id;
var user_ids = Args.user_ids;
var members = API.groups.isMember(
                            {"group_id": %s,
                            "user_ids": %s,
                            "extended":"1",
                            "v":"5.73"});

return members;
'''

# Метод groups.Members
CODE = '''
var i = 0;
var members = [];
var offset = 0;
while(i < 2){
var resp = API.groups.getMembers({
                "group_id": %s,
                "offset": offset,
                "filter": "friends"
});
members.push(resp);
i = i + 1;
offset = offset + 1000;
}
return members;
'''