from typing import Optional

from sqlalchemy.orm import Session

from app.models import Task
from core.repositories.abstract_repository import AbstractRepository


class TaskRepository(AbstractRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, task_id: int) -> Task:
        task = self.get_or_none(task_id)
        if not task:
            raise LookupError(f'Task ID={task_id} not found')
        return task

    def get_or_none(self, task_id: int) -> Optional[Task]:
        return self.session.get(Task, task_id)

    def create(self, task: Task) -> Task:
        self.session.add(Task)
        self.session.commit()
        self.session.refresh(task)
        return task
