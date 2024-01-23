# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/events/lifecycle/boot.py

This script defines the Boot class.

Copyright (C) 2024-today rydnr's pythoneda-runtime/boot

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
from pythoneda.runtime.events.lifecycle import Booted, BootRequested


class Boot(EventListener):
    """
    Reacts to BootRequested events.

    Class name: Boot

    Responsibilities:
        - Boot up PythonEDA domains.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Boot instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.artifact.git.GitArtifact
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(BootRequested)
    async def listen_BootRequested(cls, event: BootRequested) -> Booted:
        """
        Gets notified of a BootRequested event.
        Emits a Booted event.
        :param event: The event.
        :type event: pythoneda.runtime.events.lifecycle.BootRequested
        :return: The event of a domain booted up.
        :rtype: pythoneda.runtime.events.lifecycle.Booted
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
