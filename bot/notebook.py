from typing import List, Optional
from bot.note import Note


class Notebook:
    def __init__(self):
        self._notes: List[Note] = []

    @property
    def notes(self) -> List[Note]:
        return self._notes
