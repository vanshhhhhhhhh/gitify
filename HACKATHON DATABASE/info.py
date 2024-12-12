import sqlite3


conn = sqlite3.connect('GITIF.db')


c = conn.cursor()

infoo = [
    ('2dust /\n\n      v2rayN' , 'https://github.com/2dust/v2rayN' ,'11599' , '70341'),
    ('EbookFoundation /\n\n      free-programming-books' , 'https://github.com/EbookFoundation/free-programming-books','61802','339671'),
    ('jesseduffield /\n\n    lazydocker','https://github.com/jesseduffield/lazydocker','1215','38090'),
    ('bluesky-social /\n\n      social-app','https://github.com/bluesky-social/social-app','1617','127061'),
    ('abi /\n\n      screenshot-to-code','https://github.com/abi/screenshot-to-code','7524','61530'),
    ('termux /\n\n      termux-app','https://github.com/termux/termux-app','3861','36806'),
    ('black-forest-labs /\n\n      flux','https://github.com/black-forest-labs/flux','1244','17607'),
    ('OpenInterpreter /\n\n      open-interpreter','https://github.com/OpenInterpreter/open-interpreter','4850','56029'),
    ('public-apis /\n\n      public-apis','https://github.com/public-apis/public-apis','33925','318562'),
    ('gitroomhq /\n\n      postiz-app','https://github.com/gitroomhq/postiz-app','2337','11601'),
    ('bluesky-social /\n\n      atproto','https://github.com/bluesky-social/atproto','512','7227'),
    ('FortAwesome /\n\n      Font-Awesome','https://github.com/FortAwesome/Font-Awesome','12203','74209'),
    ('shader-slang /\n\n      slang','https://github.com/shader-slang/slang',' 210','2923')
]

c.executemany("INSERT INTO gitify VALUES(?,?,?,?)",infoo)
 
print("Task completed.")
conn.commit()

conn.close()
