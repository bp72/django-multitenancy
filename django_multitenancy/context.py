from contextvars import ContextVar


current_tenant = ContextVar("current_tenant", default=None)
