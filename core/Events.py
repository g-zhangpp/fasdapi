from typing import Callable

from fastapi import FastAPI

def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        # app 启动完成后触发
        print("启动完毕")
        # await init_db()
    return app_start

def stopping(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        print("停止")
    return stop_app