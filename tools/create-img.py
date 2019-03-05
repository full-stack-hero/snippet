from os import listdir
from os.path import isfile, join, splitext
from code2image.cls import Code2ImageBackground

tags = [
    'fullstackhero', 'design', 'hacking', 'softwareengineer', 'programminglife',
    'dev', 'webdev', 'business', 'hacker', 'engineer', 'art', 'programmerslife',
    'coders', 'developers', 'programmerlife', 'programmingmemes', 'website',
    'nodejs', 'softwareengineering', 'angular', 'frontend', 'machinelearning',
    'artificialintelligence', 'devlife', 'worldcode', 'innovation',
    'cybersecurity', 'electronics', 'geek', 'nerd',
]

def check_meta(s, meta):
    for key in [':autor:', ':url:']:
        if s.startswith(key):
            meta[key[1:-1]] = s[len(key):].strip()
            return True
    return False


def make(code_file):
    with open(f'snippets/{code_file}.py') as f:
        data = f.readlines()

    data = [x.strip('\n') for x in data]

    n = 0
    while True:
        if not data[n].strip().startswith('#'):
            break
        n += 1

    caption = ''
    meta = {}
    for d in data[:n]:
        s = d.strip('# ')
        if not s:
            caption += '\n'
            continue

        if not check_meta(s, meta):
            caption += s + ' '

    code = '\n'.join(data[n:])
    #if meta.get('autor'):
    #    code = '{}\n\n{}'.format(meta.get('autor'), code)

    with open(f'out/{code_file}.txt', 'w') as f:
        f.write(caption+'\n')
        if meta.get('url'):
            f.write('\nsource: '+ meta.get('url')+'\n')
        f.write(' '.join(['#'+t for t in tags]))

    c2i = Code2ImageBackground()
    img = c2i.highlight(code)
    img.save(f'out/{code_file}.png')



onlyfiles = sorted([splitext(f)[0] for f in listdir('snippets') if isfile(join('snippets', f))], reverse=True)
for filename in onlyfiles[:5]:
    make(filename)
