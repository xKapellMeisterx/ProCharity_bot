from core.repositories.task_repository import TaskRepository
from app.database import db_session


class TaskService:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository
