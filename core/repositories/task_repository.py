from typing import Optional

from app.models import Task
from core.repositories.abstract_repository import AbstractRepository
from sqlalchemy.orm import Session


class TaskRepository(AbstractRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_or_none(self, telegram_id: int) -> Optional[Task]:
        return self.session.get(Task, telegram_id)

    def get(self, telegram_id: int) -> Task:
        task = self.get_or_none(telegram_id)
        if not task:
            raise LookupError(f'Task ID={telegram_id} not found')
        return task

    def create(self, task: Task) -> Task:
        self.session.add(Task)
        self.session.commit()
        self.session.refresh(task)
        return task
