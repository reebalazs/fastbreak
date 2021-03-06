from persistent.mapping import PersistentMapping

from substanced.content import content
from substanced.folder import Folder

from ..interfaces import ICoach

@content(
    ICoach,
    name='Coach',
    icon='icon-tags',
    )
class Coach(Folder):
    def __init__(self, external_id, firstname, lastname,
                 team_name, props):
        Folder.__init__(self)
        self.external_id = external_id
        self.firstname = firstname
        self.lastname = lastname
        self.team_name = team_name
        self.title = lastname + ', ' + firstname

        self.props = PersistentMapping()

        for k,v in props.items():
            self.props[k] = v
