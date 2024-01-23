# vim: set fileencoding=utf-8
"""
pythoneda/runtime/infrastructure/eventstoredb/eventstoredb.py

This script defines the EventStoreDB class.

Copyright (C) 2024-today rydnr's pythoneda-runtime-infrastructure/eventstoredb

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared import EventListener, listen
from pythoneda.runtime.infrastructure.events.eventstoredb import (
    EventstoredbBooted,
    EventstoredbBootRequested,
)


class EventStoreDB(EventListener):
    """
    Reacts to EventStoreDB infrastructure events.

    Class name: Boot

    Responsibilities:
        - Boot up EventStoreDB.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new EventStoreDB instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.runtime.infrastructure.eventstoredb.EventStoreDB
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(EventstoredbBootRequested)
    async def listen_EventstoredbBootRequested(
        cls, event: EventstoredbBootRequested
    ) -> EventstoredbBooted:
        """
        Gets notified of a EventstoredbBootRequested event.
        Emits a EventstoreBooted event.
        :param event: The event.
        :type event: pythoneda.runtime.infrastructure.events.eventstoredb.EventstoredbBootRequested
        :return: The event of EventStoreDB booted up.
        :rtype: pythoneda.runtime.infrastructure.events.eventstoredb.EventstoredbBooted
        """
        print("TODO!!!!")


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
