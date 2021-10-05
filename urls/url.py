import re
                        # protocol (http,https,ftp), www, url with dot something
regexp = re.compile(r'''(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+''')