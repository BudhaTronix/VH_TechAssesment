import subprocess
from urllib.request import Request, urlopen

req = Request(
    url = 'https://cdn.fbsbx.com/v/t59.3654-21/15720510_10211855778255994_5430581267814940672_n.mp4/audioclip-1484407992000-3392.mp4?oh=a78286aa96c9dea29e5d07854194801c&oe=587C3833',
    headers={'User-Agent': 'Mozilla/5.0'}
)
mp4file = urlopen(req).read()
def convertToWAV(input, output):
    with open(input, "wb") as handle:
        handle.write(mp4file.read())

    cmdline = ['avconv',
               '-i',
               'test.mp4',
               '-vn',
               '-f',
               'wav',
               output]
    subprocess.call(cmdline)
