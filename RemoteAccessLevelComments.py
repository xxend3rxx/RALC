from requests import post
from base64 import b64decode
head = {
    "Accept-Encoding": "",
    "User-Agent": "",
    "Accept": "*/*",
    "Accept-Language": "",
    "Content-Length": "82",
    "Content-Type": "application/x-www-form-urlencoded",
}
while True:
    levelid = str(input("Insert level ID (CTRL+C to exit): "))
    page = input("\nWhat page of comments? (0 for newest), (CTRL+C to exit): ")
    r = 'levelID=' + levelid + 'page=' + page + 'total=0&secret=Wmfd2893gb7'
    data = post(url='http://www.boomlings.com/database/getGJComments21.php', data=r, headers=head)
    response_text = data.text
    if response_text.startswith('2'):
        comments_data = response_text.split("|")
        for comment_data in comments_data:
            comment_parts = comment_data.split("~")
            author_name = None
            author_name_index = comment_data.find(":1~")
            if author_name_index != -1:
                author_name = comment_data[author_name_index + 3:comment_data.index("~9")]
            else:
                print('\nerror')
            comment_base64 = comment_parts[comment_parts.index('2') + 1]
            message_id = comment_parts[comment_parts.index('6') + 1].split(':')[0]
            try:
                comment = b64decode(comment_base64).decode('utf-8')
            except Exception as e:
                comment = "Unable to decode comment"
            print("Author Name:", author_name if author_name else "N/A")
            print("Comment:", comment)
            print("Message ID:", message_id)
            print("\n\n\n")
    else:
        print('error')