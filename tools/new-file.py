import os
import datetime
title = input('Title: ')

filename = datetime.datetime.now().strftime("%Y%m%d%H%M-") + title + '.py'
url = f'https://github.com/full-stack-hero/snippet/blob/master/snippet/snippets/{filename}'
print('Create new file', filename)

with open(f'snippets/{filename}', 'w') as f:
    f.write(f'# :autor: @full.stack.hero\n')
    f.write(f'# :url: {url}\n\n')
