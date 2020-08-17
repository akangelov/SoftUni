#Social_Media_Posts

data_list = input().split()

posts_dict = {}

while not data_list[0] == "drop":
    command = data_list[0]
    post_name = data_list[1]

    if command == "post":
        posts_dict[post_name] = {'likes': 0, 'dislikes': 0, 'comments': None}
    elif command == "like":
        if post_name in posts_dict.keys():
            posts_dict[post_name]['likes'] += 1
    elif command == "dislike":
        if post_name in posts_dict.keys():
            posts_dict[post_name]['dislikes'] += 1
    elif command == "comment":
        commentator = data_list[2]
        content = ' '.join(data_list[3:])
        if post_name in posts_dict.keys():
            if not posts_dict[post_name]['comments']:
                posts_dict[post_name]['comments'] = []

            posts_dict[post_name]['comments'].append({commentator: content})

    data_list = input().split()

for post_name, metrics in posts_dict.items():
    print(f"Post: {post_name} | Likes: {metrics['likes']} | Dislikes: {metrics['dislikes']}")
    print("Comments:")
    if metrics['comments']:
        for comment in metrics['comments']:
            for kvp in comment.items():
                print(f"*  {kvp[0]}: {kvp[1]}")
    else:
        print(None)