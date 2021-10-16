from datetime import datetime
import urllib

def sampleresponses(input_text):
    user_message=str(input_text).lower()
    #about="tell me something about"
    #length=len(about)
    message1="Resource to study"
    message2="Resource to Practice"
    webUrl=''
    webUrl2=''
    flag_var=-1
    if user_message in ("hello","hi","sup"):
        return "Hey! How's it going?"
    if user_message in ("who are you", "who are you?", "whats your name", "what is your name?","What's your name","What's your name?"):
        return "My name is Data Structures and Algorithms Practice Bot"
    if user_message in ("time","time?","what's the time","what is the time?"):
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    if user_message in("dynamic programming","dp"):
        webUrl='https://www.youtube.com/watch?v=oBt53YbR9Kk'
        webUrl2='https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/'
        flag_var=1
    if user_message in ('greedy algorithms','greedy'):
        webUrl='https://www.youtube.com/playlist?list=PLqM7alHXFySESatj68JKWHRVhoJ1BxtLW'
        webUrl2='https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/'
        flag_var=1
    if 'array' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PLBlnK6fEyqRjoG6aJ4FvFU1tlXbjLBiOP'
        webUrl2='https://leetcode.com/tag/array/'
        flag_var=1
    if 'linked list' in user_message:
        webUrl='https://www.geeksforgeeks.org/data-structures/linked-list/'
        webUrl2='https://leetcode.com/tag/linked-list/'
        flag_var=1
    if 'sort' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U'
        webUrl2='https://leetcode.com/tag/sort/'
        flag_var=1
    if 'search' in user_message:
        webUrl='https://www.youtube.com/watch?v=13ocRMSJy5M'
        webUrl2='https://leetcode.com/tag/binary-search/'
        flag_var=1
    if 'number theory' in user_message:
        webUrl='https://www.youtube.com/watch?v=19SW3P_PRHQ'
        webUrl2='https://codeforces.com/blog/entry/49494'
        flag_var=1
    if 'bitmasking' in user_message:
        webUrl='https://www.youtube.com/watch?v=wEZfc6cPC4w'
        webUrl2='https://leetcode.com/tag/bit-manipulation/'
        flag_var=1
    if 'backtracking' in user_message or 'recursion' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs'
        webUrl2='https://leetcode.com/tag/backtracking/'
        flag_var=1
    if 'stack' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd'
        webUrl2='https://leetcode.com/tag/stack/'
        flag_var=1
    if 'queue' in user_message:
        webUrl='https://www.youtube.com/watch?v=zp6pBNbUB2U'
        webUrl2='https://leetcode.com/tag/queue/'
        flag_var=1
    if 'tree' in user_message:
        webUrl='https://www.youtube.com/watch?v=I_JuQ5ayPmc'
        webUrl2='https://leetcode.com/tag/tree/'
        flag_var=1
    if 'heap' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9'
        webUrl2='https://leetcode.com/tag/heap/'
        flag_var=1
    if 'hash' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PLqM7alHXFySGwXaessYMemAnITqlZdZVE'
        webUrl2='https://leetcode.com/tag/hash-table/'
        flag_var=1
    if 'trie' in user_message:
        webUrl='https://www.youtube.com/watch?v=AXjmTQ8LEoI'
        webUrl2='https://leetcode.com/tag/trie/'
        flag_var=1
    if 'graph' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PLl4Y2XuUavmtTOvFcW3HfI1oQ3hsgkB3a'
        webUrl2='https://leetcode.com/tag/graph/'
        flag_var=1
    if 'string' in user_message:
        webUrl='https://www.youtube.com/playlist?list=PLqjW-ORyj-hLKFq_ESmFpXDnaLKaTCMio'
        webUrl2='https://leetcode.com/tag/string/'
        flag_var=1
    if flag_var==1:
        return message1+'\n'+webUrl+'\n'+message2+'\n'+webUrl2
    else:
        return "I do not understand you"