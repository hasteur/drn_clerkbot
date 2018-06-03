#Copyright 2009-2004 Ben Kurtovic <ben.kurtovic@gmail.com> From https://github.com/Mdann52/earwigbot-plugins/blob/develop/tasks/drn_clerkbot.py
#Copyright 2014 Hasteur <hasteur.wikipedia@gmail.com>
import wikipedia as pywikibot
import config
from pywikibot import i18n
import userlib
import datetime
import time
import re
class DRNClerkBot:
    STATUS_UNKNOWN = 0
    STATUS_NEW = 1
    STATUS_OPEN = 2
    STATUS_STALE = 4
    STATUS_NEEDASSIST = 4
    STATUS_RESOLVED = 6
    STATUS_CLOSED = 7
    STATUS_FAILED = 8
    STATUS_HOLD = 9
    ALIASES = {
        STATUS_NEW: ("",),
        STATUS_OPEN: ("open", "active", "inprogress"),
        STATUS_STALE: (),
        STATUS_NEEDASSIST: ("needassist", "review", "relist", "relisted","stale",),
        STATUS_RESOLVED: ("resolved", "resolve"),
        STATUS_CLOSED: ("closed", "close"),
        STATUS_FAILED: ("failed", "fail"),
        STATUS_HOLD: ("hold"),
    }
    def __init__(self):
        self.site = pywikibot.getSite()
        self.case_list = []
        self.volunteer_list = []
    def run(self):
        self.drn = pywikibot.Page(self.site,'Wikipedia:Dispute resolution noticeboard')
        self.get_volunteer_list()
        self.read_page()
        self.write_status()
    def get_volunteer_list(self):
        volunteer_list = pywikibot.Page(self.site,
            'Wikipedia:Dispute_resolution_noticeboard/Volunteering')
        page_text = volunteer_list.get()
        marker = "<!-- please don't remove this comment (used by EarwigBot) -->"
        text = page_text.split(marker)[1]
        for line in text.splitlines():
            user = re.search("\# \{\{User\|(.+?)\}\}", line)
            if user:
                uname = user.group(1).replace("_", " ").strip()
                self.volunteer_list.append(uname)
    def read_page(self):
        split = re.split("(^==\s*[^=]+?\s*==$)",self.drn.get(),flags = re.M|re.U)
        for i in xrange(len(split)):
            if i + 1 == len(split):
                break
            if not split[i].startswith("=="):
                continue
            title = split[i][2:-2].strip()
            body = old = split[i + 1]
            tl_status_esc = re.escape("DR case status")
            case_status = self.STATUS_NEW
            stat_search = re.search("\s*\{\{"+tl_status_esc+ "\|?(.*?)\}\}",body,re.U)
            if not stat_search:
                case_status = self.STATUS_NEW
            try:
              for option, names in self.ALIASES.iteritems():
                  if stat_search.group(1).lower() in names:
                      case_status = option
                      break
            except:
                case_status = self.STATUS_NEW
            case_vitals = self.parse_case_vitals(body)
            case_vitals['topic'] = title
            case_vitals['status'] = case_status
            self.case_list.append(case_vitals)
        pass
    def parse_case_vitals(self,case_body):
        return_parm = { 
            'created':'',
            'created_editor':'',
            'last_updater':'',
            'last_updated':'', 
            'last_volunteer':'',
            'volunteer_update':''
        }
        applicable_signatures = self.read_signatures(case_body)
        try:
            sort_sig = sorted(applicable_signatures, 
                key = lambda signature: signature[1]
            )
            return_parm['created'] = '{{DRNAgo|%s}}' % sort_sig[0][1]
            return_parm['created_editor'] = sort_sig[0][0]
        except:
            return_parm['created'] = "'''Unknown'''"
            return_parm['created_editor'] = 'Example'
            sort_sig = sorted(applicable_signatures[1:], 
                key = lambda signature: signature[1]
            )
        try:
            return_parm['last_updater'] = sort_sig[-1][0]
            return_parm['last_updated'] = sort_sig[-1][1]
        except:
            return_parm['last_updater'] = ''
            return_parm['last_updated'] = 'Unknown'

        return_parm['last_volunteer'] = ''
        return_parm['volunteer_update'] = 'Unknown'
        for signature in sort_sig:
            if signature[0] in self.volunteer_list:
                return_parm['last_volunteer'] = signature[0]
                return_parm['volunteer_update']= signature[1]
        return return_parm
    def read_signatures(self, text):
        """Return a list of all parseable signatures in the body of a case.
        Signatures are returned as tuples of (editor, timestamp as datetime).
        """
        regex = r"\[\[(?:User(?:\stalk)?\:|Special\:Contributions\/)"
        regex += r"([^\n\[\]|]{,256}?)(?:\||\]\])"
        regex += r"(?!.*?(?:User(?:\stalk)?\:|Special\:Contributions\/).*?)"
        regex += r".{,256}?(\d{2}:\d{2},\s\d{1,2}\s\w+\s\d{4}\s\(UTC\))"
        matches = re.findall(regex, text, re.U|re.I)
        match_2 = re.findall(r"\{\{drn filing editor\|(?P<username>.+)\|(?P<stamp>.+)\}\}",text, re.U|re.I)
        signatures = []
        try:
            timestamp = datetime.datetime.strptime(match_2[0][1], "%H:%M, %d %B %Y (UTC)")
            signatures.append((match_2[0][0],timestamp))
        except:
            # Shit... We didn't find the filing editor template. Raise unhloy 
            # stink
            signatures.append(('Example','Unknown'))
        for userlink, stamp in matches:
            username = userlink.split("/", 1)[0].replace("_", " ").strip()
            username = username[0].upper() + username[1:]
            if username == "DoNotArchiveUntil":
                continue
            stamp = stamp.strip()
            timestamp = datetime.datetime.strptime(stamp, "%H:%M, %d %B %Y (UTC)")
            signatures.append((username, timestamp))
        return signatures
    def write_status(self):
        DRN_case_status = "{{DRN case status/header|small={{{small|}}}|collapsed={{{collapsed|}}}}}\n"
        for case in self.case_list:
            row_string = """{{DRN case status/row|t=%(topic)s|d=%(topic)s|s=%(status)i|cu=%(created_editor)s|ct=%(created)s|vu=%(last_volunteer)s|vt={{DRNAgo|%(volunteer_update)s}}|mu=%(last_updater)s|mt={{DRNAgo|%(last_updated)s}}}}\n""" 
            case_string = row_string % case
            DRN_case_status += case_string
        DRN_case_status += "{{DRN case_status/footer|small={{{small|}}}}}"
        status_chart = pywikibot.Page(self.site,'Template:DRN case status')
        template_text = status_chart.get()
        new_text = re.sub(u"<!-- status begin -->(.*?)<!-- status end -->",
                           "<!-- status begin -->\n" + DRN_case_status + "\n<!-- status end -->",
                           template_text, flags=re.DOTALL)
        if template_text != new_text:
            new_text = re.sub("<!-- sig begin -->(.*?)<!-- sig end -->",
                              "<!-- sig begin -->~~~ at ~~~~~<!-- sig end -->",
                              new_text)
            status_chart.put(new_text,
                comment = "DRNClerkBot: Updating statistics for [[Wikipedia:DRN|dispute resolution noticeboard]]",
                minorEdit=False,
                botflag=True,
                maxTries=1
            )
        else:
            status_chart.put(new_text,
                comment = "DRNClerkBot: Updating statistics for [[Wikipedia:DRN|dispute resolution noticeboard]]",
                minorEdit=False,
                botflag=True,
                maxTries=1
            )

        pass
def main():
    drnbot = DRNClerkBot()
    drnbot.run()

if __name__ == "__main__":
    main()

