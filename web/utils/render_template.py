# (c) github - @IllegalDeveloper ,telegram - https://telegram.me/illegal_Developer
# removing credits doesn't make you coder 


from configs import Config
from helper import temp
from web.utils.custom_dl import TGCustomYield
import urllib.parse
import secrets
import mimetypes
import aiofiles
import logging
import aiohttp
from helper import temp


URL = Config.URL

def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

async def media_watch(message_id):
    media_msg = await temp.BOT.get_messages(int(Config.BIN_CHANNEL), message_id)
    file_properties = await TGCustomYield().generate_file_properties(media_msg)
    file_name, mime_type = file_properties.file_name, file_properties.mime_type
    src = urllib.parse.urljoin(URL, f'download/{message_id}')
    tag = mime_type.split('/')[0].strip()
    if tag == 'video':
        async with aiofiles.open('web/template/watch.html') as r:
            heading = 'Watch - {}'.format(file_name)
            html = (await r.read()).replace('tag', tag) % (heading, file_name, src)
    else:
        html = '<h1>This is not streamable file</h1>'
    return html
