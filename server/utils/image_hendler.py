

import os
import base64
import uuid
IMAGEDIR=os.getcwd()

async def image_upload(Hax_Value):
    try:
        random_name = str(uuid.uuid4())
        path="server/static/"+random_name+".jpg"
        imgname = open(path, 'wb')
        imgname.write(base64.b64decode(Hax_Value))
        imgname.close()
        img_path =IMAGEDIR+chr(92) +"server"+chr(92)+"static"+chr(92)+str(random_name) +".jpg"
        return img_path
    except:
        return ""
    
