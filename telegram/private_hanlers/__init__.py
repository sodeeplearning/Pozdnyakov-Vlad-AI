from aiogram import Router

from . import post, sendfrom, logs, info


router = Router()

router.include_router(post.router)
router.include_router(sendfrom.router)
router.include_router(logs.router)
router.include_router(info.router)
