from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id: UUID = Field(default=None, primary_key=True)
    username: str = Field()
    email: str = Field()


class Profile(SQLModel, table=True):
    id: UUID = Field(
        default=None,
        primary_key=True,
        foreign_key="auth.users.id",
        nullable=False,
        ondelete="CASCADE",
    )
    name: Optional[str] = Field(default=None)
    email: str = Field()
    date_joined: datetime = Field(default=datetime.now())
    date_last_login: Optional[datetime] = Field(default=None)


class Section(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(default="New Section", description="Title of the Section")
    section_order: int = 0
    pages: list["Page"] = Relationship(back_populates="section")


class Page(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(default="New Page", description="Title of the page")
    locked: bool = Field(
        default=False, description="Whether being a user is needed to view the page"
    )
    section: Section = Relationship(back_populates="pages")
    page_order: int = 0
    active: bool = Field(default=True, description="Whether the page is active")
    beta: bool = Field(default=False, description="Whether the page is in beta")
    path: str = Field(default="pages/test.py", description="Path to the page")


class UserEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: UUID = Field(default=None, foreign_key="profile.id")
    event: str = Field(description="What is happening. Should be eg. 'Complete page'")
    page: Optional[int] = Field(
        default=None,
        description="If applicable, a page to which this applies to.",
        foreign_key="page.id",
    )
    time: datetime
