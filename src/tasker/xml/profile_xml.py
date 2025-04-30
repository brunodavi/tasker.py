from .xml_builder import XmlBuilder

from tasker.py.profile import Profile
from tasker.profiles import Time


class ProfileXml(XmlBuilder):
    def __init__(self, profile: Profile):
        self.profile = profile

    def _create_event(self):
        E = self.E

        profile_event = self.profile.event

        match profile_event:
            case Time():
                start_hour = str(profile_event.start_hour)
                start_minute = str(profile_event.start_minute)

                end_hour = str(profile_event.end_hour)
                end_minute = str(profile_event.end_minute)

                every_type = profile_event._every_type

                every_list = []

                if (every_type is not None):
                    every_type = str(every_type)
                    every_value = str(
                        profile_event._every_value
                    )

                    every_list = [
                        E.rep(every_type),
                        E.repval(every_value)
                    ]

                yield E.Time(
                    E.fh(start_hour),
                    E.fm(start_minute),
                    *every_list,
                    E.th(end_hour),
                    E.tm(end_minute),
                    sr='con0'
                )

    def to_xml(self):
        E = self.E

        profile_id = str(self.profile.id)
        task_id = str(self.profile.task_id)
        profile_name = self.profile.name

        return E.Profile(
            E.cdate('0'),
            E.edate('1'),
            E.flags('8'),
            E.id(profile_id),
            E.mid0(task_id),
            E.nme(profile_name),
            *self._create_event(),
            sr='prof'
        )
